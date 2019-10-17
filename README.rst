
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-lsm303dlh-mag/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/lsm303dlh-mag/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag
    :alt: Build Status

Adafruit CircuitPython module for the LSM303DLH's 3-axis magnetometer

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    import time
    import board
    import busio
    import adafruit_lsm303dlh_mag

    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

    while True:
        mag_x, mag_y, mag_z = sensor.magnetic

        print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))
        print('')
        time.sleep(1.0)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
