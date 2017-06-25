# LED - Matrix

This repo hosts Code to run the best LED Matrix in the world. If you don't know us you will probably not need this code. Sorry, but we will add a detailed documentation later in order to make it useable for everyone. Hope it doesn't take too long. : )

# What you need?
- LED Matrix with rgb LED's that are individual adressable
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

# Coding stuff
## About how things are done
Steps to start a pattern, game, ... on the matrix:
1) Choose a pattern in the web interface
2) After clicking on it any running pattern gets stoped and the corresponding python script for the new pattern gets executed.
3) *Magic*

# Classes
### Matrix
Main object thats needed to change the state of the LED's. Remember to call *matrix.show()* for updating the matrix after setting pixels. Uses internal the adafruit ws2801 library.
| Matrix() | 
| -------- |

| set(x, y, color) | *set a specified pixel in the given color. Top-Left is 0, 0* |
| -------- | ----------- |
| x | x coordinate of the pixel |
| y | y coordinate of the pixel |
| color | r,g,b tupel containing the desired color |

| get(x, y) | *get a  given pixels color. Top-Left is 0, 0* |
| - | - |
| x | x coordinate of the pixel |
| y | y coordinate of the pixel |

| clear() | sets all pixel black (0, 0, 0) |
| - | - |

| show() | "push" changes to the LED's |
| - | - |

### Number
| Number() |
| - |
TODO: Update, number needs a different structure and shouldn't be a part of the Matrix class

### GIFPlayer
A simple way to display gif images witch multiple frames on the LED Matrix. 

| GIFPlayer(matrix, file_path) |   |
| -------- | ----------- |
| matrix | the matrix object to draw on |
| file_path | relative or absolute path to the .gif file |

| set_fps(fps) |   |
| -------- | ----------- |
| fps | integer setting the frames per second, default = 1 |

| play() | 
| -------- |
| start playing the file |
