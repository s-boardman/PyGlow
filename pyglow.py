#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# For more information and documentation see:
# https://github.com/benleb/PYGlow
#
#####
#
# Author:
#
# Ben Lebherz (@ben_leb)
#
# Contributors:
#
# Austin Parker (@austinlparker)
#  - pulse features
# Jon@Pimoroni
#  - gamma correction mapping
# Jiri Tyr
#  - PEP8 code compliance
#  - code refactoring and documentation
#  - fixing pulsing function
#  - adding pulse_color function
#
#####


# Import some modules
import re
import RPi.GPIO as rpi
from smbus import SMBus
from time import sleep


# Define GPIO addresses
I2C_ADDR = 0x54
EN_OUTPUT_ADDR = 0x00
EN_ARM1_ADDR = 0x13
EN_ARM2_ADDR = 0x14
EN_ARM3_ADDR = 0x15
UPD_PWM_ADDR = 0x16

# Define global variables
LED_LIST = range(1, 19)
LED_HEX_LIST = [
    "0x07", "0x08", "0x09", "0x06", "0x05", "0x0A",
    "0x12", "0x11", "0x10", "0x0E", "0x0C", "0x0B",
    "0x01", "0x02", "0x03", "0x04", "0x0F", "0x0D"]
ARM_LIST = range(1, 4)
ARM_LED_LIST = [range(1, 7), range(7, 13), range(13, 19)]
COLOR_LIST = range(1, 7)
COLOR_NAME_LIST = ["white", "blue", "green", "yellow", "orange", "red"]
COLOR_LED_LIST = [
    [6, 12, 18], [5, 11, 17], [4, 10, 16], [3, 9, 15], [2, 8, 14], [1, 7, 13]]
GAMMA_TABLE = [
    0, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 5, 5, 5, 5, 5,
    5, 5, 5, 6, 6, 6, 6, 6,
    6, 6, 7, 7, 7, 7, 7, 7,
    8, 8, 8, 8, 8, 8, 9, 9,
    9, 9, 10, 10, 10, 10, 10, 11,
    11, 11, 11, 12, 12, 12, 13, 13,
    13, 13, 14, 14, 14, 15, 15, 15,
    16, 16, 16, 17, 17, 18, 18, 18,
    19, 19, 20, 20, 20, 21, 21, 22,
    22, 23, 23, 24, 24, 25, 26, 26,
    27, 27, 28, 29, 29, 30, 31, 31,
    32, 33, 33, 34, 35, 36, 36, 37,
    38, 39, 40, 41, 42, 42, 43, 44,
    45, 46, 47, 48, 50, 51, 52, 53,
    54, 55, 57, 58, 59, 60, 62, 63,
    64, 66, 67, 69, 70, 72, 74, 75,
    77, 79, 80, 82, 84, 86, 88, 90,
    91, 94, 96, 98, 100, 102, 104, 107,
    109, 111, 114, 116, 119, 122, 124, 127,
    130, 133, 136, 139, 142, 145, 148, 151,
    155, 158, 161, 165, 169, 172, 176, 180,
    184, 188, 192, 196, 201, 205, 210, 214,
    219, 224, 229, 234, 239, 244, 250, 255]


class PyGlow:
    def __init__(self, brightness=None, speed=None):
        # Check what Raspberry Pi version we got
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2:
            i2c_bus = 1
        else:
            raise PyGlowException(
                self, "Unable to determine Raspberry Pi Hardware-Revision.")

        # Enables the LEDs
        self.bus = SMBus(i2c_bus)

        # Tell the SN3218 to enable output
        self.update_leds(I2C_ADDR, EN_OUTPUT_ADDR, 0x01)

        # Enable each LED arm
        self.update_leds(I2C_ADDR, EN_ARM1_ADDR, 0xFF)
        self.update_leds(I2C_ADDR, EN_ARM2_ADDR, 0xFF)
        self.update_leds(I2C_ADDR, EN_ARM3_ADDR, 0xFF)

        # Set default brightness and speed
        self.brightness = brightness
        self.speed = speed

    def led(self, led, brightness=None):
        if brightness is None:
            brightness = self.brightness

        # Use set_leds and update_leds
        self.set_leds([led], brightness)
        self.update_leds()

    def color(self, color, brightness=None):
        if brightness is None:
            brightness = self.brightness

        # Check if an available color is choosen and if brightness value is OK
        if color in COLOR_LIST and 0 <= brightness <= 255:
                leds = COLOR_LED_LIST[color - 1]
        elif color in COLOR_NAME_LIST and 0 <= brightness <= 255:
                leds = COLOR_LED_LIST[COLOR_NAME_LIST.index(color)]
        else:
            raise PyGlowException(
                self, "usage: color(color=[<name>|[1-6]], brightness=[0-255])")

        # Light up the choosen LEDs
        self.set_leds(leds, brightness)
        self.update_leds()

    def arm(self, arm, brightness=None):
        if brightness is None:
            brightness = self.brightness

        # Check if an existing arm is choosen and if brightness value is OK
        if arm in ARM_LIST and 0 <= brightness <= 255:
            leds = LED_LIST[arm - 1]
        else:
            raise PyGlowException(
                self, "usage: arm(arm=[1-3], brightness=[0-255])")

        # Light up the choosen LEDs
        self.set_leds(leds, brightness)
        self.update_leds()

    def all(self, brightness=None):
        if brightness is None:
            brightness = self.brightness

        # Check if given brightness value is OK
        if 0 <= brightness <= 255:
            # Choose all LEDs
            self.set_leds(LED_LIST, brightness)
            self.update_leds()
        else:
            raise PyGlowException(self, "usage: all(brightness=[0-255])")

    def __pulse_loop(self, led, brightness=None, speed=None, direction=-1):
        if brightness is None:
            brightness = self.brightness
        if speed is None:
            speed = self.speed

        # Number of steps of the loop
        steps = int(float(speed) / float(brightness) + 0.5)

        # The initial brightness value
        b_val = 0
        if direction == -1:
            self.__pulse_loop(led, brightness, speed, 1)
            b_val = brightness

        # The brightness value with which we should finish the loop
        b_val_final = b_val

        # Step up the brightness
        for n in range(1, steps + 1):
            # Calculate new brightness value
            b_val += int(float(brightness) / float(steps) + 0.5) * direction

            # Round the final brightness value to the desired value
            if n == steps:
                b_val = brightness - b_val_final

            # Set the brightness
            self.set_leds(led, b_val)
            self.update_leds()

            # Sleep for certain period
            # (here we should divide by 1000.0 but that was too slow/fast
            # so I have increased it to 1500.0)
            sleep(float(speed) / float(steps) / 1500.0 / 2.0)

    def pulse(self, led, brightness=None, speed=None):
        if brightness is None:
            brightness = self.brightness
        if speed is None:
            speed = self.speed

        self.__pulse_loop([led], brightness, speed)

    def pulse_color(self, color, brightness=None, speed=None):
        if brightness is None:
            brightness = self.brightness
        if speed is None:
            speed = self.speed

        if color in COLOR_LIST and 0 <= brightness <= 255:
            leds = COLOR_LED_LIST[color - 1]
        elif color in COLOR_NAME_LIST and 0 <= brightness <= 255:
            leds = COLOR_LED_LIST[COLOR_NAME_LIST.index(color)]
        else:
            raise PyGlowException(
                self, "usage: pulse_color(color=[<name>|[1-6]], "
                "brightness=[0-255], speed=<int>)")

        self.__pulse_loop(leds, brightness, speed)

    def pulse_arm(self, arm, brightness=None, speed=None):
        if brightness is None:
            brightness = self.brightness
        if speed is None:
            speed = self.speed

        if arm in ARM_LIST and 0 <= brightness <= 255:
            leds = LED_LIST[arm - 1]
        else:
            raise PyGlowException(
                self,
                "usage: pulse_arm(arm=[1-3], brightness=[0-255], speed=<int>)")

        self.__pulse_loop(leds, brightness, speed)

    def pulse_all(self, brightness=None, speed=None):
        if brightness is None:
            brightness = self.brightness
        if speed is None:
            speed = self.speed

        if 0 <= brightness <= 255:
            leds = range(1, 19)
            self.__pulse_loop(leds, brightness, speed)
        else:
            raise PyGlowException(
                self, "usage: pulse_all(brightness=[0-255], speed=<int>)")

    def set_leds(self, leds, brightness=None):
        if brightness is None:
            brightness = self.brightness

        # Pick the gamma-corrected value
        gc_value = GAMMA_TABLE[brightness]

        for led in leds:
            m = re.match('^([a-z]+)([1-3])$', str(led))

            if m and 0 <= brightness <= 255:
                color = m.group(1)
                arm = int(m.group(2))
                color_index = COLOR_NAME_LIST.index(color)

                led = LED_HEX_LIST[6 * (arm - 1) + 5 - color_index]
            elif (
                    isinstance(led, int) and
                    1 <= led <= 18 and
                    0 <= brightness <= 255):

                led = LED_HEX_LIST[led - 1]
            else:
                raise PyGlowException(
                    self,
                    "usage: set_leds([[1-18]|<color_name><color_number>], "
                    "brightness=[0-255])")

            # Write update value to the IC
            self.update_leds(I2C_ADDR, int(led, 16), gc_value)

    def update_leds(
            self,
            i2c_addr=I2C_ADDR, upd_pwm_addr=UPD_PWM_ADDR, brightness=0xFF):

        # Tell the IC to update the LEDs
        self.bus.write_byte_data(i2c_addr, upd_pwm_addr, brightness)


class PyGlowException(Exception):
    def __init__(self, parent, msg):
        # Switch all LEDs off
        parent.all(0)

        self.msg = msg

    def __str__(self):
        return self.msg
