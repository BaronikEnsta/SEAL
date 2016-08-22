# SEAL

## Fonctionnment
On peut piloter le robot SEAL en ligne de commande depuis un terminal.
Pour cela il suffit de se brancher à celui-ci en **ssh** puis de lancer un terminal **Python3**.
Une fois le fichier **Seal** importé et l'objet **Com()** créer il suffit de lancer l'écriture dans un fichier txt nommé **Seal_Full_State.txt** par la commande suivante
**objet.start()**. Il est important de lancé cette écriture car toutes les fonctionnalités dépendent de ce fichier txt. Il contient tous les messages envoyés sur le port série,
que se soit de la carte Arduino ou de la Raspberry PI3. 

Les messages de la carte arduino sont de la forme : 
$INFO,#message,Propeller_babore, Propeller_tribore, Propeller_front, Propeller_rear, State_propellers ,External_pressure, Mission_departure, Azimuth, Pitch Angle, Roll Angle, Temperature

Les messages de la Raspberry PI3 doivent commancé par **$** et finir par **\n**. 
$ATACH													-> attacher les pins de commandes des variateurs
$STOP													-> detacher les pins de commandes des variateurs et donc arrêter les propulseurs
$INIT													-> initialiser les variateurs en cas de blocage de ceux-ci
$PRO, babore value, tribore value, front value, rear value		-> ordonner les valeurs de propulsion pour chaque propulseur (entre -100 et 100)

## Utulisation

###Dans un terminal **Python3** voici les différentes commandes possibles,
###mais avant tout il est nécessaire d'éxcuter c'est trois premiéres lignes.
```python
from Seal import*	#importer toutes les fonctionnalitées
s=Com()				#créer un objet Com
s.start()				#lancer le thread pour l'écriture du fchier txt
```

###Voici les autres commandes disponible:
```python
s.show()
s.atach()
s.show()
s.propellers(20,20,20,20)
s.show
s.propellers(0,0,0,0)
s.show
s.detach()
s.close()
```
