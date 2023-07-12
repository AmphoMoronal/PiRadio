"""
    IMPORTANT:
    THIS VOLUME MANAGMENT ONLY WORK ON LINUX SYSTEMS!!!
    IF YOU WANT TO USE IT ON OTHER SYSTEMS THAN YOU HAVE TO REWRITE IT!
"""

from subprocess import call, run
import os

output_device = "Master"


def get_volume():
    volume = os.popen("amixer get Master | grep -o [0-9]*%|sed 's/%//'").readline()
    return int(volume)


def set_volume(volume):
    call(["amixer", "-D", "pulse", "sset", "Master", f"{volume}%", ">>", "/dev/null"])


def mute():
    call(["amixer", "-D", "pulse", "sset", "Master", "0%", ">>", "/dev/null"])


def increase():
    call(["amixer", "-D", "pulse", "sset", "Master", "5%+", ">>", "/dev/null"])


def decrease():
    call(["amixer", "-D", "pulse", "sset", "Master", "5%-", ">>", "/dev/null"])

