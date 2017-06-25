class Number:
    def __init__(self, matrix):
        self.matrix = matrix

    def draw(self, num, x, y, color):
        assert 0 <= num <= 9, "Number must be from 0 to 9"
        if num == 0:
            self.zero(x, y, color)
        elif num == 1:
            self.one(x, y, color)
        elif num == 2:
            self.two(x, y, color)
        elif num == 3:
            self.three(x, y, color)
        elif num == 4:
            self.four(x, y, color)
        elif num == 5:
            self.five(x, y, color)
        elif num == 6:
            self.six(x, y, color)
        elif num == 7:
            self.seven(x, y, color)
        elif num == 8:
            self.eight(x, y, color)
        elif num == 9:
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