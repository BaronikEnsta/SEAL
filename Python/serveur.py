# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:20:44 2016

@author: kbaroni
"""

import socket
import sys
from Seal import*
from function  import*

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

socket.listen(1)
client, address = socket.accept()
print("{} connected".format( address ) )

s=Com()
time.sleep(2)
s.start()
time.sleep(2)
s.atach()
time.sleep(2)

for line in socket.makefile():
	s.show()	
	tab=decoding_joy(line)
	print(tab)
	if s.go != 0 :
		propeller_babord = ( int( tab[1] ) + int( tab[2] ) ) / 2
		propeller_tribord = ( int( tab[1] ) - int( tab[2] ) ) / 2
		propeller_vertical = int( tab[4] )
		s.propellers(propeller_babord,propeller_tribord,propeller_vertical,propeller_vertical)
	else :
		s.propellers(0,0,0,0)

#s.close()
client.close()
socket.close()
print("Close")