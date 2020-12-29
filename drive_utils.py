import config

def drive_till_black(robot, sensor):
    # Drive forward till we sense white followed by black
    detectedWhite = False
    while True:
        robot.drive(config.DRIVE_SPEED_SLOW, 0)

        reflection_value = sensor.reflection()
        if (reflection_value <= config.BLACK_THRESHOLD and detectedWhite):
            # print("Black " + str(reflection_value))
            robot.stop()
            break
        elif (reflection_value >= config.WHITE_THRESHOLD):
            detectedWhite = True
            # print("White " + str(reflection_value))
            
def drive_till_white(robot, sensor):
    # Drive forward till we sense white followed by black
    detectedBlack = True
    while True:
        robot.drive(config.DRIVE_SPEED_SLOW, 0)

        reflection_value = sensor.reflection()
        if (reflection_value <= config.WHITE_THRESHOLD and detectedBlack):
            # print("Black " + str(reflection_value))
            robot.stop()
            break
        elif (reflection_value >= config.WHITE_THRESHOLD):
            detectedWhite = True

def gyro_turn(robot, gyro, angle):
    gyro.reset_angle(0)

    direction = angle/abs(angle)
    angle = abs(angle)

    while True:
        if (direction == -1):
            # Turn left
            robot.turn(-1)
        else:
            # Turn right
            robot.turn(1)
        
        if (abs(gyro.angle()) >= angle):
            print("Stopping the robot at angle " + str(gyro.angle()))
            robot.stop()
            if ((abs(gyro.angle()) - angle) > config.TURN_THRESHOLD):
                # Turn the robot the other way.
                print("Fixing the overshoot " + (abs(gyro.angle()) - angle))
                gyro_turn(robot, gyro_sensor, (direction * -1) * (abs(gyro.angle()) - angle))
                
            break;
        
def follow_line(drive_speed, distance):
    left_motor = Motor(Port.D, Direction.CLOCKWISE)
    right_motor = Motor(Port.A, Direction.CLOCKWISE)

    line_sensor = ColorSensor(Port.S1)

    # All parameters are in millimeters
    robot = DriveBase(left_motor, right_motor, wheel_diameter=config.WHEEL_DIAMETER, axle_track=config.AXLE_TRACK)

    # Set the straight speed to 100 and turn speed to 100
    robot.settings(straight_speed=drive_speed, turn_rate=30)
    robot.reset()

    BLACK = 3
    WHITE = 62

    threshold_1 = int((WHITE-BLACK)/3)+BLACK
    threshold_2 = WHITE-int((WHITE-BLACK)/3)

    while True:
        reflection_value = line_sensor.reflection()
        if (reflection_value <= threshold_1):
            robot.stop()
            right_motor.run_angle(drive_speed, 50)
            left_motor.stop()

        elif (reflection_value >= threshold_2):
            robot.stop()
            left_motor.run_angle(drive_speed, 50)
            right_motor.stop()

        else:
            robot.drive(drive_speed, 0)
            wait(10)
            if (robot.distance() >= distance):
                robot.stop()

