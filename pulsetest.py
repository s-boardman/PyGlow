##
##  PyGlow
##
##      python module to control Pimoronis PiGlow (http://shop.pimoroni.com/products/piglow)
##
##      * pulsetest.py - test the pulsing light feature
##

from pyglow import PyGlow

pyglow = PyGlow()

val = input("Maximum Brightness: ")
print("Pulsing 1 Light")
pyglow.pulse(1, val)
print("Pulsing Arms")
pyglow.pulse_arm(1, val)
pyglow.pulse_arm(2, val)
pyglow.pulse_arm(3, val)
print("Pulsing All")
pyglow.pulse_all(val)