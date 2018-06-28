from gifplayer import GIFPlayer
from matrix import Matrix

 
def main():
    gif_player = GIFPlayer(Matrix(), '/home/pi/Matrix/GIFs/ship.gif')
    gif_player.set_fps(2)
    gif_player.play()

if __name__ == '__main__':
    main()
