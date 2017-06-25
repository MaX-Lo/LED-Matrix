from PIL import Image

from matrix import Matrix


def main():
    matrix = Matrix()
    image = Image.open('smiley.gif')
    rgb_im = image.convert('RGB')

    matrix.clear()
    for x in range(matrix.WIDTH):
        for y in range(matrix.HEIGHT):
            matrix.set(x, y, rgb_im.getpixel((x, y)))
    matrix.show()

if __name__ == '__main__':
    main()