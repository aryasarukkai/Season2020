import config
import grogu
import drive_utils

def run_trip():
    # Initilize our motors
    left_motor = grogu.Motor(grogu.Port.A)
    right_motor = grogu.Motor(grogu.Port.D)
    front_motor_1 = grogu.Motor(grogu.Port.C)
    front_motor_2 = grogu.Motor(grogu.Port.B)

    grogu.left_motor.reset_angle(0)
    grogu.right_motor.reset_angle(0)
    grogu.front_motor_1.reset_angle(0)
    grogu.front_motor_2.reset_angle(0)

    # Initialize the color sensor.
    left_sensor = grogu.ColorSensor(grogu.Port.S4)
    right_sensor = grogu.ColorSensor(grogu.Port.S1)

    # Speeds
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
    # Initialize the Gyro sensor
    gyro = grogu.GyroSensor(grogu.Port.S2)
    grogu.gyro.reset_angle(0)

    # All parameters are in millimeters
    grogu.robot = grogu.DriveBase(grogu.left_motor, grogu.right_motor, wheel_diameter=config.WHEEL_DIAMETER, axle_track=config.AXLE_TRACK)

    # Set the straight speed and turn rate
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_FAST, turn_rate=config.TURN_RATE)

    grogu.robot.straight(700)
    grogu.robot.straight(-1100)

    # End of trip: Stop Robot and all motors
    grogu.robot.stop()
    grogu.front_motor_1.stop()
    grogu.front_motor_2.stop()
