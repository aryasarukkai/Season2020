#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
import config
import drive_utils

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

# Initialize the color sensors and motors.
right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S4)
ARM_MOTOR_SPEED = 400
WHEEL_DIAMETER = 92
AXLE_TRACK = 130
DRIVE_SPEED_FAST = 350
DRIVE_SPEED_NORMAL = 200
DRIVE_SPEED_SLOW = 100
DRIVE_EXTRA_SLOW = 30
CIRCUMFERENCE = 3.14 * WHEEL_DIAMETER # Diameter = 100mm, Circumference = 314.10mm = 1 rotation

# All parameters are in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
# Set the straight speed and turn rate
robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 50, then=Stop.HOLD, wait=False)
front_motor_1.stop()


robot.straight(430)
robot.turn(-35)
robot.turn(25)

robot.straight(120)
robot.straight(-110)


# front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 550, then=Stop.HOLD, wait=True)
# front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -250, then=Stop.HOLD, wait=True)
