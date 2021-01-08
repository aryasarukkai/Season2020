import config
import grogu
import drive_utils
from time import sleep
def run_trip():
    # Initilize our motors
    left_motor = grogu.Motor(grogu.Port.A)
    right_motor = grogu.Motor(grogu.Port.D)
    front_motor_1 = grogu.Motor(grogu.Port.C)

    # Initialize the color sensors and motors.
    right_sensor = grogu.ColorSensor(grogu.Port.S1)
    left_sensor = grogu.ColorSensor(grogu.Port.S4)
    ARM_MOTOR_SPEED = 400
    WHEEL_DIAMETER = 92
    AXLE_TRACK = 130
    DRIVE_SPEED_FAST = 350
    DRIVE_SPEED_NORMAL = 200
    DRIVE_SPEED_SLOW = 100
    DRIVE_EXTRA_SLOW = 30
    CIRCUMFERENCE = 3.14 * WHEEL_DIAMETER # Diameter = 100mm, Circumference = 314.10mm = 1 rotation

    # All parameters are in millimeters
    grogu.robot = grogu.DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)

    # Move forward to Step Counter
    grogu.robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=30)   
    grogu.robot.straight(800)
    # Slow down and start slowly pushing forward
    grogu.robot.stop()
    # was DRIVE_SPEED_EXTRA_SLOW --> DRIVE_SLOW
    grogu.robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)

    # Do Step Counter (Small Steps so it doesn't get stuck)
    i=0
    for i in range(0,20):
        grogu.robot.straight(10)
        sleep(0.1)
        i = i + 1
    grogu.robot.stop()

    # Backup a little
    grogu.robot.straight(-50)
    grogu.robot.stop()

    # Rotate left to align with wall
    grogu.robot.settings(straight_speed=100, turn_rate=30)
    grogu.robot.turn(-135)
    grogu.robot.stop()

    # Back up to wall
    grogu.robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
    # HCK Increase back up frpm -45 to -55 --> -50 after combined program 1/6
    grogu.robot.straight(-60)

    # Go straight a little bit
    # HCK 1: Too far in, reduce by .8 cm // was 138 --> 130 --> 125
    # DEBUG REMOVED robot.straight(125)
    
    # HCK 2 Drive till white black
    drive_utils.drive_till_white(grogu.robot, left_sensor)
    # Go forward 35 mm
    grogu.robot.stop()
    grogu.robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
    # HCK Incressed from 35 to 40 after combined runs --> 36
    grogu.robot.straight(36)
    grogu.robot.stop()

    # Rotate Right
    grogu.robot.settings(straight_speed=DRIVE_SPEED_SLOW, turn_rate=30)
    grogu.robot.turn(90)
    # drive_utils.gyro_turn(grogu.robot, grogu.gyro, 88)
    grogu.robot.stop()

    # Go straight to get closer to the treadmill
    grogu.robot.settings(straight_speed=DRIVE_SPEED_NORMAL, turn_rate=30)
    grogu.robot.straight(560)
    grogu.robot.stop()

    # ORIGINAL WORKING CODE
    # Look for black followed by white to position the tire exactly on the treadmill
    grogu.robot.settings(straight_speed=50, turn_rate=30)
    drive_utils.drive_till_white(grogu.robot, left_sensor)
    # Tweaking to get to exact position HCK1 Added 10 --> 20 --> 15 --> after unified program 13
    grogu.robot.straight(13)
    grogu.robot.stop()
    # END OF ORIGINAL CODE


    # rotate motor 2 to go down to rowing machine
    grogu.front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED_FAST, 120, then=grogu.Stop.HOLD, wait=False)

    # Rotate the tire to move the tradmill
    grogu.front_motor_1.run_angle(10* config.ARM_MOTOR_SPEED, -5300, then=grogu.Stop.HOLD, wait=True)
    
    # keep pushing down while going back
    grogu.front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED, 30, then=grogu.Stop.HOLD, wait=False)

    # Pull back rowing machine by going back straight in reverse
    # HCK 2: Lowered distance to not pull too much // 180 --> 160 --> Aftert new combined trips --> 150 --> afrter unified 140 --> 125
    # OLD WITHOUT GYRO grogu.robot.straight(-125)
    grogu.robot.straight(-130)

    # TUNING down from -8/6 degrees to -10/8
    grogu.robot.stop()
    grogu.robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=10)
    # drive_utils.gyro_turn(grogu.robot, grogu.gyro, -6)
    # drive_utils.gyro_turn(grogu.robot, grogu.gyro, 4)
    # grogu.robot.turn(-8)
    # grogu.robot.turn(6)

    grogu.front_motor_2.run_angle(0.5*config.ARM_MOTOR_SPEED, -160, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.stop()

    # Come back home
    grogu.robot.settings(straight_speed=DRIVE_SPEED_FAST, turn_rate=30)
    grogu.robot.straight(-1880)

    # End of trip: Stop Robot and all motors
    grogu.robot.stop()
    grogu.front_motor_1.stop()
    grogu.front_motor_2.stop()
