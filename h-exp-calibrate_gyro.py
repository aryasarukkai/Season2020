#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create a data log file in the project folder on the EV3 Brick.
# * By default, the file name contains the current date and time, for example:
#   log_2020_02_13_10_07_44_431260.csv
# * You can optionally specify the titles of your data columns. For example,
#   if you want to record the motor angles at a given time, you could do:
data = DataLog('time', 'sensor_value', name='log', timestamp=False, extension='csv', append=False)


# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize the gyro sensor. It is used to provide feedback for balancing the
# robot.
gyro_sensor = GyroSensor(Port.S2)

# The following (UPPERCASE names) are constants that control how the program
# behaves.
GYRO_CALIBRATION_LOOP_COUNT = 200
GYRO_OFFSET_FACTOR = 0.0005

# Calibrate the gyro offset. This makes sure that the robot is perfectly
# still by making sure that the measured rate does not fluctuate more than
# 2 deg/s. Gyro drift can cause the rate to be non-zero even when the robot
# is not moving, so we save that value for use later.
while True:
    gyro_minimum_rate, gyro_maximum_rate = 440, -440
    gyro_sum = 0
    for _ in range(GYRO_CALIBRATION_LOOP_COUNT):
        gyro_sensor_value = gyro_sensor.speed()
        gyro_sum += gyro_sensor_value
        if gyro_sensor_value > gyro_maximum_rate:
            gyro_maximum_rate = gyro_sensor_value
        if gyro_sensor_value < gyro_minimum_rate:
            gyro_minimum_rate = gyro_sensor_value
        wait(5)
    if gyro_maximum_rate - gyro_minimum_rate < 2:
        break
gyro_offset = gyro_sum / GYRO_CALIBRATION_LOOP_COUNT