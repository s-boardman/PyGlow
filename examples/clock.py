#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * clock.py - binary clock by Jason (@Boeeerb) & Remi (rparpa)
# [https://github.com/Boeeerb/PiGlow]
#
#####


from PyGlow import PyGlow
from time import sleep
from datetime import datetime


pyglow = PyGlow()

##
# You can customise these settings:
##

# Show 12 or 24hr clock - 0= 24hr, 1= 12hr
show12hr = 0
# Set brightness of LED - 1-255
# (recommend 10-20, put 0 and you won't see it!)
led_brightness = 50
# Choose how to flash change of hour - 1= white leds, 2= all flash
hour_flash = 2

# arms
arm_top = {i: 0 for i in range(1, 7)}
arm_right = {i: 0 for i in range(7, 13)}
arm_bottom = {i: 0 for i in range(13, 19)}

# link arm to a time value
armConfig = {
    "1_seconds": arm_top,
    "2_minutes": arm_right,
    "3_hours": arm_bottom,
}

###
# End of customising
###

pyglow.all(0)

hour_count = 0
hour_current = 0


def assign_binary_value_to_arm(binary_value, arm):
    arm_led_numbers = [n for n in sorted(arm.iterkeys())]
    return {arm_led_numbers[key]: value for key, value in enumerate(reversed(list(binary_value)))}


def turn_on_off_led(hour, minute, second):
    bin_hour = "%06s" % bin(hour)[2:]
    bin_min = "%06s" % bin(minute)[2:]
    bin_sec = "%06s" % bin(second)[2:]

    armConfig["1_seconds"] = assign_binary_value_to_arm(bin_sec, armConfig["1_seconds"])
    armConfig["2_minutes"] = assign_binary_value_to_arm(bin_min, armConfig["2_minutes"])
    armConfig["3_hours"] = assign_binary_value_to_arm(bin_hour, armConfig["3_hours"])

    for key in sorted(armConfig.iterkeys()):
        for led_number in sorted(armConfig[key].iterkeys()):
            pyglow.led(led_number, led_brightness if armConfig[key][led_number] == "1" else 0)

while True:
    now = datetime.now()
    hour = now.hour

    if show12hr == 1 and now.hour > 12:
        hour -= 12

    # Check if current hour is different and set ready to flash hour
    if hour_current != hour:
        hour_count, hour_current = hour, hour

    turn_on_off_led(hour, now.minute, now.second)

    # Flash the white leds for the hour
    if hour_count != 0:
        sleep(0.5)
        if hour_flash == 1:
            pyglow.color("white", led_brightness)
        if hour_flash == 2:
            pyglow.all(led_brightness)
        sleep(0.5)
        hour_count -= 1
    else:
        sleep(0.1)
