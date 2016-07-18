#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*

from serial import*
import time
from serial.serialposix import Serial, PosixPollSerial
import string
import sys
import serial
from function import *  # or import function as fct -> fct.requirement(tab)
import io

def read_serial_bytes():
	lin = ""
	tabl = []
	while len(tabl)<20:
		char = ser.read(8)
		if  char== '$': 
			lin += ser.read()
		elif char == '\n' and len(lin) > 1 :
			break
		tabl.append(lin)
		lin = ""
	print(tabl)


def tmtc(a, b, c, d) :	
	ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	print("Serial port open")
	print ('order :   ' + a + ' ' + b+ ' ' + c + ' ' +d)
	read_serial(ser)	
	for i in range (1,3):
		if (ser.isOpen()):
			ser.flush()
			Propeller_trib = int(a)
			Propeller_babo= int( b)
			Propeller_fron = int(c)
			Propeller_rear = int(d)
			Propeller_order = '$PRO,' + str(Propeller_trib)+ ',' + str(Propeller_babo) + ',' + str(Propeller_fron) + ',' + str(Propeller_rear) + '\r\n'
			byte = str.encode(Propeller_order)
			#code=b"$PRO,-100,0,90,-10\n"
			print('code envoyé :  ' + str(byte) )
			ser.flush()
			ser.write(byte)
			ser.flush()
			
			read_serial(ser)
			#print(ser.readline())
			time.sleep(1)
	#ser.close()
	#print("Serial port close")

	time.sleep(1)
	ser.flush()
	#ser= serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	#print("Serial port open")	
	read_serial(ser)
	#time.sleep(1)
	#read_serial(ser1)
	ser.close()
	print("Serial port close")
	

if  len(sys.argv) >1:
	tmtc(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	#sys.exit(1)
else:
	print('tu as rien mit')

#if __name__ == '__main__' :
#	ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
# 	sio=io.TextIOWrapper( io.BufferedRWPair(ser,  ser) )
#	sio.write(unicode("$PRO,-100,0,90,-10\n"))
#	sio.flush()
#	pro=sio.readline()
#	print(pro)

