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

# TRIP 2 CODE  ###################

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

# Initialize the color sensor.
left_sensor = ColorSensor(Port.S4)
right_sensor = ColorSensor(Port.S1)

# Initialize the Gyro sensor
gyro = GyroSensor(Port.S2)
gyro.reset_angle(0)

# All parameters are in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter=config.WHEEL_DIAMETER, axle_track=config.AXLE_TRACK)

# Set the straight speed and turn rate
robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=config.TURN_RATE)

# Go forward 600mm 
robot.straight(750)

# Drive forward till we sense white followed by black
drive_utils.drive_till_black(robot, left_sensor)
        
# Turn left
drive_utils.gyro_turn(robot, gyro, -38)

# Go forward to the tire
robot.straight(265)

# Turn the arm up to flip the tire
front_motor_1.run_angle(config.ARM_MOTOR_SPEED_FAST, 320, then=Stop.HOLD, wait=True)

# Go backwards 
robot.straight(-100)

# Turn left to go under the bridge
drive_utils.gyro_turn(robot, gyro, -46)

# Go back and align with the wall before going forward.
robot.straight(-200)

# Bring the arm down so that it doesn't crash in the bridge
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -150, then=Stop.HOLD, wait=True)

# Go under the bridge
robot.straight(500)

# Turn the arm up to not interfere
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 320, then=Stop.HOLD, wait=True)

# Go under the bridge and align with black line beyond the bridge
drive_utils.drive_till_black(robot, right_sensor)

# Go forward a bit more
robot.straight(150)

# Turn left towards the swing
drive_utils.gyro_turn(robot, gyro, -105)

# Bring the Tire arm down
front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -240, then=Stop.HOLD, wait=True)

#Bring slide arm down
front_motor_2.run_angle(config.ARM_MOTOR_SPEED, 210, then=Stop.HOLD, wait=True)

#Go straight to the slide
robot.straight(210)

#slide the people off the slide
front_motor_2.run_angle(config.ARM_MOTOR_SPEED_FAST, -120, then=Stop.HOLD, wait=True)



