/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Dat Nguyen
 * Created on: Mar 2026
 * This program will change the colour of an RGB LED.
*/

// Initialize display.
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Initialize pins.
pins.digitalWritePin(DigitalPin.P14, 0) // Red.
pins.digitalWritePin(DigitalPin.P15, 0) // Green.
pins.digitalWritePin(DigitalPin.P16, 0 )// Blue.

input.onButtonPressed(Button.A, function() {
    // Turn LED red.
    pins.digitalWritePin(DigitalPin.P14, 1)
    basic.showString("Red")

    // Wait 1 second.
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P14, 0)

    // Turn LED green for 1 second.
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("Green")
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P15, 0)

    // Turn LED blue for 1 second.
    pins.digitalWritePin(DigitalPin.P16, 1)
    basic.showString("Blue")
    basic.pause(1000)

    // Turn LEDs off.
    pins.digitalWritePin(DigitalPin.P16, 0)

    // Turn LED magenta for 1 second.
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P16, 1)
    basic.showString("Magenta")
    basic.pause(1000)

    // Turn LEDs off.
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P16, 0)

    // Turn LED cyan for 1 second.
    pins.digitalWritePin(DigitalPin.P15, 1)
    pins.digitalWritePin(DigitalPin.P16, 1)
    basic.showString("Cyan")
    basic.pause(1000)

    // Turn LEDs off.
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P16, 0)

    // Turn LED yellow for 1 second.
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("Yellow")
    basic.pause(1000)

    // Turn LEDs off.
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)

    // Turn LED white for 1 second.
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P15, 1)
    pins.digitalWritePin(DigitalPin.P16, 1)
    basic.showString("White")
    basic.pause(1000)

    // Turn LEDs off.
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P16, 0)

    // Display happy face.
    basic.showIcon(IconNames.Happy)
})
