#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import config
import drive_utils

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Initilize our motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
front_motor_1 = Motor(Port.C)

left_motor.reset_angle(0)
right_motor.reset_angle(0)
front_motor_1.reset_angle(0)

# Initialize the color sensor.
right_sensor = ColorSensor(Port.S1)

# Initialize the Gyro sensor
gyro = GyroSensor(Port.S2)
gyro.reset_angle(0)

# All parameters are in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter=config.WHEEL_DIAMETER, axle_track=config.AXLE_TRACK)

# Set the straight speed and turn rate
robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=config.TURN_RATE)

# Go forward 600mm 
robot.straight(600)

# Drive forward till we sense white followed by black
drive_utils.drive_till_black(robot, right_sensor)
        
# Turn left
drive_utils.gyro_turn(robot, gyro, -23)

# Go forward
robot.straight(270)

# Turn the arm up to flip the tire
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 320, then=Stop.HOLD, wait=True)

# Go backwards
robot.straight(-100)

# Turn left
drive_utils.gyro_turn(robot, gyro, -35)

# Turn the arm down
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -320, then=Stop.HOLD, wait=True)

# Go under the bridge
robot.straight(300)

# Turn the arm up to not interfere
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 320, then=Stop.HOLD, wait=True)

# Go under the bridge
robot.straight(240)

# Turn left
drive_utils.gyro_turn(robot, gyro, -85)





