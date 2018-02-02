#!/usr/bin/python2

from optparse import OptionParser
from colorsys import rgb_to_hls, hls_to_rgb

COLOR_CODE_MAX = "BE5046"
COLOR_CODE_MIN = "486A2F"

color_stage_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def color_triple():
    def __init__(fst, snd, thrd, color_space):
        self.first = fst
        self.second = snd
        self.third = thrd

    def change_value(color_change):
        (color_change_values, colorspace_string) = color_change((self.first, self.second, self.third))
        if colorspace_string != self.colorspace_string:
            (self.first, self.second, self.third) = color_change_values
        else:
            print "[!] ERROR: Could not convert colorspace to self\n"

    def get_tuple():
        return (self.first, self.second, self.third)


def main():
    parser = OptionParser

    parser.add_option("-v", "--value",
                      action="store", dest="val")

    (optiosn, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect Number of Arguments")

    return get_ram_color(args.val)

if __name__ == "__main__":
    main()
