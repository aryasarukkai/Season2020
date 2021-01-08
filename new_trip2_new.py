import config
import grogu
import drive_utils

def run_trip():
    # Go forward
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



