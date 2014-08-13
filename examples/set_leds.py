#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * set_leds.py - how to control a individual set of leds by Ben (@ben_leb)
#
#####


from PyGlow import PyGlow
from time import sleep


pyglow = PyGlow()

try:
    while True:
        # Choose a set of leds
        leds = [1, 3, 5, 11, 13, 15]
        # Save them with the brightness you want
        pyglow.set_leds(leds, 50)
        # Wait to demonstrate...
        sleep(3)
        # Light up the leds!
        pyglow.update_leds()

        sleep(3)

        # Now we want to shut down the first set
        pyglow.set_leds(leds, 0)
        # ...build a newer, brighter set
        leds = [2, 4, 9]
        pyglow.set_leds(leds, 150)
        # and update the leds!
        pyglow.update_leds()

except KeyboardInterrupt:
    pyglow.all(0)
