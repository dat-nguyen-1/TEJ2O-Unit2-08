"""
Created by: Dat Nguyen
Created on: Feb 2026
This program uses an SR latch to control an RGB LED.
"""

from microbit import *

display.clear()
display.show(Image.HAPPY)

while True:
    pin15.write_digital(0)
    pin16.write_digital(0)
    if button_a.is_pressed() and button_b.is_pressed():
        display.show("A+B")
        pin15.write_digital(1)
        pin16.write_digital(1)
    elif button_a.is_pressed():
        display.show("A")
        pin15.write_digital(1)
    elif button_b.is_pressed():
        display.show("B")
        pin16.write_digital(1)
