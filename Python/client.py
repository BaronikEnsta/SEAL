#!/usr/bin/env python
# coding: utf-8

import socket
import sys
from joystick import Joystick

go=0
hote = "172.20.10.5"
port = 15555
print( "Connection on {}".format(port) )


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))


with Joystick('/dev/ttyUSB2', 57600) as joy:
  for m in joy:
    print(m)
    socket.send(m)
    

print( "Close" )
socket.close()
