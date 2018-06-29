import time
from random import random, randint

from matrix import Matrix


def draw_time(matrix : Matrix):

    green_1 = (0, 255, 0)
    green_2 = (0, 200, 0)
    green_3 = (0, 150, 0)
    green_4 = (0, 100, 0)

    """ Idea:
    generate random pixels at the screen top which fall down with a constant speed
    tearing a 4 pixel long tail that gets darker with each pixel
    """
    raindrops = []

    while True:
        matrix.clear()

        if random() < 0.3:
            pos = (randint(0, matrix.WIDTH - 1), 0)
            raindrops.append(pos)

        for i in range(len(raindrops)):
            if raindrops[i][1] <= matrix.HEIGHT + 3:
                if raindrops[i][1] < matrix.HEIGHT:
                    matrix.set(raindrops[i][0], raindrops[i][1], green_1)
                if 0 <= raindrops[i][1] - 1 < matrix.HEIGHT:
                    matrix.set(raindrops[i][0], raindrops[i][1] - 1, green_2)
                if 0 <= raindrops[i][1] - 2 < matrix.HEIGHT:
                    matrix.set(raindrops[i][0], raindrops[i][1] - 2, green_3)
                if 0 <= raindrops[i][1] - 3 < matrix.HEIGHT:
                    matrix.set(raindrops[i][0], raindrops[i][1] - 3, green_4)

                raindrops[i] = (raindrops[i][0], raindrops[i][1] + 1)

        for drop in raindrops:
            if drop[1] > matrix.HEIGHT + 3:
                raindrops.remove(drop)

        matrix.show()

        time.sleep(0.1)


if __name__ == "__main__":
    matrix = Matrix()

    matrix.clear()
    matrix.show()

    draw_time(matrix)

    matrix.clear()
    matrix.show()