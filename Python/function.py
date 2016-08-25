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
	"""Fonction qui s'assure que les valeur contenue dans le tableau sont correcte. 

	Tout d'abord elle vérifie si les cases du tableau contient bien des int sauf pour tab[0] qui contient "$INFO" .
	puis elle s'assure que les valeur de propulsion, qui se trouvent dans les cases allant de 2 à 5, 
	sont bien comprise entre -100 et 100.

	Args:
		tab(array): 

	Return:
		False(bool): si les valeurs ne correspondent pas à ce qui est attendue

	"""
	if len(tab) != 11 :
		return False
	for j in range ( 1, len(tab) ) :
		if isinstance( tab[j] , int) != True :
			return False
	for i in range ( 2, 5 ) :
		if tab[i]  > 100 and tab[i]  < -100 :
			return False
	

def decoding(bit) :
	"""Function for decoding bytes from Arduino.

	This function convert bytes on string and split on array after each ",".
	
	Args:
		bits(byte): bytes from joystick 

	Return:
		tab(array): 	tab[0] = $INFO
				tab[1]-> is the number of this message and matches of number of messages send by Arduino from the beginning
				tab[2]-> Propeller_babore value read 
				tab[3]-> Propelle_tribore value read
				tab[4]-> Propeller_front value read
				tab[5]-> Propeller_rear value read
				tab[6]-> State_propellers
				tab[7]-> External_pressure
				tab[8]-> Mission_departure
				tab[9]-> Azimuth
				tab[10]-> Pitch Angle
				tab[11]-> Roll Angle
				tab[12]-> Temperature on SEAL
				
	"""
	toto=str(bit)
	toto=toto[  toto.index("$INFO") : len(toto) -5 ]
	tab = toto.split(',' , 13 )
	for i in range (1,len(tab)) :
		if isinstance( tab[i] , int) == True :
			tab[i] = int( tab[i] )
	return tab

def get_port():
	"""Fonction qui retourne le numéro du port au quel la carte arduino est branché. 

	Le numéro du port est passé en variable global au début de ce programme, entre autre cette fonction permet
	d'avoir à modifier juste le numéro du port dans ce programme pour qu'il soit répercuté sur les autres.

	Return:
		no_port_arduino(int): 

	"""
	return no_port_arduino

def get_baud():
	"""Fonction qui retourne le débit de communication du port série entre la carte arduino et la raspberry. 

	Le débit de communication est passé en variable global au début de ce programme, entre autre cette fonction permet
	d'avoir à modifier juste le débit dans ce programme pour qu'il soit répercuté sur les autres.

	Return:
		baud_arduino(int): 

	"""
	return baud_arduino

def get_encoding():
	"""Fonction qui retourne l'encodage utilisé sur le port série entre la carte arduino et la raspberry. 

	L'encodage utilisé est passé en variable global au début de ce programme, entre autre cette fonction permet
	d'avoir à modifier juste le type d'encodage dans ce programme pour qu'il soit répercuté sur les autres.

	Return:
		encoding_arduino(String): 

	"""
	return encoding_arduino

def read_serial( ser ):
	"""Fonction prévu initialement pour lire les message envoyé par la carte arduino sur le port série. 

	Cette solution était prévu pour être plus robuste qu'un ser.readline(), et retourne directement un tableau 
	avec les différentes informations envoyé par la carte arduino.
	En effet, cette fonction s'assure tout d'abord d'avoir un message commencant par "$INFO", puis une fois la bonne
	ligne reçu elle la confit à la fonction decoding qui lui retourne un tableau contenant les informations. 
	Et pour finir elle s'assure que les informations sont correcte avec la fonction requirement.

	Args:
		serial(objet): 

	Return:
		tab(array): 	tab[0] = $INFO
				tab[1]-> is the number of this message and matches of number of messages send by Arduino from the beginning
				tab[2]-> Propeller_babore value read 
				tab[3]-> Propelle_tribore value read
				tab[4]-> Propeller_front value read
				tab[5]-> Propeller_rear value read
				tab[6]-> State_propellers
				tab[7]-> External_pressure
				tab[8]-> Mission_departure
				tab[9]-> Azimuth
				tab[10]-> Pitch Angle
				tab[11]-> Roll Angle
				tab[12]-> Temperature on SEAL

	"""
	bit=ser.readline()
	toto=str(bit)
	while ( toto.find("$INFO") == -1 ):
		bit=ser.readline()
		toto=str(bit)

	tab=decoding(bit)
	while tab[0] !="$INFO"  and requirement(tab) == False:
		bit=ser.readline()
		tab=decoding(bit)
	print(tab)
	return tab
	
def decoding_joy(bit) :
	"""Function for decoding bytes from joystick.

	This function convert bytes on string and split on array after each ",".
	Them each value for propellers is adjust because the bottoms and the joystick on neutral position are not at zero.
	And finaly, each value is adjust for each propellers, because they are not same rotation sense and the lateral propellers
	must be adapted with joystick.

	Args:
		bits(byte): bytes from joystick 

	Return:
		tab(array): 	tab[0] = $JOY
				tab[1]-> Propeller_babore
				tab[2]-> Propelle_tribore 
				tab[3]-> Propeller_front 
				tab[4]-> Propeller_rear

	"""
	toto=str(bit)
	toto=toto[  toto.index("$JOY") : toto.index("*") ]
	tab = toto.split(',' , 13 )
<<<<<<< HEAD
	#First process
=======
	#for i in range (1,len(tab)) :
	#	if isinstance( tab[i] , int) == True :
	#		tab[i] = int( tab[i] )
>>>>>>> origin/master
	tab[1] = max( [ int( tab[1] ) - 5, -100 ] )
	tab[2] = max( [ int( tab[2] ) - 2, -100 ] )
	tab[3] = max( [ int( tab[3] ) - 5, -100 ] )
	tab[4] = max( [ int( tab[4] ) - 5, -100 ] )
<<<<<<< HEAD
	#Second process
	tab[1] = max( [ min ( [( int( tab[1] ) - int( tab[2] ) ) , 100 ]) , -100 ] )
	tab[2] = - max( [ min ( [( int( tab[1] ) + int( tab[2] ) ) , 100 ]) , -100 ] )
	tab[3] = -int( tab[4] )
	tab[4] = int( tab[4] )
=======
>>>>>>> origin/master
	return tab
		
