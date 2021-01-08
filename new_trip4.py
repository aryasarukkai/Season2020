import config
import grogu
import drive_utils

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
    grogu.robot = grogu.DriveBase(grogu.left_motor, grogu.right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
    # Set the straight speed and turn rate
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

    # First adjust the elevator, Go down to touch floor, then go back up to give enough distance to ground
    # OLD WORKING PROGRAM DELETED front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -15, then=Stop.HOLD, wait=True)
    # DBG NEW GO UP LESSER 120 --> 90
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED_FAST, 90, then=grogu.Stop.HOLD, wait=True)
    grogu.front_motor_1.stop()

    # Go straight to the bench mission
    grogu.robot.straight(430)
    grogu.robot.stop()
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=30)

    # Turn left and then right to topple bench
    grogu.robot.turn(-35)
    grogu.robot.straight(-30)
    grogu.robot.turn(25)

    # Back out a bit and then go forward to goto bar
    # DBG Original robot.straight(-30)
    grogu.robot.straight(110)

    # Turn to align with bar and then pull elevator up to dislodge bar then turn left to be back to parallel path
    grogu.robot.turn(15)
    grogu.front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 200, then=grogu.Stop.HOLD, wait=True)
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -200, then=grogu.Stop.HOLD, wait=True)

    # Doing it one more time to ensure that the 
    grogu.front_motor_1.run_angle(2*config.ARM_MOTOR_SPEED_FAST, 250, then=grogu.Stop.HOLD, wait=True)
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -250, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.turn(-15)

    # pull up motor 1 and turn right and Drop blocks
    '''
    # ADDED NEW
    grogu.robot.turn(30)
    grogu.robot.straight(-20)
    grogu.front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, 1000, then=grogu.Stop.HOLD, wait=True)  
    grogu.front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, -1100, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.turn(-30)
    #END ADDED NEW
    '''
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
    # DEBUG REDUCED IN LATEST RUN from -70 --> -60 --> -40 ==> REMOVED
    # grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -40, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.straight(-200)
    grogu.robot.stop()

    # Turn right and then goto the basketball mission
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_FAST, turn_rate=30)
    grogu.robot.turn(60)
    grogu.robot.straight(160)
    grogu.robot.turn(20)
    grogu.robot.straight(300)
    grogu.robot.turn(-90)
    grogu.robot.straight(250)
    # Final step, turn more with added weight of cube drop -15 --> -25
    grogu.robot.turn(-25)
    # HCK Adding more forward distance as it stopped working 90 --> 110 --> 120 --> 130 --> after unified back to 120 --> 110 --> 100
    grogu.robot.straight(110)

    # Drop blocks into basket
    grogu.robot.turn(30)
    grogu.front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, 1900, then=grogu.Stop.HOLD, wait=True)  
    grogu.front_motor_2.run_angle(2*config.ARM_MOTOR_SPEED, -2000, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.turn(-30)

    # Now pull up basketball basket to middle and lower down 10 --> 20
    # DEBUG REMOVED AFTER ADDING ABOVE grogu.robot.straight(10)
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 1000, then=grogu.Stop.HOLD, wait=True)
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -300, then=grogu.Stop.HOLD, wait=True)
    grogu.robot.turn(-10)

    # Goto to robot dance area and dance
    # HCK turn increased based on run - from -75 --> -85 --> -70 --> -85 after blocks weight
    # After unified run -85 --> -95 --> -85 --> -80 --> -70
    grogu.robot.turn(-70)
    grogu.robot.straight(-325)
    i=0
    for i in range(0,20):
        grogu.robot.turn(-15)
        grogu.robot.turn(15)
        grogu.ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'], tempo=278)
        i=i+1

    grogu.robot.stop()

    # End of trip: Stop Robot and all motors
    grogu.robot.stop()
    grogu.front_motor_1.stop()
    grogu.front_motor_2.stop()
