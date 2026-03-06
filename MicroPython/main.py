"""
Created by: Dat Nguyen
Created on: Mar 2026
This module will cycle an RGB LED through its primary and secondary colours with a 1 second delay.
"""

import time
from microbit import *

# Initialize display
display.clear()
display.show(Image.HAPPY)

# Assign pins as constants
RED_PIN = pin14
GREEN_PIN = pin15
BLUE_PIN = pin16

# Initialize pins to OFF
RED_PIN.write_digital(0)
GREEN_PIN.write_digital(0)
BLUE_PIN.write_digital(0)

while True:
    if button_a.is_pressed():
        # Red
        RED_PIN.write_digital(1)
        display.show("Red")
        time.sleep(1)
        RED_PIN.write_digital(0)

        # Green
        GREEN_PIN.write_digital(1)
        display.show("Green")
        time.sleep(1)
        GREEN_PIN.write_digital(0)

        # Blue
        BLUE_PIN.write_digital(1)
        display.show("Blue")
        time.sleep(1)
        BLUE_PIN.write_digital(0)

        # Magenta (Red + Blue)
        RED_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("Magenta")
        time.sleep(1)
        RED_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # Cyan (Green + Blue)
        GREEN_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("Cyan")
        time.sleep(1)
        GREEN_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # Yellow (Red + Green)
        RED_PIN.write_digital(1)
        GREEN_PIN.write_digital(1)
        display.show("Yellow")
        time.sleep(1)
        RED_PIN.write_digital(0)
        GREEN_PIN.write_digital(0)

        # White (Red + Green + Blue)
        RED_PIN.write_digital(1)
        GREEN_PIN.write_digital(1)
        BLUE_PIN.write_digital(1)
        display.show("White")
        time.sleep(1)
        RED_PIN.write_digital(0)
        GREEN_PIN.write_digital(0)
        BLUE_PIN.write_digital(0)

        # Display happy face
        display.show(Image.HAPPY)
