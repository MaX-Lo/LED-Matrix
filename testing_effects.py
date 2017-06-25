import time

from matrix import Matrix


def random_dots_main():
    matrix = Matrix()
    matrix.clear()
    while True:
        matrix.effect.random_dots(0.5)
        matrix.show()
        time.sleep(0.1)

def main():
    matrix = Matrix()
    matrix.clear()
    i = 0
    while True:
        i += 1
        matrix.clear()
        if (i % 3 == 0):
            matrix.effect.rings_center_to_outside((0, 255, 0))
        elif (i % 3 == 1):
            matrix.effect.rings_center_to_outside((255, 0, 0))
        else:
            matrix.effect.rings_center_to_outside((0, 0, 255))

        matrix.show()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
