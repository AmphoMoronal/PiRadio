# Basic Imports from kivy
from kivy.lang import Builder
from kivymd.app import MDApp

# Import to Change the Window Size
from kivy.core.window import Window

# Import to Build the UI
from kivymd.uix.dialog import MDDialog      # PopUp Window
from kivy.clock import Clock

# for internet and clock
from urllib import request
from datetime import datetime

# volume and radio managers
from modules import volume, radio_manager

# sets the window size
Window.size = (1036, 606)


class RadioApp(MDApp):
    def build(self):
        # set the theme colors
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("radio.kv")    # load the kv file

    # some variables
    p = None
    default_volume = 0  # sets the Default Volume when you start the program
    muted = True        # defines if the radio starts muted or not
    channel = 0
    icon = 0
    play = False        # autoplay at start of program
    internet = False    # default Value for the internet

    # Executed if Ui is loaded
    def on_start(self):
        self.root.ids.volume_slider.value = self.default_volume     # sets the volume (Slider and on the machine)
        self.root.ids.volume_slider.disabled = True                 # diable the slider
        self.root.ids.radio_icon.source = radio_manager.icons[self.icon]    # sets the stream icon
        Clock.schedule_interval(self.update_time, 1)    # start the clock

    # update the clock
    def update_time(self, *args):
        self.root.ids.time_label.text = str(datetime.now().strftime("%H:%M:%S"))

    # Popup when you don't have an internet connection
    @staticmethod
    def show_dialog():
        dialog = MDDialog(
            title="Kein Internet",
            text="Aktuell ist kein Internetzugriff vorhanden, bitte stellen Sie eine Verbindung zum Internet her."
        )
        dialog.open()

    # Volume functions
    def change_volume(self, *args):
        volume.set_volume(args[1])
        self.root.ids.volume_slider.value = volume.get_volume()

    def volume_up(self, *args):
        self.stream()
        if self.root.ids.volume_slider.disabled:
            self.root.ids.volume_slider.disabled = False
            self.muted = False
        volume.set_volume(self.root.ids.volume_slider.value + 5)
        self.root.ids.volume_slider.value = volume.get_volume()

    def volume_down(self, *args):
        self.stream()
        if self.root.ids.volume_slider.disabled:
            self.root.ids.volume_slider.disabled = False
            self.muted = False
        volume.set_volume(self.root.ids.volume_slider.value - 5)
        self.root.ids.volume_slider.value = volume.get_volume()

    def mute(self):
        if not self.muted:
            volume.mute()
            self.muted = True
            self.root.ids.volume_slider.disabled = True

        elif self.muted:
            self.stream()
            volume.set_volume(self.root.ids.volume_slider.value)
            self.muted = False
            self.root.ids.volume_slider.disabled = False

    # start and end the radio streams
    def stream(self):
        self.check_internet()
        if self.internet:
            if not self.play:
                radio_manager.play(self.channel)
                self.play = True

            else:
                radio_manager.kill()
                self.play = False

        else:
            self.show_dialog()

    # switching Channels
    def next_channel(self):
        self.play = False
        if self.channel == len(radio_manager.channels) - 1:
            self.channel = 0
            self.icon = 0
            radio_manager.kill()
            self.p = radio_manager.play(self.channel)
            self.play = True
            self.root.ids.radio_icon.source = radio_manager.icons[self.icon]
        else:
            self.channel += 1
            self.icon += 1
            radio_manager.kill()
            self.p = radio_manager.play(self.channel)
            self.play = True
            self.root.ids.radio_icon.source = radio_manager.icons[self.icon]

    def prev_channel(self):
        self.play = False
        if self.channel == 0:
            self.channel = len(radio_manager.channels) - 1
            self.icon = len(radio_manager.channels) - 1
            radio_manager.kill()
            self.p = radio_manager.play(self.channel)
            self.play = True
            self.root.ids.radio_icon.source = radio_manager.icons[self.icon]

        else:
            self.channel -= 1
            self.icon -= 1
            radio_manager.kill()
            self.p = radio_manager.play(self.channel)
            self.play = True
            self.root.ids.radio_icon.source = radio_manager.icons[self.icon]

    # checks the internet Connection
    def check_internet(self, host='http://google.com'):
        try:
            request.urlopen(host)
            self.internet = True
        except:
            radio_manager.kill()
            self.internet = False


if __name__ == "__main__":
    RadioApp().run()
