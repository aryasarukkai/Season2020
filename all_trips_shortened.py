#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

import config
import drive_utils
# This program requires LEGO EV3 MicroPython v2.0 or higher.

def init_brick():
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

# Create your brick object and initialize
ev3 = EV3Brick()
# init_brick()

# Select or skip this trip
ev3.speaker.beep()
ev3.screen.print("TRIP 1")

# Wait till left button is pressed; then if left button pressed run trip, right button skip to next trip
i=0
while ( (Button.CENTER not in ev3.buttons.pressed()) and (Button.RIGHT not in ev3.buttons.pressed()) ): 
    i = i + 1

if (Button.CENTER in ev3.buttons.pressed()):
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
        sleep(0.1)
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
    # HCK Increase back up frpm -45 to -55
    robot.straight(-55)

    # Go straight a little bit
    # HCK 1: Too far in, reduce by .8 cm // was 138 --> 130 --> 125
    # DEBUG REMOVED robot.straight(125)
    
    # HCK 2 Drive till white black
    drive_utils.drive_till_white(robot, left_sensor)
    # Go forward 35 mm
    robot.stop()
    robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
    # HCK Incressed from 35 to 40 after combined runs --> 36
    robot.straight(36)
    robot.stop()

    # Rotate Right
    robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
    robot.turn(90)
    robot.stop()

    # Go straight to get closer to the treadmill
    robot.settings(straight_speed=DRIVE_SPEED_NORMAL, turn_rate=30)
    robot.straight(560)
    robot.stop()

    # ORIGINAL WORKING CODE
    # Look for black followed by white to position the tire exactly on the treadmill
    robot.settings(straight_speed=50, turn_rate=30)
    drive_utils.drive_till_white(robot, left_sensor)
    # Tweaking to get to exact position HCK1 Added 10 --> 20 --> 15
    robot.straight(15)
    robot.stop()
    # END OF ORIGINAL CODE


    # rotate motor 2 to go down to rowing machine
   front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED_FAST, 120, then=Stop.HOLD, wait=False)

    # Rotate the tire to move the tradmill
    front_motor_1.run_angle(5* config.ARM_MOTOR_SPEED, -5300, then=Stop.HOLD, wait=True)
    
    # keep pushing down while going back
    front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED, 30, then=Stop.HOLD, wait=False)

    # Pull back rowing machine by going back straight in reverse
    # HCK 2: Lowered distance to not pull too much // 180 --> 160
    robot.straight(-160)

'''
    # Turn left to pull into small circle
    robot.turn(-60)
    front_motor_2.run_angle(config.ARM_MOTOR_SPEED, 30, then=Stop.HOLD, wait=True)
    robot.turn(60)
    front_motor_2.run_angle(config.ARM_MOTOR_SPEED_FAST, -150, then=Stop.HOLD, wait=True)
'''

    robot.stop()

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

# Create and initialize brick before every trip
ev3 = EV3Brick()
# init_brick()

# Select or skip this trip
ev3.speaker.beep()
ev3.screen.print("TRIP 2")

# Wait till left button is pressed; then if left button pressed run trip, right button skip to next trip
i=0
while ( (Button.CENTER not in ev3.buttons.pressed()) and (Button.RIGHT not in ev3.buttons.pressed()) ): 
    i = i + 1

if (Button.CENTER in ev3.buttons.pressed()):
    # Go forward 600mm 
    robot.straight(750)

    # Drive forward till we sense white followed by black
    drive_utils.drive_till_black(robot, left_sensor)
            
    # Turn left
    drive_utils.gyro_turn(robot, gyro, -37)

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
    drive_utils.gyro_turn(robot, gyro, -103)

    # Bring the Tire arm down
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -240, then=Stop.HOLD, wait=True)

    #Bring slide arm down
    front_motor_2.run_angle(config.ARM_MOTOR_SPEED, 205, then=Stop.HOLD, wait=True)

    #Go straight to the slide
    robot.straight(210)

    #slide the people off the slide
    front_motor_2.run_angle(config.ARM_MOTOR_SPEED_SUPER_FAST, -120, then=Stop.HOLD, wait=True)

    robot.stop()

    # Set the straight speed and turn rate
    robot.settings(straight_speed=config.DRIVE_SPEED_SUPER_FAST, turn_rate=config.TURN_RATE)

    # Turn left to go back to base
    robot.turn(19)

    #Go straight to base
    robot.straight(200)

    # Turn left to go back to base
    robot.turn(-17)

    #Go straight to base
    robot.straight(1000)

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# TRIP 3 CODE  ##################

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create and initialize brick before every trip
ev3 = EV3Brick()
# init_brick()

# Select or skip this trip
ev3.speaker.beep()
ev3.screen.print("TRIP 3")

# Wait till left button is pressed; then if left button pressed run trip, right button skip to next trip
i=0
while ( (Button.CENTER not in ev3.buttons.pressed()) and (Button.RIGHT not in ev3.buttons.pressed()) ): 
    i = i + 1
if (Button.CENTER in ev3.buttons.pressed()):
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

# TRIP 4 CODE TRIMMED ########################
# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create and initialize brick before every trip
ev3 = EV3Brick()
# init_brick()

# Select or skip this trip
ev3.speaker.beep()
ev3.screen.print("TRIP 4")

# Wait till left button is pressed; then if left button pressed run trip, right button skip to next trip
i=0
while ( (Button.CENTER not in ev3.buttons.pressed()) and (Button.RIGHT not in ev3.buttons.pressed()) ): 
    i = i + 1

if (Button.CENTER in ev3.buttons.pressed()):
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
    # OLD WORKING PROGRAM DELETED front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -15, then=Stop.HOLD, wait=True)
    # DBG NEW GO UP LESSER 120 --> 90
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED_FAST, 90, then=Stop.HOLD, wait=True)
    front_motor_1.stop()

    # Go straight to the bench mission
    robot.straight(430)
    robot.stop()
    robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

    # Turn left and then right to topple bench
    robot.turn(-35)
    robot.straight(-30)
    robot.turn(25)

    # Back out a bit and then go forward to goto bar
    # DBG Original robot.straight(-30)
    robot.straight(110)

    # Turn to align with bar and then pull elevator up to dislodge bar then turn left to be back to parallel path
    robot.turn(15)
    front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 200, then=Stop.HOLD, wait=True)
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -200, then=Stop.HOLD, wait=True)

    # Doing it one more time to ensure that the 
    front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 250, then=Stop.HOLD, wait=True)
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -250, then=Stop.HOLD, wait=True)
    robot.turn(-15)

    # pull up motor 1 and turn right and Drop blocks
    '''
    front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 20, then=Stop.HOLD, wait=True)
    robot.turn(30)
    robot.straight(-30)
    front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, 2000, then=Stop.HOLD, wait=True)  
    robot.turn(-30)
    front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, -2000, then=Stop.HOLD, wait=True)  
    '''

    # Backup, lower elevator, go further back
    # DEBUG REMOVED robot.straight(-10)
    # HCK - reduced lowering from -100 to -70 
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -70, then=Stop.HOLD, wait=True)
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
    # Final step, turn more with added weight of cube drop -15 --> -25
    robot.turn(-25)
    # HCK Adding more forward distance as it stopped working 90 --> 110 --> 120 --> 130
    robot.straight(130)

    # Drop blocks into basket
    front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, 1900, then=Stop.HOLD, wait=True)  
    front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, -1900, then=Stop.HOLD, wait=True)

    # Now pull up basketball basket to middle and lower down
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 1000, then=Stop.HOLD, wait=True)
    front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -300, then=Stop.HOLD, wait=True)

    # Goto to robot dance area and dance
    # HCK turn increased based on run - from -75 --> -85 --> -70 --> -85 after blocks weight
    robot.turn(-85)
    robot.straight(-320)
    i=0
    for i in range(0,20):
        robot.turn(-15)
        robot.turn(15)
        ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'], tempo=278)
        i=i+1

    robot.stop()

    # End of trip: Stop Robot and all motors
    robot.stop()
    front_motor_1.stop()
    front_motor_2.stop()

# END OF ALL TRIPS
ev3.speaker.say("BYE")
ev3.screen.print("BYE")
