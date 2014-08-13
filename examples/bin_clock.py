#!/usr/bin/env python2

#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * bin_clock.py - binary clock by Jiri Tyr
#
#####


from datetime import datetime
from PyGlow import PyGlow, ARM_LED_LIST
from sys import stdout
from time import sleep


def int2bin(num):
    return int('{0:b}'.format(num))


def print_time():
    now = datetime.now()
    cur_time = [now.hour, now.minute, now.second]

    bin_time = tuple(list(map(int2bin, cur_time)) + cur_time)

    stdout.write(' %0.5d | %0.6d | %0.6d (%0.2d:%0.2d:%0.2d)\r' % bin_time)
    stdout.flush()

    for arm_index, arm_bin in enumerate(bin_time[0:3]):
        for led_index, c in enumerate("%0.6d" % arm_bin):
            if c == '1':
                pg.led(ARM_LED_LIST[arm_index][led_index])
            else:
                pg.led(ARM_LED_LIST[arm_index][led_index], 0)


def main():
    print(' %5s | %6s | %6s' % ('Hour', 'Minute', 'Second'))

    global pg
    pg = PyGlow(brightness=50)

    try:
        while True:
            print_time()
            sleep(0.5)
    except KeyboardInterrupt:
        print ''
        pg.all(0)


if __name__ == '__main__':
    main()
