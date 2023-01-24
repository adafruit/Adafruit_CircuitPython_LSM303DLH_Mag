
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-lsm303dlh-mag/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/lsm303dlh-mag/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Adafruit CircuitPython module for the LSM303DLH's 3-axis magnetometer

Note that this is specifically intended for the LSM303DLHC, as opposed to the
LSM303DLH proper, which has the magnetic Y and Z orientations swapped.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-lsm303dlh_mag/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-lsm303dlh_mag

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-lsm303dlh_mag

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install adafruit-circuitpython-lsm303dlh_mag

Usage Example
=============

.. code-block:: python3

    import time
    import board
    import adafruit_lsm303dlh_mag

    i2c = board.I2C()  # uses board.SCL and board.SDA
    sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

    while True:
        mag_x, mag_y, mag_z = sensor.magnetic

        print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))
        print('')
        time.sleep(1.0)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/lsm303dlh-mag/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
