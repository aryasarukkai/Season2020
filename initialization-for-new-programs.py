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

sub init_brick():
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

    # Speeds
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
    # Initialize the Gyro sensor
    gyro = GyroSensor(Port.S2)
    gyro.reset_angle(0)

    # All parameters are in millimeters
    robot = DriveBase(left_motor, right_motor, wheel_diameter=config.WHEEL_DIAMETER, axle_track=config.AXLE_TRACK)

    # Set the straight speed and turn rate
    robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=config.TURN_RATE)

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Initialize Brick
init_brick()
