PyGlow
======

PyGlow is a small Python module for the PiGlow addon by [Pimoroni](http://www.pimoroni.com/) which will let
you flex the LED muscles of this fantastic addon. It was started as
[PiGlow](https://github.com/Boeeerb/PiGlow) by Jason ([@Boeeerb](https://twitter.com/Boeeerb)) and has been forked by
([@ben_leb](https://twitter.com/ben_leb)) to provide a more clean and easier to use module.

I ([@s_boardman](https://twitter.com/s_boardman)) aim to create a web interface to set the colour and brightness via a browser rather than programmatically.

Features (from PyGlow by [@ben_leb](https://twitter.com/ben_leb))
========

- Control a single LED, a single arm, a single color or any combination of these
- Pulsing LED
- Gamma Correction (makes the progression from `0-255` more visually linear)


Installation instructions
=========================

Preparation
-----------

For instructions on how to setup Raspberry Pi for use with PyGlow, please see
https://github.com/pimoroni/piglow#setting-up-your-raspberry-pi


Requirements
------------

PyGlow module requires the `smbus` Python module. It must be installed before
the PyGlow module is used. Example of installation for
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
git clone https://github.com/s-boardman/PyGlow.git
```

This will download the PyGlow module into the `~/lib/python/PyGlow` directory.

In order to make the PyGlow module accessible for other scripts, a system
environment variable  with a path to the module must be exported (you can add
it into your `~/.bashrc`):

```
export PYTHONPATH=$PYTHONPATH:~/lib/python
```

Now go to the `examples` directory and run the testing script:

```
cd ~/lib/python/PyGlow/examples/
python test.py
```

If the script loads, you can set the brightness of each LED color group by
typing a number between `0` (off) and `255` (brightest).

See the other files in the [`examples`](https://github.com/s-boardman/PyGlow/tree/master/examples) directory for more examples 
of how to use PyGlow.


Install using pip
-----------------

If you just want to install the PyGlow library for use in your own project,
you can also install it using pip

```
$ pip install git+https://github.com/s-boardman/PyGlow.git
```

The PyGlow.py files will be downloaded and placed in the site-packages directory
ready for use.


Usage
=====

Instantiation
-------------

In order to be able to use PyGlow module, the `PyGlow()` class must be
imported:

```
from PyGlow import PyGlow
```

Then it's possible to instantiate the `PyGlow()` object:

```
pyglow = PyGlow()
```

The `PyGlow()` object can accept four optional parameters:

- `brightness=None` - sets default brightness level (value: number from `0` and
  `255`)
- `speed=None` - sets default pulsing speed in milliseconds (value: number > 0)
- `pulse=None` - enables pulsing by default (value: `True` or `False`)
- `pulse_dir=None` - sets default pulsation direction (value: `UP`, `DOWN`,
   `BOTH`)

The default parameter values are used across all functions unless overridden on
the function level. If the default parameter value is not set during the object
instantiation, it must be set on the function level. The value for the parameter
`speed` and `pulse_dir` must be set only if the parameter `pulse=True`.


Functions
---------

Functions provided by the `PyGlow()` object are:


### `led(led, brightness=None, speed=None, pulse=None, pulse_dir=None)`

Sets the specific `led` to the `brightness` level. The `led` is in the range of
`1` to `18`. The `led` parameter can also be a list of individual leds. The
other parameters can have the same value like in the case of the object
instantiation.


### `color(color, brightness=None, speed=None, pulse=None, pulse_dir=None)`

Sets the specific `color` group to the `brightness` level. The `color` group
can be either a number or a name:

- `1` = `white`
- `2` = `blue`
- `3` = `green`
- `4` = `yellow`
- `5` = `orange`
- `6` = `red`

The other parameters can have the same value like in the case of the object
instantiation.


### `arm(arm, brightness=None, speed=None, pulse=None, pulse_dir=None)`

Sets the specific LED `arm` to the `brightness` level. The `arm` value can be
either `1`, `2` or `3`. The other parameters can have the same value like in
the case of the object instantiation.


### `all(brightness=None, speed=None, pulse=None, pulse_dir=None)`

Sets all LEDs to the `brightness` level. The parameters can have the same value
like in the case of the object instantiation.


### `set_leds(leds, brightness=None, speed=None, pulse=None, pulse_dir=None)`

Prepares the list of `leds` to be set to the `brightness` level. The `leds`
list can be composed of numbers from `1` to `18` or connection of `color` name
and `arm` number (e.g. `red1` will light up the `red` LED in the arm `1`). The
other parameters can have the same value like in the case of the object
instantiation. The set `brightness` will take effect only after the
`update_leds()` is called (see bellow).


### `update_leds()`

Sets the brightness level of all LEDs specified by the `set_leds()` function.

```
leds_odd = [1, 3, 5, 7, 9, 11, 13, 15, 17]
leds_even = [2, 4, 6, 8, 10, 12, 14, 16, 18]
pyglow.set_leds(leds_odd, 150)
pyglow.set_leds(leds_even, 10)
pyglow.update_leds()
```


Files
=====

- `pyglow.py` - Python module providing the PyGlow class by Ben [@ben_leb](https://twitter.com/ben_leb)
- `examples/bin_clock.py` - binary clock by Jiri Tyr
- `examples/clock.py` - binary clock by Jason ([@Boeeerb](https://twitter.com/Boeeerb))
- `examples/cpu.py` - CPU percentage indicator by Jason ([@Boeeerb](https://twitter.com/Boeeerb))
- `examples/pulsetest.py` - shows how to use LED pulsing by Ben [@ben_leb](https://twitter.com/ben_leb)
- `examples/set_leds.py` - shows how `set_leds()` and `update_leds()` works by [@ben_leb](https://twitter.com/ben_leb)
- `examples/test.py` - allows to choose the brightness of each LED color group by Ben [@ben_leb](https://twitter.com/ben_leb)


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
