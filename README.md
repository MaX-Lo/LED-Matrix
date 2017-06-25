# LED - Matrix

This repo hosts Code to run our LED Matrix. If you don't know this you will probably not need this code at the moment. In future updates a detailed documentation will be added to make it useable for everyone. Hope it doesn't take too long. : )

#### Short video:
[![Example video showing time](https://img.youtube.com/vi/AUEFyxiVq1U/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
# What you need?
- LED Matrix with rgb LED's that are individual adressable (TODO more details about that)
- Raspberry PI to control LED's color
    - Apache Webserver running on the pi (remote control for the matrix over a website)
    - Adafruit ws2801 library (makes communication with the LED's a lot easier)
    - python 2.7.x (ws2801 library doesn't run on 3.x yet)

TODO: add detailed description of requirement

# Patterns
| Filename | Description |
| -------- | ----------- |
| clock.py | shows the current time in 24:00 format with background displaying seconds
| testing_effects.py | rapidly changing pattern for guarenteed eye cancer
| timer.py | wow, who would expect that - a timer

# Classes
## Matrix
Main object thats needed to change the state of the LED's. Remember to call `matrix.show()` for updating the matrix after setting pixels. Uses internal the adafruit ws2801 library.
`Matrix()`
| Matrix.set(x, y, color) | *set a specified pixel in the given color. Top-Left is 0, 0* |
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
TODO: Update, number needs a different structure and shouldn't be a part of the Matrix class

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
