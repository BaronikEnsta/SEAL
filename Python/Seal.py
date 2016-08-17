#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*
import sys
from serial import*
import serial
from serial.serialposix import Serial, PosixPollSerial
from function import *  # or import function as fct -> fct.requirement(tab)
from threading import Thread, RLock

class Com(Thread):
	#Classe permettant de communiqué directement avec la carte Arduino par des commandes simples

	def __init__( self ):
		Thread.__init__(self)
		self.txt = open("/home/pi/Documents/Python/Seal_Full_State.txt","w")
		self.chaine=""
		self.stop = False
		#Ouverture du port serie
		try :
			#self.ser = serial.Serial(port='/dev/ttyACM0',baudrate=get_baud())
			self.ser = serial.Serial(port='/dev/ttyACM{no_port}'.format(no_port=get_port()),baudrate=get_baud(),parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
		except :
			print("Open Serial Error")
		
		print("Serial open")


	def run(self):
		while self.stop == False:
			self.chaine = self.ser.readline().decode(get_encoding())
			self.txt.write(self.chaine)
		
	
	def show( self ):
		print(self.chaine)
		

	def send( self, message ):		
		message = '$' + message + '\n'
		byte=message.encode(get_encoding())
		self.ser.write(byte)
		print('code envoyé :  ' + str(byte) )
		time.sleep(3)
		print(self.chaine)


	def propellers( self, Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear ):
		Propeller_order = '$PRO,' + str(Propeller_babore)+ ',' + str(Propeller_tribore) + ',' + str(Propeller_front) + ',' + str(Propeller_rear) + '\n'
		byte=Propeller_order.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + Propeller_order
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		time.sleep(3)
		print(self.chaine)


	def atach( self ):
		code= '$ATACH' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		time.sleep(3)
		print(self.chaine)


	def detatach( self ):
		code= '$STOP' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		time.sleep(3)
		print(self.chaine)


	def initia( self ):
		code= '$INIT' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		time.sleep(3)
		print(self.chaine)


	def close( self ):
		code= '$STOP' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		time.sleep(1)
		print(self.chaine)
		self.stop = True
		self.ser.close()
		print("Serial close")


if __name__ == '__main__' :
	print( '__main__')
	s=Com()
	s.start()
	s.show()
	s.atach()
	s.show()
	s.propellers(20,20,20,20)
	s.show
	s.propellers(0,0,0,0)
	s.show
	s.detach()
	s.close()

