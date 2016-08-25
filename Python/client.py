#!/usr/bin/env python
# coding: utf-8

import socket
import sys
from joystick import Joystick

go=0
<<<<<<< HEAD
hote = "172.20.10.5"
=======
<<<<<<< HEAD
hote = "172.20.10.5"
=======
<<<<<<< HEAD
hote = "172.20.10.5"
=======
<<<<<<< HEAD
hote = "172.20.10.5"
=======
<<<<<<< HEAD
hote = "172.20.10.5"
=======
hote = "127.0.0.1"
>>>>>>> origin/master
>>>>>>> origin/master
>>>>>>> origin/master
>>>>>>> origin/master
>>>>>>> origin/master
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
