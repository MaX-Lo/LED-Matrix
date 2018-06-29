"""
by MaX-Lo 29.06.2018

Helper class for drawing digits at a 3 (width) by 5 (height) size.
"""


class Number:
    def __init__(self, matrix):
        self.matrix = matrix

    def draw(self, digit, x, y, color):
        """
        draw the given digit at position x, y in color

        :param digit - digit to draw, has to be in range 0..9
        :param color - digits color as (r, g, b) color tuple
        :param x - left coordinate of the digit
        :param y - top coordinate of the digit
        """
        assert 0 <= digit <= 9, "Digit has to be in range 0..9"
        if digit == 0:
            self.zero(x, y, color)
        elif digit == 1:
            self.one(x, y, color)
        elif digit == 2:
            self.two(x, y, color)
        elif digit == 3:
            self.three(x, y, color)
        elif digit == 4:
            self.four(x, y, color)
        elif digit == 5:
            self.five(x, y, color)
        elif digit == 6:
            self.six(x, y, color)
        elif digit == 7:
            self.seven(x, y, color)
        elif digit == 8:
            self.eight(x, y, color)
        elif digit == 9:
            self.nine(x, y, color)

    def zero(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x, y + 3, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def one(self, x, y, color):
        """ :param x, y: top left corner of the number minus two for formatting all numbers equal
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 1, y + 1, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x + 1, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def two(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def three(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def four(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x + 2, y + 4, color)

    def five(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def six(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x, y + 3, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def seven(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x + 2, y + 4, color)

    def eight(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x, y + 3, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)

    def nine(self, x, y, color):
        """ :param x, y: top left corner of number
            number is 3x5 in size"""
        self.matrix.set(x, y, color)
        self.matrix.set(x + 1, y, color)
        self.matrix.set(x + 2, y, color)
        self.matrix.set(x, y + 1, color)
        self.matrix.set(x + 2, y + 1, color)
        self.matrix.set(x, y + 2, color)
        self.matrix.set(x + 1, y + 2, color)
        self.matrix.set(x + 2, y + 2, color)
        self.matrix.set(x + 2, y + 3, color)
        self.matrix.set(x, y + 4, color)
        self.matrix.set(x + 1, y + 4, color)
        self.matrix.set(x + 2, y + 4, color)