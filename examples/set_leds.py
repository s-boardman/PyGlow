##
##  PyGlow
##
##      python module to control Pimoronis PyGlow (http://shop.pimoroni.com/products/pyglow)
##
##      * set_leds.py - how to control a individual set of leds by Ben (@ben_leb)
##

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()

try:

    while True:

        ## choose a set of leds
        leds = [1,3,5,11,13,15]
        ## save them with the brightness you want
        pyglow.set_leds(leds,50)
        ## wait to demonstrate...
        sleep(3)
        ## light up the leds!
        pyglow.update_leds()

        sleep(3)

        ## now we want to shut down the first set
        pyglow.set_leds(leds,0)
        ## ...build a newer, brighter set
        leds = [2,4,9]
        pyglow.set_leds(leds,150)
        ## and update the leds!
        pyglow.update_leds()

except KeyboardInterrupt:

    pyglow.all(0)
