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
baud_arduino=115200

def requirement(tab) :
	if len(tab) != 7 :
		return False
	for j in range ( 1, len(tab) ) :
		if isinstance( tab[j] , int) != True :
			return False
	for i in range ( 1, 4 ) :
		if tab[i]  > 100 and tab[i]  < -100 :
			return False
	

def decode(bit) :
	line = bit.decode('utf8')   #   'utf8'  'ascii'
	tab = line.split(',' ,7)
	for i in range (1,len(tab)) :
		if isinstance( tab[i] , int) == True :
			tab[i] = int( tab[i] )
	return tab

def get_port():
	return no_port_arduino

def get_baud():
	return baud_arduino

def read_serial( ser ):
	#ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	bit=ser.readline()
	tab=decode(bit)
	while tab[0] !="$INFO" and requirement(tab) == False:
		bit=ser.readline()
		tab=decode(bit)
	print(tab)
	return tab
	#print(len(tab))
	#data1=[ int( tab[1] ), int( tab[2] ), int( tab[3] ), int( tab[4] ) ] 
	#data2=tab[5]
	#data3=tab[6]
	#print(data1)
	#print(data2)
	#print(data3)
	#ser.close()

#class read_serial_thread(Thread):             # ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
#	def __init__(self, ser):
#		Thread.__init__(self)
#		self.ser = ser 

#	def run(self):
		
