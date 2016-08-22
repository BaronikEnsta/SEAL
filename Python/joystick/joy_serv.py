import socket
from joystick import Joystick

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))


socket.listen(1)
client, address = socket.accept()
print("{} connected".format( address ) )

with Joystick('/dev/ttyUSB2', 57600) as joy:
  for m in joy:
    print(m)
    client.send(m)


client.close()
socket.close()
print("Close")
