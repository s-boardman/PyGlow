#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * test.py - set brightness for each color individually
#
#####


from PyGlow import PyGlow


pyglow = PyGlow()

val = input("White: ")
pyglow.color("white", int(val))

val = input("Blue: ")
pyglow.color("blue", int(val))

val = input("Green: ")
pyglow.color("green", int(val))

val = input("Yellow: ")
pyglow.color("yellow", int(val))

val = input("Orange: ")
pyglow.color("orange", int(val))

val = input("Red: ")
pyglow.color("red", int(val))

val = input("All: ")
pyglow.all(int(val))
