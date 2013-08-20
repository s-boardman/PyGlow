##
##  PyGlow
##
##      python module to control Pimoronis PiGlow (http://shop.pimoroni.com/products/piglow)
##
##      for info & documentation see:    https://github.com/benleb/PYGlow
##

import re, sys
import RPi.GPIO as rpi
from smbus import SMBus

bus = 0

class PyGlow:

    def __init__(self):

        ## check if its an old v1 or v2 raspi
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2:
            i2c_bus = 1
        else:
            print "Unable to determine Raspberry Pi Hardware-Revision."
            sys.exit(1)

        ## enables the leds
        self.bus = SMBus(i2c_bus)
        self.bus.write_i2c_block_data(0x54, 0x00, [0x01])
        self.bus.write_byte_data(0x54, 0x13, 0xFF)
        self.bus.write_byte_data(0x54, 0x14, 0xFF)
        self.bus.write_byte_data(0x54, 0x15, 0xFF)


    def all(self, value):

        ## check if given brightness value is ok
        if 0 <= value <= 255:
            ## choose all leds
            leds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            self.set_leds(leds, value)
            self.update_leds()
        else:
            lights_off("usage: all([0-255])")


    def led(self, led, value):

        ## use set_leds & update_leds
        led = [led];
        self.set_leds(led, value)
        self.update_leds()


    def arm(self, arm, value):

        ## check if an existing arm is choosen & if brightness value is ok
        if arm == 1 and 0 <= value <= 255:
            leds = [1,2,3,4,5,6]
        elif arm == 2 and 0 <= value <= 255:
            leds = [7,8,9,10,11,12]
        elif arm == 3 and 0 <= value <= 255:
            leds = [13,14,15,16,17,18]
        else:
            self.lights_off("usage: arm([1-3],[0-255])")

        ## light up the choosen leds
        self.set_leds(leds, value)
        self.update_leds()


    def color(self, color, value):

        ## check if an available color is choosen & if brightness value is ok
        if (color == 1 or color == "white") and 0 <= value <= 255:
            leds = [6,12,18]
        elif (color == 2 or color == "blue") and 0 <= value <= 255:
            leds = [5,11,17]
        elif (color == 3 or color == "green") and 0 <= value <= 255:
            leds = [4,10,16]
        elif (color == 4 or color == "yellow") and 0 <= value <= 255:
            leds = [3,9,15]
        elif (color == 5 or color == "orange") and 0 <= value <= 255:
            leds = [2,8,14]
        elif (color == 6 or color == "red") and 0 <= value <= 255:
            leds = [1,7,13]
        else:
            self.lights_off("usage: color(<color>,[-0-255])")

        ## light up the choosen leds
        self.set_leds(leds, value)
        self.update_leds()


    def set_leds(self, leds, value):

        for led in leds:
            if isinstance(led, int) and 1 <= led <= 18 and 0 <= value <= 255:
                leds = [
                    "0x00", "0x07", "0x08", "0x09", "0x06", "0x05", "0x0A", "0x12", "0x11",
                    "0x10", "0x0E", "0x0C", "0x0B", "0x01", "0x02", "0x03", "0x04", "0x0F", "0x0D"]
            elif re.match('^[a-z]+[1-3]$', str(led)) and 0 <= value <= 255:
                leds = {"red1": "0x07", "orange1": "0x08", "yellow1": "0x09", "green1": "0x06", "blue1": "0x05", "white1": "0x0A",
                        "red2": "0x12", "orange2": "0x11", "yellow2": "0x10", "green2": "0x0E", "blue2": "0x0C", "white2": "0x0B",
                        "red3": "0x01", "orange3": "0x02", "yellow3": "0x03", "green3": "0x04", "blue3": "0x0F", "white3": "0x0D"}
            else:
                self.lights_off("usage: set_leds(leds, value) | leds has to be a list of [1-18] or <color>[1-18]")

            ## write update value to the ic
            self.bus.write_byte_data(0x54, int(leds[led], 16), value)


    def update_leds(self):
    
        ## tell the ic to update the leds
        self.bus.write_byte_data(0x54, 0x16, 0xFF)


    def lights_off(self, msg):

        ## exit function with shuts down the leds
        self.all(0)
        print msg
        sys.exit(1)
