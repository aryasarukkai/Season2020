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
# Set the straight speed and turn rate
robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

# First adjust the elevator, Go down to touch floor, then go back up to give enough distance to ground
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -15, then=Stop.HOLD, wait=True)
front_motor_1.run_angle(config.ARM_MOTOR_SPEED_FAST, 120, then=Stop.HOLD, wait=True)
front_motor_1.stop()


# Go straight to the bench mission
robot.straight(430)
robot.stop()
robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

# Turn left and then right to topple bench
robot.turn(-35)
robot.turn(25)

# Back out a bit and then go forward to goto bar
robot.straight(-30)
robot.straight(110)

# Turn to align with bar and then pull elevator up to dislodge bar then turn left to be back to parallel path
robot.turn(15)
front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 200, then=Stop.HOLD, wait=True)
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -200, then=Stop.HOLD, wait=True)

# Doing it one more time to ensure that the 
front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 250, then=Stop.HOLD, wait=True)
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -250, then=Stop.HOLD, wait=True)
robot.turn(-15)

# Backup, lower elevator, go further back
robot.straight(-10)
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -100, then=Stop.HOLD, wait=True)
robot.straight(-200)
robot.stop()

# Turn right and then goto the basketball mission
robot.settings(straight_speed=config.DRIVE_SPEED_FAST, turn_rate=30)
robot.turn(60)
robot.straight(160)
robot.turn(20)
robot.straight(300)
robot.turn(-90)
robot.straight(250)
robot.turn(-15)
robot.straight(35)

# Now pull up basketball basket to middle
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 1000, then=Stop.HOLD, wait=True)

# Goto to robot dance area and dance
robot.turn(-75)
robot.straight(-320)
i=0
for i in range(0,20):
    robot.turn(-15)
    robot.turn(15)
    i=i+1

robot.stop()



# front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 550, then=Stop.HOLD, wait=True)
# front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -250, then=Stop.HOLD, wait=True)