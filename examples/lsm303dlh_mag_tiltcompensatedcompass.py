# SPDX-FileCopyrightText: 2021 Alex Dew
# SPDX-License-Identifier: MIT
# Tilt Compensated Compass using Accelerometer and Magnetometer

# The equations below are the ones used in code
# Equations from st manual:
# "Computing tilt measurement and tilt-compensated eCompass" by Andrea Vitali
# https://www.st.com/resource/en/design_tip/dm00269987-computing-tilt-measurement-and-tiltcompensated-ecompass-stmicroelectronics.pdf

# for Phi (Roll)
# Phi = atan2(Gy, Gz)
# for stability, 'Gz' can be substituted with Gz+Gx*alpha (alpha=0.01-0.05)

# for Theta (Pitch)
# Gz2 = Gy * Sin( Phi ) + Gz * Cos( Phi )
# Theta = Atan(-Gx / Gz2)

# for Psi or "Yaw" (The Tilt Compensated Heading)
# Bx,By,Bz are magnetometer readings

# By2 = Bz * Sin( Phi ) – By * Cos( Phi )
# Bz2 = By * Sin( Phi ) + Bz * Cos( Phi )
# Bx3 = Bx * Cos( Theta ) + Bz2 * Sin( Theta )
# Psi = Atan2(By2 , Bx3) # This is the Yaw (Tilt Compensated Heading)
###############################################

import board
import re
import time
from math import atan, atan2, degrees, cos, sin
import adafruit_lsm303_accel
import adafruit_lis2mdl
import adafruit_lsm303dlh_mag

# Mag and Accel offsets from calibration. You need to calibrate your own offset
offmag = (-10.8, 4.875, -54.225)
offaccel = (-0.994392, -0.305969, 0.382458)


i2c = board.I2C()  # uses board.SCL and board.SDA
sensoraccel = adafruit_lsm303_accel.LSM303_Accel(i2c)
sensormag = adafruit_lis2mdl.LIS2MDL(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


while True:
    Xm, Ym, Zm = sensormag.magnetic
    Xm = Xm - offmag[0]
    Ym = Ym - offmag[1]
    Zm = Zm - offmag[2]
    ax, ay, az = sensoraccel.acceleration
    ax = ax - offaccel[0]
    ay = ay - offaccel[1]
    az = az - offaccel[2]

    # tilt compensation equations
    stableZ = az + (ax * 0.01)
    phi = atan2(ay, stableZ)

    Gz2 = ay * sin(phi) + az * cos(phi)
    theta = atan(-ax / Gz2)

    By2 = Zm * sin(phi) - Ym * cos(phi)
    Bz2 = Ym * sin(phi) + Zm * cos(phi)
    Bx3 = Xm * cos(theta) + Bz2 * sin(theta)

    Psi = vector_2_degrees(Bx3, By2)

    print("Yaw Heading: ", "{:.0f}".format(Psi))

    # Offset declination for your general location
    # -5 degrees declination in FL ## find yours @ magnetic-declination.com
    withdecl = Psi - 5
    if withdecl < 0:
        withdecl += 360
    print("Yaw with Declination: ", "{:.0f}".format(withdecl))

    time.sleep(0.5)
