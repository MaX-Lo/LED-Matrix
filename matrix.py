from RPi import GPIO

import Adafruit_WS2801

from effects import Effects
from numbers import Number

"""
by MaX-Lo 29.06.2018

class to interact with the matrix by providing methods to manipulate pixels color

ToDo: values in __init__ must be adjusted to your specific matrix layout

Assumption: the Matrix consists of one LED stripe in a snake like shape
somehow like this:
___________________________________________
|  ------------------------------------.  |
|  .-----------------------------------'  |
|  '-----------------------------------.  |
|  .-----------------------------------'  |
|  '-----------------------------------.  |
|  .-----------------------------------'  |
|  '-----------------------------------.  |
|  ------------------------------------'  |
|_________________________________________|
"""


class Matrix:
    def __init__(self):
        # equals max x coordinate
        self.WIDTH = 15

        # equals max y coordinate
        self.HEIGHT = 10
        self.PIXEL_COUNT = self.WIDTH * self.HEIGHT

        # following two values depend on the PINs you used on your Pi
        # the SPI port you choose on your RaspPi
        SPI_PORT = 0
        # the SPI device you choose on your RaspPI
        SPI_DEVICE = 1

        self.pixels = Adafruit_WS2801.WS2801Pixels(self.PIXEL_COUNT, spi=Adafruit_WS2801.SPI.SpiDev(SPI_DEVICE, SPI_PORT), gpio=GPIO)

        # ToDo should that really be a part of matrix? Maybe better to include extra scripts/helpers as you need them.
        self.number = Number(self)
        self.effect = Effects(self)

    def set(self, x, y, color):
        """
        set color of LED at x, y with color

        :param x: pixels x coordinate
        :param y: pixels y coordinate
        :param color: tuple with r, g, b values, each in range 0..255
        """
        if y % 2 == 0:
            pixel_num = 15 * y + x
        else:
            pixel_num = 15 * (y + 1) - x - 1

        r, b, g = color
        self.pixels.set_pixel(pixel_num, Adafruit_WS2801.RGB_to_color(r, g, b))

    def get(self, x, y):
        """
        get r, g, b color tuple at position x, y

        :param x: pixels x coordinate
        :param y: pixels y coordinate
        :returns (r,g,b)
        """
        if y % 2 == 0:
            pixel_num = 15 * y + x
        else:
            pixel_num = 15 * (y + 1) - x - 1

        self.pixels.get_pixel(pixel_num)

    def clear(self):
        """
        set all pixels color to (0, 0, 0)
        """
        self.pixels.clear()

    def show(self):
        """
        apply color changes to the matrix
        should get called to apply changes from one or more set() calls
        """
        self.pixels.show()
