# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Read data from the magnetometer and print it out, ASAP!"""

import board

import adafruit_lsm303dlh_mag

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

while True:
    mag_x, mag_y, mag_z = sensor.magnetic
    print(f"{mag_x:10.3f} {mag_y:10.3f} {mag_z:10.3f}")
