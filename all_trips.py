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

# TRIP 1 CODE ####################

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Select or skip this trip
ev3.speaker.say("TRIP ONE")
ev3.screen.print("TRIP 1")

if Button.LEFT in ev3.buttons.pressed(): 
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
    robot.straight(138)
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

    # Come back home
    robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=30)
    robot.straight(-1880)

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# TRIP 2 CODE ########################

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Select or skip this trip
ev3.speaker.say("TRIP TWO")
ev3.screen.print("TRIP 2")

if Button.LEFT in ev3.buttons.pressed(): 
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

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# TRIP 3 CODE  ##################

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Select or skip this trip
ev3.speaker.say("TRIP THREE")
ev3.screen.print("TRIP 3")

if Button.LEFT in ev3.buttons.pressed(): 
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
    robot.settings(straight_speed=config.DRIVE_SPEED_FAST, turn_rate=config.TURN_RATE)

    robot.straight(700)
    robot.straight(-700)

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# TRIP 4 CODE ########################
# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Select or skip this trip
ev3.speaker.say("TRIP FOUR")
ev3.screen.print("TRIP 4")

if Button.LEFT in ev3.buttons.pressed(): 
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
        ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'])
        i=i+1

    robot.stop()

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# END OF ALL TRIPS
ev3.speaker.say("BYE")
ev3.screen.print("BYE")
