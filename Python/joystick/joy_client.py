#!/usr/bin/env python
# coding: utf-8

import socket
import sys
#sys.path
from Seal import*
from function  import*

go=0
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
	try :
		tab_info=decoding(s.show())
		go = int(tab_info[8])
	except:
		#go=0
		pass
	tab=decoding_joy(line)
	print(tab)
	#for i in range(1,4) :
	#	if int( tab[i] ) < 6 & int( tab[i] ) > -6 :
	#		tab[i] = 0
	if go != 0 :
		propeller_babord = ( int( tab[1] ) + int( tab[2] ) ) / 2
		propeller_tribord = ( int( tab[1] ) - int( tab[2] ) ) / 2
		propeller_vertical = int( tab[3] )
		s.propellers(propeller_babord,propeller_tribord,propeller_vertical,propeller_vertical)
	else :
		s.propellers(0,0,0,0)

# socket.send(u"Hey my name is Olivier!")

#s.close()
print( "Close" )
socket.close()
