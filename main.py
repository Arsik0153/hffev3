#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import socket

HOST = '192.168.100.38'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Init
brick.sound.beep()

price = {
    1: 950,
    2: 1100,
    3: 1250
}

ul1 = UltrasonicSensor(Port.S1)
ul2 = UltrasonicSensor(Port.S2)
ul3 = UltrasonicSensor(Port.S3)

mA = Motor(Port.A)
mB = Motor(Port.B)
mC = Motor(Port.C)

while True:
    if ul1.distance() > 150:
        s.sendall(str(price[1]))
        mA.run_time(-700, 2000, Stop.COAST)
    if ul2.distance() > 150:
        s.sendall(str(price[2]))
        mB.run_time(-700, 2000, Stop.COAST)
    if ul3.distance() > 150:
        s.sendall(str(price[3]))
        mC.run_time(-700, 2000, Stop.COAST)

    
    wait(4000)
    