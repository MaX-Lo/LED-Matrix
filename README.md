# LED - Matrix

This repo hosts Code to run the best LED Matrix in the world. If you don't know us you will probably not need this code. Sorry, but we will add a detailed documentation later in order to make it useable for everyone. Hope it doesn't take too long. : )

# What you need?
- LED Matrix with rgb LED's that are individual adressable
- Raspberry PI to control LED's color
    - Apache Webserver running on the pi (remote control for the matrix over a website)
    - Adafruit ws2801 library (makes communication with the LED's a lot easier)
    - python 2.7.x (ws2801 library doesn't run on 3.x yet)

TODO: add detailed description of requirement

# Coding stuff
## About how things are done
Steps to start a pattern, game, ... on the matrix:
1) Choose a pattern in the web interface
2) After clicking on it any running pattern gets stoped and the corresponding python script for the new pattern gets executed.
3) *Magic*
