## PyGlow

PyGlow is a small Python module for the PiGlow addon by Pimoroni, it will let you flex the LED muscles of this fantastic addon.
It was started as "PiGlow" by Jason (@Boeeerb https://github.com/Boeeerb/PiGlow) but i (@ben_leb) decided to fork it to provide a more clean and easier to use module.


## Features

 - Control a single LED, a single Arm, a single color or any combination of this
 - Gamma Correction


## Files

 - pyglow.py - Python module you'll import into your script
 - examples/test.py - You choose the brightness of each LED color group, to see how it will look
 - examples/clock.py - binary clock by Jason (@Boeeerb)
 - examples/cpu.py - shows your cpu usage on the PiGlow by Jason (@Boeeerb)
 - examples/set_leds.py - shows how set_leds() & update_leds() works


## Requirements

    sudo apt-get install python-smbus


## Functions

The functions of pyglow are:

```python
from pyglow import PyGlow
pyglow = PyGlow()

pyglow.all([0-255])                 # Control all LEDs together
pyglow.led(<color>[1-3],[0-255])    # Control an individual LED by color + arm-number eg. "red2"
pyglow.led([1-18],[0-255])          # Control an individual LED number
pyglow.color(<color>,[0-255])       # "white", "blue", "green", "yellow", "orange", "red"
pyglow.color([1-6],[0-255])         # 1=White, 2=Blue, 3=Green, 4=Yellow, 5=Orange, 6=Red
pyglow.arm([1-3],[0-255])           # Control an arm of LEDs by number
pyglow.set_leds(<led list>,[0-255]  # this function allows you to control a individual set of leds
                                    # first argument has to be a list of leds [1-18] or <color>[1-18]
pyglow.update_leds()                # updates the leds according to values set with set_leds
```
the set_leds() & update_leds() function allows you to control a individual set of leds & work as follow (theres also an set_leds.py in example/)
```python
## first set of leds with brightness 50
leds = [1,3,5,11,13,15]
pyglow.set_leds(leds,50)
## second set with brightness 150
leds = [2,4,9]
pyglow.set_leds(leds,150)
## and now this lights up the leds
pyglow.update_leds()
```

All colors are from 0 (off) to 255 (super duper eye numbing bright!)



## Installation instructions


### Preparation

For instruction hot to setup your Raspberry Pi to use with PyGlow, please see
https://github.com/pimoroni/piglow#setting-up-your-raspberry-pi


### Downloading the PyGlow module and testing

Now create a directory for it to live in then change to that directory:

    mkdir pyglow
    cd pyglow

Next get the latest version of PyGlow python module:

    wget https://raw.github.com/benleb/PyGlow/master/pyglow.py

This will give you a file called pyglow.py, this is the module and will do all the hardwork.

Now download the test script to make sure it works

    wget https://raw.github.com/benleb/PyGlow/master/examples/test.py

And run it by typing and setting a number between 0 (off) and 255 (brightest)

    sudo python test.py

If it works successfully you can choose the level of brightness for each color.

### Use it on your own

In the examples/ dir are some files to show you how to use PyGlow.
