#!/usr/bin/env python
# coding: utf-8

import socket
import sys
#sys.path
from Seal import*
from function  import*

hote = "172.20.10.6"
port = 15555
print( "Connection on {}".format(port) )

s=Com()
time.sleep(2)
s.start()
time.sleep(2)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
time.sleep(2)
s.atach()
time.sleep(2)

for line in socket.makefile():
	tab=decoding_joy(line)
	print(tab)
	s.propellers(tab[4],tab[3],tab[1],tab[1])

# socket.send(u"Hey my name is Olivier!")

print( "Close" )
socket.close()
