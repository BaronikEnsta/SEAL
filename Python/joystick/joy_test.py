from joystick import *

with Joystick("/dev/ttyUSB2", 57600) as joy:
    for m in joy:
        print(m)
