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
front_motor_2 = Motor(Port.B)

left_motor.reset_angle(0)
right_motor.reset_angle(0)
front_motor_1.reset_angle(0)
front_motor_2.reset_angle(0)

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

# Move forward to Step Counter
robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=30)   
robot.straight(800)
# Slow down and start slowly pushing forward
robot.stop()
robot.settings(straight_speed=DRIVE_EXTRA_SLOW, turn_rate=30)

# Do Step Counter (Small Steps so it doesn't get stuck)
i=0
for i in range(0,20):
    robot.straight(10)
    sleep(0.4)
    i = i + 1
robot.stop()

# Backup a little
robot.straight(-50)
robot.stop()

# Rotate left to align with wall
robot.settings(straight_speed=100, turn_rate=30)
robot.turn(-135)
robot.stop()

# Back up to wall
robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
robot.straight(-45)

# Go straight a little bit
# HCK Adjusted distance to adjust lower 1/3/21 from 138 to 134 to 130 to 128
robot.straight(128)
robot.stop()

# Rotate Right
robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
robot.turn(90)
robot.stop()

# Go straight to get closer to the treadmill
robot.settings(straight_speed=DRIVE_SPEED_NORMAL, turn_rate=30)
robot.straight(560)
robot.stop()

# Look for black followed by white to position the tire exactly on the treadmill
robot.settings(straight_speed=50, turn_rate=30)
drive_utils.drive_till_white(robot, left_sensor)

# Tweaking to get to exact position HCK1
robot.straight(10)
robot.stop()

# Rotate the tire to move the tradmill
# front_motor_1.run_time(speed=config.ARM_MOTOR_SPEED, time=500, then=Stop.HOLD, wait=False)
front_motor_1.run_angle(5* config.ARM_MOTOR_SPEED, -5000, then=Stop.HOLD, wait=True)

front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED_FAST, 120, then=Stop.HOLD, wait=True)
# keep pushing down while going back
front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED, 30, then=Stop.HOLD, wait=False)

# Pull back rowing machine
robot.straight(-180)

# Turn left to pull into small circle
robot.turn(-60)
front_motor_2.run_angle(config.ARM_MOTOR_SPEED_FAST, -80, then=Stop.HOLD, wait=True)
robot.turn(60)
robot.stop()

# Come back home
robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=30)
robot.straight(-1880)

# End of trip: Stop Robot
robot.stop()


