##
##  PyGlow
##
##      python module to control Pimoronis PyGlow (http://shop.pimoroni.com/products/pyglow)
##
##      * clock.py - binary clock by Jason (@Boeeerb https://github.com/Boeeerb/PyGlow)
##      ! requires psutil - sudo apt-get install python-psutil
##


from pyglow import PyGlow
from time import sleep
import psutil

pyglow = PyGlow()

while True:

    cpu = psutil.cpu_percent()
    pyglow.all(0)

    if cpu < 5:
        pyglow.color("white", 20)
    elif cpu < 20:
        pyglow.color("white", 20)
        pyglow.color("blue", 20)
    elif cpu < 40:
        pyglow.color("white", 20)
        pyglow.color("blue", 20)
        pyglow.color("green", 20)
    elif cpu < 60:
        pyglow.color("white", 20)
        pyglow.color("blue", 20)
        pyglow.color("green", 20)
        pyglow.color("yellow", 20)
    elif cpu < 80:
        pyglow.color("white", 20)
        pyglow.color("blue", 20)
        pyglow.color("green", 20)
        pyglow.color("yellow", 20)
        pyglow.color("orange", 20)
    else:
        pyglow.all(20)
    sleep(0.2)
