#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

import config
import grogu
from time import sleep

import new_trip1
import new_trip2
import new_trip3
import new_trip4

font = Font(size=13)
trip_font = Font(size=15, bold=True)

xaxis = 25
yaxis = 40
while True:
    grogu.ev3.screen.clear()
    grogu.ev3.screen.set_font(font)
    
    # Display the instructions to run the different trips.
    grogu.ev3.screen.draw_text(xaxis, yaxis, "Up Button")
    grogu.ev3.screen.draw_text(xaxis + 90, yaxis, "- Trip 1")
    grogu.ev3.screen.draw_text(xaxis, yaxis + 20, "Right Button")
    grogu.ev3.screen.draw_text(xaxis + 90, yaxis + 20, "- Trip 2")
    grogu.ev3.screen.draw_text(xaxis, yaxis + 40, "Down Button")
    grogu.ev3.screen.draw_text(xaxis + 90, yaxis + 40, "- Trip 3")
    grogu.ev3.screen.draw_text(xaxis, yaxis + 40, "Left Button")
    grogu.ev3.screen.draw_text(xaxis + 90, yaxis + 40, "- Trip 4")

    grogu.ev3.speaker.beep()

    # Wait until any Brick Button is pressed.
    while not any(grogu.ev3.buttons.pressed()):
        wait(10)

    grogu.ev3.screen.clear()
    grogu.ev3.screen.set_font(trip_font)

    # Respond to the Brick Button press.  Display the chosen pattern on
    # the screen and drive in this pattern.
    if Button.UP in grogu.ev3.buttons.pressed():
        # Run trip 1
        grogu.ev3.screen.draw_text(xaxis, yaxis + 20, "Running Trip 1")
        new_trip1.run_trip()

    if Button.RIGHT in grogu.ev3.buttons.pressed():
        # Run trip 2
        grogu.ev3.screen.draw_text(xaxis, yaxis + 20, "Running Trip 2")
        new_trip2.run_trip()
 
    if Button.DOWN in grogu.ev3.buttons.pressed():
        # Run trip 3
        grogu.ev3.screen.draw_text(xaxis, yaxis + 20, "Running Trip 3")
        new_trip3.run_trip()

    if Button.LEFT in grogu.ev3.buttons.pressed():
        # Run trip 4
        grogu.ev3.screen.draw_text(xaxis, yaxis + 20, "Running Trip 4")
        new_trip4.run_trip()
    # wait few milliseconds before next read
    wait(10)




