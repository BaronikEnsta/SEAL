#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*

from serial import*
from serial.serialposix import Serial, PosixPollSerial
import serial
import string
import sys
from threading import Thread
import time

global no_port_arduino
no_port_arduino=0
global baud_arduino
baud_arduino=57600
global encoding_arduino
encoding_arduino='ascii' #'utf-8'


def requirement(tab) :
	if len(tab) != 11 :
		return False
	for j in range ( 1, len(tab) ) :
		if isinstance( tab[j] , int) != True :
			return False
	for i in range ( 2, 5 ) :
		if tab[i]  > 100 and tab[i]  < -100 :
			return False
	

def decoding(bit) :
	toto=str(bit)
	"""print(bit)
	print(toto)
	print(len(bit))
	print(toto[  toto.index("$INFO") : len(toto) -5 ])"""
	"""line = bit.decode('ascii')   #   'utf8'  'ascii'	
	#print(line[-line.index('$'):-1])
	tab = line.split(',' ,11)"""
	toto=toto[  toto.index("$INFO") : len(toto) -5 ]
	tab = toto.split(',' , 13 )
	for i in range (1,len(tab)) :
		if isinstance( tab[i] , int) == True :
			tab[i] = int( tab[i] )
	return tab

def get_port():
	return no_port_arduino

def get_baud():
	return baud_arduino

def get_encoding():
	return encoding_arduino

def read_serial( ser ):
	#ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	
	bit=ser.readline()
	toto=str(bit)
	while ( toto.find("$INFO") == -1 ):
		bit=ser.readline()
		toto=str(bit)

	tab=decoding(bit)
	#ser.flush()
	while tab[0] !="$INFO"  and requirement(tab) == False:
		bit=ser.readline()
		tab=decoding(bit)
		#ser.flush()
		#print("je boucle")
	print(tab)
	return tab
	
def decoding_joy(bit) :
	toto=str(bit)
	toto=toto[  toto.index("$JOY") : toto.index("*") ]
	tab = toto.split(',' , 13 )
	for i in range (1,len(tab)) :
		if isinstance( tab[i] , int) == True :
			tab[i] = int( tab[i] )
	tab[1] = max( [ int( tab[1] ) - 5, -100 ]
	tab[2] = max( [ int( tab[2] ) - 2, -100 ]
	tab[3] = max( [ int( tab[3] ) - 5, -100 ]
	return tab
		
