# SEAL

## Fonctionnment
On peut piloter le robot SEAL en ligne de commande depuis un terminal. Ou à l'aide du joystick.

En ligne de commande, il suffit de se brancher à celui-ci en **ssh** puis de lancer un terminal **Python3**.
Une fois le fichier **Seal** importé et l'objet **Com()** créer il suffit de lancer l'écriture dans un fichier txt nommé **Seal_Full_State.txt** par la commande suivante
**objet.start()**. Il est important de lancé cette écriture car toutes les fonctionnalités dépendent de ce fichier txt. Il contient tous les messages envoyés sur le port série,
que se soit de la carte Arduino ou de la Raspberry Pi3.

Pour piloter le robot SEAl à l'aide du joystick, il suffit de brancher le joystick à un ordinateur puis ce connecter en **ssh** au SEAL. Puis
il faut lancer le fichier **serveur.py** sur la **Raspberry**, ce fichier ce trouver dans **Documents/SEAL/Python/**; et lancer le fichier **client.py** sur l'ordinateur.
Les propulseurs du robot ne peuvent pas fonctionner tant que la coupille bleu n'est pas retiré, elle se citue à l'arriére du robot.

Le fichier nommé **Seal_Full_State.txt** contient toutes les données qui ont transité sur le port série entre la carte Arduino et la Raspberry Pi3.
Cependant à chaque fois que l'on crée un objet **Com()** et que **objet.start()** est lancé le fichier **Seal_Full_State.txt** est écrassé pour reservoir les nouvelles données.

Les messages de la carte arduino sont de la forme : 
$INFO,#message,Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear, State_propellers ,External_pressure, Mission_departure, Azimuth, Pitch Angle, Roll Angle, Temperature

Les messages de la Raspberry Pi3 doivent commancé par **$** et finir par **\n**. 
$ATACH									-> attacher les pins de commandes des variateurs
$STOP									-> detacher les pins de commandes des variateurs et donc arrêter les propulseurs
$INIT									-> initialiser les variateurs en cas de blocage de ceux-ci
$PRO, babore value, tribore value, front value, rear value		-> ordonner les valeurs de propulsion pour chaque propulseur (entre -100 et 100)

## Utulisation

###Dans un terminal **Python3** voici les différentes commandes possibles,
###mais avant tout il est nécessaire d'éxcuter c'est trois premiéres lignes.
```python
from Seal import*	#importer toutes les fonctionnalitées
s=Com()			#créer un objet Com
s.start()		#lancer le thread pour l'écriture du fchier txt
```

###Voici les autres commandes disponible:
```python
s.show()			#permet de lire le dernier message envoyé par la carte arduino
s.atach()			#permet d'attacher les pins de commande des variateurs, il est important de le faire avant d'envoyer un ordre de propulsion
s.propellers(20,20,20,20)	#ordre de propulsion chaque valeur doit être comprise entre -100 et 100
s.close()			#permet de terminer le programme ainsi que détacher les pins des propulseurs et fermer le port série.
```
