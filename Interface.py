from smbus import SMBus
from time import sleep
import RPi.GPIO as rpi
import re
import Tkinter
from PyGlow import PyGlow

pyglow = PyGlow()

"""
The PyGlow() object can accept four optional parameters:

brightness=None - sets default brightness level (value: number from 0 and 255)
speed=None - sets default pulsing speed in milliseconds (value: number > 0)
pulse=None - enables pulsing by default (value: True or False)
pulse_dir=None - sets default pulsation direction (value: UP, DOWN, BOTH)
"""

#
