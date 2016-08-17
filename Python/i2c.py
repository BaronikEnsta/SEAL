import smbus as smbus
import time

#remplacer  0 par 1 si nouveau Raspberry
deltasting = [0x68,0x69,0x6a,0x06b,0x6c,0x6d,0x6e,0x6f]
config_byte = 0x1c 

bus = smbus.SMBus()
adress = 0x12

print( "envoi de la valeur 3")
bus.write_word_data(adress, 3)
#bus.write_bytes(adress, 3)
#bus.write_bytes(deltasting[0], config_byte)
# pause de 1 seconde pour laisser le time au traitement de se faire
time.sleep(1)
reponse = bus.read_bytes(adress)
print("la reponse de l'arduino :  " + reponse)
