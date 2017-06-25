import time
import datetime
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


# Configure the count of pixels, SPI Device and Port:
from numbers import Number

PIXEL_COUNT = 150
SPI_PORT = 0
SPI_DEVICE = 1
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_DEVICE, SPI_PORT), gpio=GPIO)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

number = Number(pixels)

def set_pixel(x, y, color):
    if y % 2 == 0:
        pixel_num = 15*y+x
    else:
        pixel_num = 15*(y+1)-x-1

    r, b, g = color
    pixels.set_pixel(pixel_num, Adafruit_WS2801.RGB_to_color(r, g, b))

def draw_hour_minutes(hours, minutes):
    first_digit = hours / 10
    second_digit = hours % 10
    third_digit = minutes / 10
    fourth_digit = minutes % 10

    number.draw(first_digit, 0, 2, RED)
    number.draw(second_digit, 4, 2, RED)
    number.draw(third_digit, 8, 2, RED)
    number.draw(fourth_digit, 12, 2, RED)

def draw_minutes_seconds(minutes, seconds):
    first_digit = minutes / 10
    second_digit = minutes % 10
    third_digit = seconds / 10
    fourth_digit = seconds % 10

    number.draw(first_digit, 0, 2, RED)
    number.draw(second_digit, 4, 2, RED)
    number.draw(third_digit, 8, 2, RED)
    number.draw(fourth_digit, 12, 2, RED)

def timer():
    start_sec = time.time()

    while True:
        current_sec = time.time()

        seconds = int(current_sec - start_sec) % 60
        minutes = (int(current_sec - start_sec) / 60) % 60
        hours = ((int(current_sec - start_sec) / 60) / 60) % 24

        print hours, " ", minutes, " ", seconds

        pixels.clear()

        current = seconds % 9
        set_pixel(7, 9 - current, RED)
        set_pixel(7, current, BLUE)

        if hours > 0:
            draw_hour_minutes(hours, minutes)
        else:
            draw_minutes_seconds(minutes, seconds)

        pixels.show()
        time.sleep(0.5)

if __name__ == "__main__":
    pixels.clear()
    pixels.show()

    timer()

    pixels.show()
    time.sleep(5)

    pixels.clear()
    pixels.show()