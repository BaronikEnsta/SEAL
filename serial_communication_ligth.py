#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*

# SEAL__Propeller_states -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__External_pressure -> range value [ ]
# SEAL__Mission_departure -> 0 no departure mission, 1024 go mission
# SEAL__Propller_order -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__Led_order -> Led1, Led2, Led3, Led4 -> 1 on, 0 off -> signal : value_Led1value_Led2value_Led3value_Led4
# Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear, External_pressure, Mission_departure, Azimuth, Pitch Angle, Roll Angle, Temperature

from serial import*
import time
from serial.serialposix import Serial, PosixPollSerial
import string
import sys
import serial
from function import *
import os

#________________Init___________________
ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)


#________________Loop()________________
while True :

	#______read()_____
	tab=read_serial()
	
	sealState = open("Seal_State_Now.txt","r")
	sealState.close()
	
	#______work()_____



	#______write()_____
	for i in range (1,3):
		if (ser.isOpen()):
			Propeller_order = '$PRO,' + str(Propeller_trib)+ ',' + str(Propeller_babo) + ',' + str(Propeller_fron) + ',' + str(Propeller_rear) + '\r\n'
			byte = str.encode(Propeller_order)
			ser.write(byte)
			print('code envoyé :  ' + str(byte) )
			time.sleep(1)

	sealState = open("Seal_State_Now.txt","w")
	sealState.close()
