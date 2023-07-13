# PiRadio
This radio is programmed for raspberry pis and only work completly on linux based systems

## Installation
- [Install python](https://www.python.org/downloads/)
- [install pip](https://pip.pypa.io/en/stable/installation/#get-pip-py)
- install requirements (```pip install -r requirements.txt```)
- start Program (or [convert it for Windows, Android, Mac, ...](https://kivy.org/doc/stable/guide/packaging.html))

## Usage
- Start the application and press the logo to start the radio
- if no internet you can close the popup with a press anywhere on the screen
- Change the Volume with the bottom slider (Only on linux based systems)
- if you don't use the system on a raspberry pi with the pi screen, you should remove the line in the ```radio.py``` file that
sizes the window

## Customisation
### Radio streams
In ```modules/radio_manager.py``` you can find the variables to the stream links and below the links for the icons.
(Note: The order of the links in the stream array and icons in the icon array have to be the same)

### Colors
You can change the color in the kv file under the ```md_bg_color``` values.

### UI
if you want you can rearrange the UI with a different Layout or some other stuff. For further information look at the
[Documentation](https://kivymd.readthedocs.io/en/latest/components/).
