#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*-

# SEAL__Propeller_states -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__External_pressure -> range value [ ]
# SEAL__Mission_departure -> 0 no departure mission, 1024 go mission
# SEAL__Propller_order -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__Led_order -> Led1, Led2, Led3, Led4 -> 1 on, 0 off -> signal : value_Led1value_Led2value_Led3value_Led4
# Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear, External_pressure, Mission_departure, Azimuth, Pitch Angle, Roll Angle, Temperature, Time

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
print("Serial port open")
sealState = open("/home/pi/Documents/Python/Seal_State_Now.txt","w")
sealState.write("0, 1, 2, 3, 4, 5, 6, 7, 8, 9, %s\n" % ( time.time() ) )
sealState.close()

ser.write(b"$ATACH\n")
print ("Propellers Attached")
time.sleep(1)
#ser.flush()
ser.write(b"$INIT\n")
print ("Propellers Initiated")
time.sleep(5)


#________________Loop()________________
#while True :
for i in range (1,4):

	#______read()_____
	tabSerial=read_serial(ser)
	#ser.flush()
	
	sealState = open("/home/pi/Documents/Python/Seal_State_Now.txt","r")
	line = sealState.readline().rstrip('\n\r')
	sealState.close()
	
	#______work()_____
	line = line.replace(' ','')
	tabFile = line.split(',' ,11)
	Propeller_babo = tabFile[0]
	Propeller_trib = tabFile[1]
	Propeller_fron = tabFile[2]
	Propeller_rear = tabFile[3]
	Propeller_order = '$PRO,' + str(Propeller_babo)+ ',' + str(Propeller_trib) + ',' + str(Propeller_fron) + ',' + str(Propeller_rear) + '\r\n'
	byte = str.encode(Propeller_order)
	#print('code envoyé :  ' + str(byte) )
	print(tabFile)

	
	#______write()_____
	for i in range (1,3):
		if (ser.isOpen()):
			ser.write(byte)
			#ser.flush()
			print('code envoyé :  ' + str(byte) )
			time.sleep(3)
			read_serial(ser)

	sealState = open("/home/pi/Documents/Python/Seal_State_Now.txt","w")
	sealState.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ( tabSerial[1], tabSerial[2], tabSerial[3], tabSerial[4], tabSerial[5], tabSerial[6], tabSerial[7], tabSerial[8], tabSerial[9], tabSerial[10], time.time() ) )
	sealState.close()

	time.sleep(1)
	#ser.flush()

ser.close()
print("Serial port close")




















