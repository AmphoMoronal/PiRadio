import multiprocessing
from playsound import playsound

# Stream links
hr1 = 'https://dispatcher.rndfnk.com/hr/hr1/live/mp3/high'
hr3 = 'https://dispatcher.rndfnk.com/hr/hr3/live/mp3/high'
hr4 = 'https://dispatcher.rndfnk.com/hr/hr4/mitte/mp3/high'
absolut_relax = 'https://absolut-relax.live-sm.absolutradio.de/absolut-relax/stream/mp3'

channels = [hr3, absolut_relax, hr1, hr4]       # Channel list
icons = ["./icons/hr3.png", "./icons/absolut_relax.png", "./icons/hr1.png", "./icons/hr4.png"]      # Icon list
streams = []    # List for current stream to kill them


def play(i=1):
    p = multiprocessing.Process(target=playsound, args=(channels[i],))
    streams.append(p)
    p.start()


def kill():
    for stream in streams:
        stream.kill()
        streams.remove(stream)
