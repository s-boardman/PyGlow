#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * pulsetest.py - test the pulsing light feature
#
#####


from PyGlow import PyGlow


pyglow = PyGlow()

val = input("Maximum Brightness: ")
speedval = input("Speed (Try 500 as a default): ")

pyglow.all(0)

print("Pulsing 1 Light")
pyglow.pulse(1, val, speedval)

print("Pulsing Arms")
pyglow.pulse_arm(1, val, speedval)
pyglow.pulse_arm(2, val, speedval)
pyglow.pulse_arm(3, val, speedval)

print("Pulsing All")
pyglow.pulse_all(val, speedval)
