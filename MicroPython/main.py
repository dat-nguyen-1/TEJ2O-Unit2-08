"""
Created by: Dat Nguyen
Created on: Mar 2026
This module will cycle an RGB LED through its primary and secondary colours with a 1 second delay.
"""

from microbit import *
import time

# initialize display
display.clear()
display.show(Image.HAPPY)

# define hardware pins as constants
RED_PIN = pin14
GREEN_PIN = pin15
BLUE_PIN = pin16

# initialize pins to OFF
RED_PIN.write_digital(0)
GREEN_PIN.write_digital(0)
BLUE_PIN.write_digital(0)

# main loop
while True:
    # handle button a press
    if button_a.is_pressed():
        # Red
        RED_PIN.write_digital(1)
        display.show("Red")
        time.sleep(1)
        RED_PIN.write_digital(0)

        # green
        GREEN_PIN.write_digital(1)
        display.show("Green")
        time.sleep(1)
        GREEN_PIN.write_digital(0)

        # blue
        BLUE_PIN.write_digital(1)
        display.show("Blue")
        time.sleep(1)
        BLUE_PIN.write_digital(0)

        # magenta (red + blue)
        RED_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("Magenta")
        time.sleep(1)
        RED_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # cyan (green + blue)
        GREEN_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("Cyan")
        time.sleep(1)
        GREEN_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # yellow (red + green)
        RED_PIN.write_digital(1)
        GREEN_PIN.write_digital(1)
        display.show("Yellow")
        time.sleep(1)
        RED_PIN.write_digital(0)
        GREEN_PIN.write_digital(0)

        # white (red + green + blue)
        RED_PIN.write_digital(1)
        GREEN_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("White")
        time.sleep(1)
        RED_PIN.write_digital(0)
        GREEN_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # display happy face
        display.show(Image.HAPPY)
        
