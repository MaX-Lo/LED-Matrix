# LED - Matrix

This repo hosts Code to run my LED Matrix. Right now this documentation may lack some details to fully understand the project. Should you feel the urge to build a LED Matrix yourself and have questions or you want to skip the foolish beginner faults I did, feel free to contact me. :)

#### Short video:
[![Example video showing time](https://img.youtube.com/vi/AUEFyxiVq1U/0.jpg)](https://youtu.be/AUEFyxiVq1U)
# What you will need
- LED Matrix with rgb LED's that are individualy addressable (I took a LED stripe with LED's each controlled by a ws2801)
- Raspberry PI to control LED's color
    - Apache Webserver running on the pi (allows remote controling the matrix over a website)
    - Adafruit ws2801 library (communication with the LED's gets a lot easier with it)
    - python 2.7.x (ws2801 library doesn't run on Python3 yet)

# Patterns
| Filename | Description |
| -------- | ----------- |
| clock.py | shows the current time in 24:00 format with background displaying seconds
| testing_effects.py | rapidly changing pattern for guarenteed eye cancer
| timer.py | a simple timer

# Classes
## Matrix
Main object thats needed to change the state of the LED's. Remember to call `matrix.show()` for updating the matrix after setting pixels. Uses internal the adafruit ws2801 library.

| Matrix.set(x, y, color) | set a specified pixel in the given color. Top-Left is 0, 0 |
| -------- | ----------- |
| x | x coordinate of the pixel |
| y | y coordinate of the pixel |
| color | r,g,b tupel containing the desired color |

| Matrix.get(x, y) | *get a  given pixels color. Top-Left is 0, 0* |
| - | - |
| x | x coordinate of the pixel |
| y | y coordinate of the pixel |

| Matrix.clear() | sets all pixel black (0, 0, 0) |
| - | - |

| Matrix.show() | "push" changes to the LED's |
| - | - |

## Number
| Number() |
| - |
TODO: Update: in future, number needs a different structure and shouldn't be a part of the Matrix class

## GIFPlayer
A simple way to display gif images with multiple frames on the LED Matrix. You can either create an instance of a GIFPlayer and use that or for simply playing a certaing gif file:
```sh
$ python gifplayer.py your_filename.gif fps repetitions
```
#### Example:
Shows the content of the file *smiley.gif* with 3 frames per second and that 5 times.
```sh
$ python gifplayer.py smiley.gif 3 5
```
#### Methods
| GIFPlayer(matrix, file_path) |   |
| -------- | ----------- |
| matrix | the matrix object to draw on |
| file_path | relative or absolute path to the .gif file |

| GIFPlayer.set_fps(fps) | set speed for changing frames  |
| -------- | ----------- |
| fps | frames per second, default = 1 |

| GIFPlayer.play() | start playing the file |
| -------- | - |
