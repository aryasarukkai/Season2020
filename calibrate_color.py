#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create a data log file in the project folder on the EV3 Brick.
# * By default, the file name contains the current date and time, for example:
#   log_2020_02_13_10_07_44_431260.csv
# * You can optionally specify the titles of your data columns. For example,
#   if you want to record the motor angles at a given time, you could do:
data = DataLog('time', 'sensor_value', name='log', timestamp=False, extension='csv', append=False)
colorValues = DataLog('color', 'value', name='color', timestamp=False, extension='csv', append=False)
message = Font()

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Create your objects here.
ev3 = EV3Brick()

# Initialize the color sensor.
left_sensor = ColorSensor(Port.S1)

# Place on black.
ev3.speaker.say("Place on black")

# Write the value of the left color sensor to the screen.
while True:
    # print("Button pressed: " + str(ev3.buttons.pressed()))
    if (Button.CENTER in ev3.buttons.pressed()):
        # Check the value of reflected light
        reflected_light = left_sensor.reflection()
        colorValues.log('black', reflected_light)
        ev3.speaker.say("Recorded black")
        break

# Place on white.
ev3.speaker.say("Place on white")
while True:
    if (Button.CENTER in ev3.buttons.pressed()):
        # Check the value of reflected light
        reflected_light = left_sensor.reflection()
        colorValues.log('white', reflected_light)
        ev3.speaker.say("Recorded white")
        break


