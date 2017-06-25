from RPi import GPIO

import Adafruit_WS2801

from effects import Effects
from numbers import Number


class Matrix:

    def __init__(self):
        self.PIXEL_COUNT = 150
        self.WIDTH = 15
        self.HEIGHT = 10

        PIXEL_COUNT = 150
        SPI_PORT = 0
        SPI_DEVICE = 1
        self.pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=Adafruit_WS2801.SPI.SpiDev(SPI_DEVICE, SPI_PORT), gpio=GPIO)

        self.number = Number(self)
        self.effect = Effects(self)

    def set(self, x, y, color):
        if y % 2 == 0:
            pixel_num = 15 * y + x
        else:
            pixel_num = 15 * (y + 1) - x - 1

        r, b, g = color
        self.pixels.set_pixel(pixel_num, Adafruit_WS2801.RGB_to_color(r, g, b))

    def get(self, x, y):
        if y % 2 == 0:
            pixel_num = 15 * y + x
        else:
            pixel_num = 15 * (y + 1) - x - 1

        self.pixels.get_pixel(pixel_num)

    def clear(self):
        self.pixels.clear()

    def show(self):
        self.pixels.show()
