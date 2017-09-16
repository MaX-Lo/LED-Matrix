import math
from time import sleep

from matrix import Matrix


def main():
    matrix = Matrix()

    base_color = (0, 0, 0)
    center = (7, 5)
    r, g, b = (31, 0, 0)

    steps = 0  # max = 8
    ascending = True

    color_step = (0, 0, 0)

    while True:
        matrix.clear()

        if ascending:
            steps += 1
            if steps >= 8:
                ascending = False
        else:
            steps -= 1
            if steps <= 0:
                ascending = True
                r, g, b, color_step = change_color(color_step, r, g, b)

        for i in range(center[0]+1):
            for j in range(center[1]):

                factor = math.sqrt( (i*i)+(j*j) )
                factor = (steps - factor)
                if factor < 0:
                    factor = 0

                curr_color = (base_color[0] + int(factor*r), base_color[1] + int(factor*g), base_color[2] + int(factor*b))

                matrix.set(center[0] - i, center[1] -1 - j, curr_color)
                matrix.set(center[0] + i, center[1] + j, curr_color)
                matrix.set(center[0] - i, center[1] + j, curr_color)
                matrix.set(center[0] + i, center[1] -1 - j, curr_color)

        matrix.show()
        sleep(0.075)


def change_color(color_step, r, g, b):
    rs, gs, bs = color_step

    if (rs < 31):
        r -= 4
        g += 4
        rs += 4
    elif (gs < 31):
        g -= 4
        b += 4
        gs += 4
    elif (bs < 31):
        b -= 4
        r += 4
        bs += 4
    else:
        rs = 0
        gs = 0
        bs = 0
    print(r, g, b)
    return (r, g, b, (rs, gs, bs))




if __name__ == "__main__":
    main()