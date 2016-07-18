#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*

# SEAL__Propeller_states -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__External_pressure -> range value [ ]
# SEAL__Mission_departure -> 0 no departure mission, 1024 go mission
# SEAL__Propller_order -> Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear -> range value [ -100 ; 100 ]
# SEAL__Led_order -> Led1, Led2, Led3, Led4 -> 1 on, 0 off -> signal : value_Led1value_Led2value_Led3value_Led4

from serial import*
import time
from serial.serialposix import Serial, PosixPollSerial
import string
import sys
import serial
from shareddata import SharedMemory
from function import *

#________________Init___________________
ser = serial.Serial( port = '/dev/ttyACM{no_port}'.format(no_port=get_port()) , baudrate = 9600 , parity = serial.PARITY_NONE , stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS )
with SharedMemory() as shm:
	data1,  data2 , data3 = shm.fetch_new_data( [ 'SEAL__Propeller_states', 'SEAL__External_pressure', 'SEAL__Mission_departure' ] )

#________________Loop()________________
while True :

	#______read()_____
	tab=read_serial()

	for frame1, frame2 in shm.read( [ 'SEAL__Propller_order', 'SEAL__Led_order' ] ) :
		print( frame1.value, frame2._asdict() )
		sleep(1)

	#______work()_____
	Propeller_order = '$PRO,' + Propeller_trib + ',' + Propeller_babo + ',' + Propeller_fron + ',' + Propeller_rear + ',' + str(frame2) + '\n'
	bytes = str.encode(Propeller_order)

	tab=line.split(',' ,7)
	data1=[ int( tab[1] ), int( tab[2] ), int( tab[3] ), int( tab[4] ) ] 
	data2=tab[5]
	data3=tab[6]


	#______write()_____
	if (ser.isOpen()):
		ser.write(bytes) 
		time.sleep(1)

	for dac1, dac2, dac3 in DACS :
		data1.set( value = dac1, ts = time.time() )
		data2.set( value = dac2, ts = time.time() )
		data3.set( value = dac3, ts = time.time() )
		shm.write_datas( datalist, timestamp = time.time() )
		sleep(1)
