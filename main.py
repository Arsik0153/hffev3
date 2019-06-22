#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

balance = 10000

price = {
    1: 1000,
    2: 2000,
    3: 3000
}

ul1 = UltrasonicSensor(Port.S1)
ul2 = UltrasonicSensor(Port.S2)
ul3 = UltrasonicSensor(Port.S3)

while True:
    if ul1.distance() > 