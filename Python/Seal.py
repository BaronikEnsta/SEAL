#! /usr/share/raspi-ui-overrides/applications/idle3.desktop
# -*-coding:utf-8-*
import sys
from serial import*
import serial
from serial.serialposix import Serial, PosixPollSerial
from function import*  # or import function as fct -> fct.requirement(tab)
from threading import Thread, RLock

class Com(Thread):
	"""Class for Communicated with Arduino.

	This class can be call with shell python or normaly shell with "main" at end

	Args:

	Attributes:
		txt (file): file text that has all messsages in transit on serial connection.
		chaine (string): messsages in transit on serial connection.
		stop (bool): permission for write on txt.

	"""

	def __init__( self ):
		Thread.__init__(self)
		self.txt = open("/home/pi/Documents/Python/Seal_Full_State.txt","w")
		self.chaine=""
		self.stop = False
		self.daemon = True
		self.go = False
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
			try :
				tab_info=decoding(self.chaine)
<<<<<<< HEAD
				self.go = False if int(tab_info[8]) > 0 else True
=======
				self.go = True if int(tab_info[8]) > 0 else False
>>>>>>> origin/master
			except:
				pass
	
	def show( self ):
		"""Class for see one message send by Arduino for Raspberry PI 3.

		This message look like:
		$INFO,#message,Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear, State_propellers ,External_pressure, Mission_departure, Azimuth, Pitch Angle, Roll Angle, Temperature
		
		#message: is the number of this message and matches of number of messages send by Arduino from the beginning
		Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear: is the value of propeller between -100 and 100
		State_propellers: if the propellers are attached (in Pin of Arduino), example: all propellers attached -> 1111, any -> 0000, just Propeller_tribore -> 0100
		External_pressure: External pressure of SEAL
		Mission_departure: 0 no departure mission, 1024 go mission
		Azimuth, Pitch Angle, Roll Angle: value of compass
		Temperature: internal temperature of SEAL given by compass

		Args:

		Attributes:

		"""
		print(self.chaine)
		return(self.chaine)
		

	def send( self, message ):	
		"""Class for send message from Raspberry PI 3 for Arduino.

		This message must start with '$' and finish '\n', and the argument massage is insert between this two char.
		
		Args:
			message (string): 

		Attributes:
			byte (): is the message that is encoding (in get_encoding()) 
		"""	
		message = '$' + message + '\n'
		byte=message.encode(get_encoding())
		self.ser.write(byte)
		print('code envoyé :  ' + str(byte) )
		#time.sleep(3)
		print(self.chaine)


	def propellers( self, Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear ):
		"""Class for send order of propulsion for each propellers.

		This order look like:
		$PRO,Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear

		Args:
			Propeller_babore: range value [ -100 ; 100 ]
			Propeller_tribore: range value [ -100 ; 100 ]
			Propeller_front: range value [ -100 ; 100 ]
			Propeller_rear: range value [ -100 ; 100 ]

		Attributes:
			byte (): is the message that is encoding (in get_encoding())
			order (string): is the order that write on the file txt and start with ">>>"

		"""
		Propeller_order = '$PRO,' + str(Propeller_babore)+ ',' + str(Propeller_tribore) + ',' + str(Propeller_front) + ',' + str(Propeller_rear) + '\n'
		byte=Propeller_order.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + Propeller_order
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		#time.sleep(3)
		print(self.chaine)


	def atach( self ):
		"""Class for send order for atach the propellers (in Pin of Arduino).

		This order look like:
		$ATACH
		
		Args:

		Attributes:
			byte (): is the message that is encoding (in get_encoding()) 
			order (string): is the order that write on the file txt and start with ">>>"

		"""	
		code= '$ATACH' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		#time.sleep(3)
		print(self.chaine)


	def detatach( self ):
		"""Class for send order for detatach the propellers (in Pin of Arduino).

		This order look like:
		$STOP
		
		Args:

		Attributes:
			byte (): is the message that is encoding (in get_encoding()) 
			order (string): is the order that write on the file txt and start with ">>>"

		"""	
		code= '$STOP' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		#time.sleep(3)
		print(self.chaine)


	def initia( self ):
		"""Class for send order of initialized each variator

		This order look like:
		$INIT
		
		Args:

		Attributes:
			byte (): is the message that is encoding (in get_encoding()) 
			order (string): is the order that write on the file txt and start with ">>>"

		"""	
		code= '$INIT' + '\n'
		byte=code.encode(get_encoding())
		self.ser.write(byte)
		order = ">>> " + code
		self.txt.write(order)
		print('code envoyé :  ' + str(byte) )
		#time.sleep(3)
		print(self.chaine)


	def close( self ):
		"""Class for close the serial port and detach each propellers

		First each propellers is detached (in Pin of Arduino), for this we send a message ($STOP).
		Then we close the serial port.
		
		Args:

		Attributes:
			byte (): is the message that is encoding (in get_encoding()) 
			order (string): is the order that write on the file txt and start with ">>>"

		"""		
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

