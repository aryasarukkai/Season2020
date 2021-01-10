import config
import grogu
import drive_utils

def run_trip():
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_NORMAL, turn_rate=config.TURN_RATE)

   # Go forward 600mm 
    grogu.robot.straight(750)

    # Drive forward till we sense white followed by black
    drive_utils.drive_till_black(grogu.robot, grogu.left_sensor)
            
    # Turn left
    # ORIG drive_utils.gyro_turn(grogu.robot, grogu.gyro, -37)
    # REDUCE TO LESSER WITHOUT GYRO
    grogu.robot.turn(-37)

    # Go forward to the tire
    grogu.robot.straight(265)

    # Turn the arm up to flip the tire
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED_FAST, 320, then=grogu.Stop.HOLD, wait=True)

    # Go backwards 
    grogu.robot.straight(-100)

    # Turn left to go under the bridge
    drive_utils.gyro_turn(grogu.robot, grogu.gyro, -46)

    # Go back and align with the wall before going forward.
    grogu.robot.straight(-200)

    # Bring the arm down so that it doesn't crash in the bridge
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -150, then=grogu.Stop.HOLD, wait=True)

    # Go under the bridge
    grogu.robot.straight(500)

    # Turn the arm up to not interfere
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, 320, then=grogu.Stop.HOLD, wait=True)

    # Go under the bridge and align with black line beyond the bridge
    drive_utils.drive_till_black(grogu.robot, grogu.right_sensor)

    # Go forward a bit more
    grogu.robot.straight(150)

    # Turn left towards the swing
    drive_utils.gyro_turn(grogu.robot, grogu.gyro, -103)

    # Bring the Tire arm down
    grogu.front_motor_1.run_angle(config.ARM_MOTOR_SPEED, -240, then=grogu.Stop.HOLD, wait=True)

    #Bring slide arm down
    grogu.front_motor_2.run_angle(config.ARM_MOTOR_SPEED, 205, then=grogu.Stop.HOLD, wait=True)

    #Go straight to the slide
    grogu.robot.straight(210)

    #slide the people off the slide
    grogu.front_motor_2.run_angle(config.ARM_MOTOR_SPEED_SUPER_FAST, -120, then=grogu.Stop.HOLD, wait=True)

    grogu.robot.stop()

    # Set the straight speed and turn rate
    grogu.robot.settings(straight_speed=config.DRIVE_SPEED_SUPER_FAST, turn_rate=config.TURN_RATE)

    # Turn left to go back to base
    grogu.robot.turn(19)

    #Go straight to base
    grogu.robot.straight(200)

    # Turn left to go back to base
    grogu.robot.turn(-17)

    #Go straight to base
    grogu.robot.straight(1000)

    # End of trip: Stop grogu.robot and all motors
    grogu.robot.stop()
    grogu.front_motor_1.stop()
    grogu.front_motor_2.stop()



