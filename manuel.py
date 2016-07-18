#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*
from serial import*
import serial
from serial.serialposix import Serial, PosixPollSerial

class Communication:
	#Classe permettant de communiqué directement avec la carte Arduino par des commandes simples

	def __init__(self):
		#Ouverture du port serie
		self.ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
		print("Serial open")
		print(self.ser.readline())
		

	def propeller(self, id_propeller, value):
		if id_propeller == 'babore' :
			Propeller_order = '$PRO,' + str(value)+ ',' + str(0) + ',' + str(0) + ',' + str(0) + '\n'
			byte = str.encode(Propeller_order)
			#print('code envoyé :  ' + str(byte) )
			self.ser.write(byte)
		elif id_propeller == "tribore" :
			Propeller_order = '$PRO,' + str(0)+ ',' + str(value) + ',' + str(0) + ',' + str(0) + '\n'
			byte = str.encode(Propeller_order)
			#print('code envoyé :  ' + str(byte) )
			self.ser.write(byte)
		elif id_propeller == "front" :
			Propeller_order = '$PRO,' + str(0)+ ',' + str(0) + ',' + str(value) + ',' + str(0) + '\n'
			byte = str.encode(Propeller_order)
			#print('code envoyé :  ' + str(byte) )
			self.ser.write(byte)
		elif id_propeller == "rear" :
			Propeller_order = '$PRO,' + str(0)+ ',' + str(0) + ',' + str(0) + ',' + str(value) + '\n'
			byte = str.encode(Propeller_order)
			#print('code envoyé :  ' + str(byte) )
			self.ser.write(byte)
		else :
			print("Error Id PROPELLER")
		print(self.ser.readline())

	def propellers(self, Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear):
		Propeller_order = '$PRO,' + str(Propeller_babore)+ ',' + str(Propeller_tribore) + ',' + str(Propeller_front) + ',' + str(Propeller_rear) + '\n'
		byte = str.encode(Propeller_order)
		#print('code envoyé :  ' + str(byte) )
		print('code envoyé :  ' + str(byte) )
		self.ser.write(byte)
		time.sleep(2)
		print(self.ser.readline())

	def show(self):
		read_serial()
		print("attend")
	


if __name__ == '__main__' :
        print('tt')        


