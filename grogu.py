import config
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

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