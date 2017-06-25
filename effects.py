import math
from random import randint


class Effects:
    def __init__(self, matrix):
        self.matrix = matrix

        # rings_center_to_outside
        self.rings_num = 0
        self.rings_color = []

    def random_dots(self, set_likelihood):

        set_a_pixel = randint(0, 100)
        if (set_a_pixel < set_likelihood * 100):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            x = randint(0, self.matrix.WIDTH - 1)
            y = randint(0, self.matrix.HEIGHT - 1)

            self.matrix.set(x, y, (r, g, b))

    def rings_center_to_outside(self, color):

        # self.draw_ring(self.rings_num, color)
        for i in range(0, 7, 2):
            if self.rings_num % 2 == 0:
                self.draw_ring(i, color)
            else:
                self.draw_ring(i + 1, color)
        self.rings_num += 1

    def draw_ring(self, num, color):
        for i in range(num + 1):
            if 0 <= i < 7 and 0 <= num <= 4:
                self.matrix.set(7 + i, 4 - num, color)
                self.matrix.set(7 + i, 5 + num, color)
                self.matrix.set(7 - i, 4 - num, color)
                self.matrix.set(7 - i, 5 + num, color)

            if 0 <= i <= 4 and 0 <= num <= 7:
                self.matrix.set(7 - num, 4 - i, color)
                self.matrix.set(7 - num, 5 + i, color)
                self.matrix.set(7 + num, 4 - i, color)
                self.matrix.set(7 + num, 5 + i, color)
