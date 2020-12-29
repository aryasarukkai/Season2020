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
            break;
        elif (reflection_value >= config.WHITE_THRESHOLD):
            detectedWhite = True
            # print("White " + str(reflection_value))

def drive_till_white(robot, sensor):
    # Drive forward till we sense black followed by white
    detectedBlack = False
    while True:
        robot.drive(config.DRIVE_SPEED_SLOW, 0)

        reflection_value = sensor.reflection()
        if (reflection_value >= config.WHITE_THRESHOLD and detectedBlack):
            # print("White " + str(reflection_value)) 
            # Use line above to debug
            robot.stop()
            break
        elif (reflection_value <= config.BLACK_THRESHOLD):
            detectedBlack = True
            
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
