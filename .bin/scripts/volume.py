import os, sys
import subprocess

from optparse import OptionParser

def main():
    if os.environ["AUDIO_OUTPUT"] == "UNKNOWN":
        pactl_list = "pactl list"
        pactl_proc = subprocess.Popen()
