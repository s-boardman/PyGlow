PyGlow
======

PyGlow is a small Python module for the PiGlow addon by Pimoroni which will let
you flex the LED muscles of this fantastic addon. It was started as
[PiGlow](https://github.com/Boeeerb/PiGlow) by Jason (@Boeeerb) but I
(@ben_leb) decided to fork it to provide a more clean and easier to use module.


Features
========

- Control a single LED, a single arm, a single color or any combination of this
- Pulsing LED
- Gamma Correction (makes the progression from `0-255` more visually linear)


Installation instructions
=========================

Preparation
-----------

For instruction hot to setup Raspberry Pi to use with PyGlow, please see
https://github.com/pimoroni/piglow#setting-up-your-raspberry-pi


Requirements
------------

PyGlow module requires the `smbus` Python module. It must be installed before
the PyGlow modules is used. Example of installation for
[RASPBIAN](http://raspbian.org/):

```
sudo apt-get install python-smbus
```


Downloading and testing the PyGlow module
-----------------------------------------

Now create a directory for python modules and then change to that directory:

```
$ mkdir -p ~/lib/python/
$ cd ~/lib/python/
```

Next get the latest version of PyGlow python module:

```
git clone https://github.com/benleb/PyGlow.git
```

This will download the PyGlow module into the `~/lib/python/PyGlow` directory.

In order to make the PyGlow module accessible for other scripts, a system
environment variable  with a path to the module must be exported (you can add
it into your `~/.bashrc`):

```
export PYTHONPATH="$PYTHONPATH:~/lib/python"
```

Now go to the `examples` directory and run the testing script:

```
cd ~/lib/python/PyGlow/examples/
python test.py
```

If the script loads, you can set the brightness of each LED color group by
typing a number between `0` (off) and `255` (brightest).

See the other files in the `examples` directory for more examples how to us
PyGlow.


Functions
=========

In order to be able to use PyGlow module, the `PyGlow()` class must be
imported:

```
from PyGlow import PyGlow
```

Then it's possible to instantiate the `PyGlow()` object:

```
pyglow = PyGlow()
```

The `PyGlow()` object can accept two optional parameters:

- `brightness=None` - sets default brightness level (value from `0` and `255`)
- `speed=None` - sets default pulsing speed in milliseconds

The default value is used across all function unless overridden on the function
level. If the default value is not set during the object instantiation, it must
be set on the function level.

Functions provided by the `PyGlow()` object are:


### `led(led, brightness=None)`

Sets the specific `led` to the `brightness` level. The `led` is in the range of
`1` to `18`. The `brightness` value is in the range of `0` to `255`.


### `color(color, brightness=None)`

Sets the specific `color` group to the `brightness` level. The `color` group
can be either a number or a name:

- `1` = `white`
- `2` = `blue`
- `3` = `green`
- `4` = `yellow`
- `5` = `orange`
- `6` = `red`

The `brightness` value is in the range of `0` to `255`.


### `arm(arm, brightness=None)`

Sets the specific LED `arm` to the `brightness` level. The `arm` value can be
either `1`, `2` or `3`. The `brightness` value is in the range of `0` to `255`.


### `all(brightness=None)`

Sets all LEDs to the `brightness` level. The `brightness` value is in the range
of `0` to `255`.


### `pulse(led, brightness=None, speed=None)`

Pulses with a specific `led` to the `brightness` level with the `speed`. The
`led` value is in the range of `1` to `18`. The `brightness` value is in the
range of `0` to `255`. The `speed` value is in milliseconds.


### `pulse_color(color, brightness=None, speed=None)`

Pulses with a specific `color` group to the `brightness` level with the
`speed`. The `color` group value can be be either a number or a name:

- `1` = `white`
- `2` = `blue`
- `3` = `green`
- `4` = `yellow`
- `5` = `orange`
- `6` = `red`

The `brightness` value is in the range of `0` to `255`. The `speed` value is in
milliseconds.


### `pulse_arm(arm, brightness=None, speed=None)`

Pulses with a specific `arm` to the `brightness` level with the specified
`speed`. The `led` value is in the range of `1` to `18`. The `brightness` value
is in the range of `0` to `255`. The `speed` value is in milliseconds.


### `pulse_all(brightness=None, speed=None)`

Pulses with all LEDs to the `brightness` level with the `speed`. The `led`
value is in the range of `1` to `18`. The `brightness` value is in the range of
`0` to `255`. The `speed` value is in milliseconds.


### `set_leds(leds, brightness=None)`

Sets a list of `leds` to the `brightness` level. The `leds` list can be
composed of numbers from `1` to `18`. The `brightness` value is in the range of
`0` to `255`. The set `brightness` will take effect only after the
`update_leds()` is called (see bellow).


### `update_leds()`

Sets the brightness level to all LEDs specified by the `set_leds()` function.

```
leds = [1, 3, 5, 11, 13, 15]
pyglow.set_leds(leds, 50)
pyglow.update_leds()
```


Files
=====

- `pyglow.py` - Python module providing the PyGlow class
- `examples/bin_clock.py` - binary clock by Jiri Tyr
- `examples/clock.py` - binary clock by Jason (@Boeeerb)
- `examples/cpu.py` - CPU percentage indicator by Jason (@Boeeerb)
- `examples/pulsetest.py` - shows how to use LED pulsing
- `examples/set_leds.py` - shows how `set_leds()` and `update_leds()` works
- `examples/test.py` - allows to choose the brightness of each LED color group


Contributing
============

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


License
=======

This module is release under the MIT license.
