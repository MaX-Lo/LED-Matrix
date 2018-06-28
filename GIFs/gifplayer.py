from PIL import Image
import time

import sys

from matrix import Matrix

'''
modified
source: https://gist.github.com/BigglesZX/4016539
'''


class GIFPlayer:
    def __init__(self, matrix, file_path):
        self.matrix = matrix
        self.fps = 1
        self.mode = self.analyse_image(file_path)['mode']
        self.file_path = file_path
        self.img = Image.open(file_path)
        self.current_frame_num = 0
        self.color_palette = self.img.getpalette()
        self.last_frame = self.img.convert('RGBA')

    def set_fps(self, fps):
        self.fps = fps*1.0

    def play(self):
        try:

            while True:
                '''
                If the GIF uses local colour tables, each frame will have its own palette.
                If not, we need to apply the global palette to the new frame.
                '''
                if not self.img.getpalette():
                    self.img.putpalette(self.color_palette)

                new_frame = Image.new('RGBA', self.img.size)

                '''
                Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
                If so, we need to construct the new frame by pasting it on top of the preceding frames.
                '''
                if self.mode == 'partial':
                    new_frame.paste(self.last_frame)

                new_frame.paste(self.img, (0, 0), self.img.convert('RGBA'))

                self.matrix.clear()
                for x in range(self.matrix.WIDTH):
                    for y in range(self.matrix.HEIGHT):
                        r, g, b, _ = new_frame.getpixel((x, y))
                        self.matrix.set(x, y, (r, g, b))
                self.matrix.show()

                self.current_frame_num += 1
                self.last_frame = new_frame
                self.img.seek(self.img.tell() + 1)

                time.sleep(1/self.fps)
        except EOFError:
            self.reset()
            self.matrix.clear()
            self.matrix.show()

    def reset(self):
        self.current_frame_num = 0
        self.img = Image.open(self.file_path)
        self.current_frame_num = 0
        self.color_palette = self.img.getpalette()
        self.last_frame = self.img.convert('RGBA')

    @staticmethod
    def analyse_image(path):
        """
        Pre-process pass over the image to determine the mode (full or additive).
        Necessary as assessing single frames isn't reliable. Need to know the mode
        before processing all frames.
        """
        im = Image.open(path)
        results = {
            'size': im.size,
            'mode': 'full',
        }
        try:
            while True:
                if im.tile:
                    tile = im.tile[0]
                    update_region = tile[1]
                    update_region_dimensions = update_region[2:]
                    if update_region_dimensions != im.size:
                        results['mode'] = 'partial'
                        break
                im.seek(im.tell() + 1)
        except EOFError:
            pass
        return results


def main():
    """
    executing gifplayer.py with a gif file as parameter shows
    that image
    
    params: gif_file, fps, repetitions
    """
    path = sys.argv[1]
    if len(sys.argv) < 3:
        fps = 1
    else:
        fps = int(sys.argv[2])

    if len(sys.argv) < 4:
        repetitions = 1
    else:
        repetitions = int(sys.argv[3])

    gifplayer = GIFPlayer(Matrix(), path)
    gifplayer.set_fps(fps)
    for i in range(repetitions):
        gifplayer.play()

if __name__ == '__main__':
    main()
