#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
# import line_follow.py

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Initilize our motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
front_motor_1 = Motor(Port.C)

# Initialize the color sensor.
right_sensor = ColorSensor(Port.S4)

ARM_MOTOR_SPEED = 400
WHEEL_DIAMETER = 92
AXLE_TRACK = 130
DRIVE_SPEED_NORMAL = 200
DRIVE_SPEED_SLOW = 100
DRIVE_EXTRA_SLOW = 30
CIRCUMFERENCE = 3.14 * WHEEL_DIAMETER # Diameter = 100mm, Circumference = 314.10mm = 1 rotation

# All parameters are in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)

# Set the straight speed to 100 and turn speed to 100
robot.settings(straight_speed=DRIVE_SPEED_NORMAL, turn_rate=30)   

# Move forward to Step Counter
robot.straight(700)
# Slow down and start slowly pushing forward
robot.stop()
robot.settings(straight_speed=DRIVE_EXTRA_SLOW, turn_rate=30)

# Fix later: Meant to be seconds
i=0
for i in range(0,28):
    robot.straight(10)
    sleep(0.4)
    i = i + 1

robot.stop()
robot.settings(straight_speed=20, turn_rate=20)
robot.straight(-50)
robot.turn(-90)
'''
steering_drive.on_for_seconds(0,SpeedPercent(1.5), 17.5)

# Rotate one wheel to turn back into the wall
steering_A.on_for_seconds(0,SpeedPercent(-20), 3)

# Go forward for few seconds and then turn right
steering_drive.on_for_seconds(0, SpeedPercent(20), 0.5)
steering_A.on_for_rotations(0,SpeedPercent(20), 0.37)

# Go straight till you reach the treadmill
steering_drive.on_for_rotations(0,SpeedPercent(20), 0.735)
steering_drive.on_for_rotations(0,SpeedPercent(20), 2.54)

# Rotate the front wheel attachment (large motor C)
motor_C.on_for_rotations(0,SpeedPercent(100), 13)

# Move back to the Pull up bar by going in reverse on steering drive
steering_drive.on_for_rotations(0,SpeedPercent(-50), 2.3)

# Rotate left by turning wheel motor D
steering_D.on_for_degrees(0,SpeedPercent(50), 140)

# Go straight to go thrugh pull up bar
steering_drive.on_for_degrees(0,SpeedPercent(30), 513)

# Go reverse to come out of the pull up bar
steering_drive.on_for_degrees(0,SpeedPercent(-30), 560)

# Turn back towards base using motor D
steering_D.on_for_degrees(0, SpeedPercent(50), -140)

# Final run to head back to base
steering_drive.on_for_degrees(0,SpeedPercent(50), 1286)
'''