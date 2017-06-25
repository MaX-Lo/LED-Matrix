import time
import datetime

# Configure the count of pixels, SPI Device and Port:
import colors
from matrix import Matrix

matrix = Matrix()


def draw_time():
    # background color:
    bg_color = (0, 100, 255)
    # digit color:
    digit_color = colors.WHITE

    while True:
        matrix.clear()

        # get time in minutes and hours
        minutes = datetime.datetime.now().time().minute
        hours = datetime.datetime.now().time().hour
        sec = datetime.datetime.now().time().second
        micro_sec = datetime.datetime.now().time().microsecond

        draw_seconds(bg_color, sec, micro_sec)

        # set two pixels between hour and minute digits
        matrix.set(7, 9, digit_color)
        matrix.set(7, 0, digit_color)

        # convert time into 4 digits
        first_digit = hours / 10
        second_digit = hours % 10
        third_digit = minutes / 10
        fourth_digit = minutes % 10

        matrix.number.draw(first_digit, 0, 2, digit_color)
        matrix.number.draw(second_digit, 4, 2, digit_color)
        matrix.number.draw(third_digit, 8, 2, digit_color)
        matrix.number.draw(fourth_digit, 12, 2, digit_color)

        matrix.show()

        time.sleep(0.1)


def draw_seconds(color, sec, micro_sec):
    color_r, color_g, color_b = color

    # fading after full minute is over
    if sec < 1:
        factor = (micro_sec + ((sec % 1) * 1000000))
        brightness_r = color_r - int(factor * color_r / 1000000)
        brightness_g = color_g - int(factor * color_g / 1000000)
        brightness_b = color_b - int(factor * color_b / 1000000)
        for i in range(1, 15):
            for j in range(8, 10):
                matrix.set(i, j, (brightness_r, brightness_g, brightness_b))

    # draw seconds progress in the background
    rows = sec / 4
    factor = micro_sec + ((sec % 4) * 1000000)
    brightness_r = int(factor * color_r / 4000000)
    brightness_g = int(factor * color_g / 4000000)
    brightness_b = int(factor * color_b / 4000000)
    for i in range(rows):
        for j in range(8, 10):
            matrix.set(i, j, (color_r, color_g, color_b))
    for j in range(8, 10):
        matrix.set(rows, j, (brightness_r, brightness_g, brightness_b))


if __name__ == "__main__":
    matrix.clear()
    matrix.show()

    draw_time()

    matrix.clear()
    matrix.show()
