#include <Servo.h>        // servo_moteur.write( angle entre 0 et 180° ) ou servo_moteur.writeMicroseconds(en uS )-> période de 20 mS et analogWrite( pin , value ) -> pas adapté
#include <stdlib.h>



Servo propel_babo;
Servo propel_trib;
Servo propel_fron;
Servo propel_rear;
String consigne="$STOP";                 // $PRO, propel_trib, propel_babo, propel_front, propel_rear    $STOP    $INIT 
String inputString = ""; 
boolean stringComplete = false;
String inputString1 = ""; 
boolean stringComplete1 = false; 
String compassAray[5];
int pression = A5;
int go_mission = A4;
long time = 0;


void setup() {
  Serial.begin(57600);                 // On initialise la connexion 9600
  Serial1.begin(19200);
  pinMode(pression, INPUT);
  pinMode(go_mission, INPUT);
  inputString.reserve(200);
  inputString1.reserve(200);

}

void loop() {
  
  //time = millis();
  
  if (stringComplete1) {
    time += 1;
    Serial.println(info());
  }
  
  delay(10);

  if (stringComplete) {
    inputString.replace("\n", "\0");       // on remplace les retours chariots (touche clavier entrée) par des espaces
    inputString.replace("\r\n", "\0");
    consigne=inputString;
    propulsion(consigne);                //                                                                             $PRO,-45,10,100,-60
    //Serial.println(inputString);
    
    inputString = "";                      // clear the string:
    stringComplete = false;                // remet la condition à false
    }
}


//Fonction qui gére tous les cas pour la propulsion
void propulsion(String consigne) {

  if( consigne.charAt(0)=='$' && consigne.charAt(1)=='S' && consigne.charAt(2)=='T' && consigne.charAt(3)=='O' && consigne.charAt(4)=='P' ){
    lock(propel_babo);
    lock(propel_trib);
    lock(propel_fron);
    lock(propel_rear);
    }
  else if( consigne.charAt(0)=='$' && consigne.charAt(1)=='I' && consigne.charAt(2)=='N' && consigne.charAt(3)=='I' && consigne.charAt(4)=='T' ) {
    unlock(propel_babo);
    unlock(propel_trib);
    unlock(propel_fron);
    unlock(propel_rear);
    }
  else if( consigne.charAt(0)=='$' && consigne.charAt(1)=='A' && consigne.charAt(2)=='T' && consigne.charAt(3)=='A' && consigne.charAt(4)=='C' && consigne.charAt(5)=='H') {
    propel_babo.attach(8);               // propuleseur numero 1
    propel_trib.attach(9);               // propuleseur numero 2
    propel_fron.attach(10);              // propuleseur numero 3
    propel_rear.attach(11);              // propuleseur numero 4
    delay(500);
    }
  else if ( consigne.charAt(0)=='$' && consigne.charAt(1)=='P' && consigne.charAt(2)=='R' && consigne.charAt(3)=='O' /*&& analogRead(go_mission)!= 0 */)   {   //(consigne == "$PRO" et go_mission)
    int tableau[]={0,0,0,0};
    int taille=4;
    if ( extraction(consigne,tableau,taille) == true ){ // pas de problème      
      propel_babo.writeMicroseconds(tableau[0]);
      propel_trib.writeMicroseconds(tableau[1]);
      propel_fron.writeMicroseconds(tableau[2]);
      propel_rear.writeMicroseconds(tableau[3]);         
      }
    else if ( extraction(consigne,tableau,taille) != true ) {
      //consigne="$STOP";
      neutral(propel_babo);
      neutral(propel_trib);
      neutral(propel_fron);
      neutral(propel_rear);
      }                                                                                                               
  }
  else {
    neutral(propel_babo);
    neutral(propel_trib);
    neutral(propel_fron);
    neutral(propel_rear);
    }
}

//Fonction reception des caractéres sur le port USB
void serialEvent(){
  while( Serial.available() && stringComplete == false ) {     // tant que des caractéres sont disponible
  //Serial.println("while serial event");
    char inChar = (char)Serial.read();          // get the new byte:
    //Serial.println(inChar);
    inputString += inChar;                      // add it to the inputString:
    if (inChar == '\n' || inChar == '\r\n' )  {       // if the incoming character is a newline, set a flag
      Serial.println(inputString);
      int index = inputString.indexOf('$');
      //Serial.println("index du $  ");Serial.println(index);
      inputString=inputString.substring(index);
      stringComplete = true;                    // so the main loop can do something about it:                                                      $PRO,-45,10,100,-60
      break;
    }
  }
  Serial.print("j'ai recu ca -> ");Serial.println(inputString);
  //Serial.println(stringComplete); 
}

//Fonction reception des données de OS5000 Compass sur le port Serial1
void serialEvent1(){
  while(Serial1.available() ) {     // tant que des caractéres sont disponible
  //Serial.println("while serial event");
    char inChar1 = (char)Serial1.read();          // get the new byte:
    //Serial.println(inChar1);
    inputString1 += inChar1;                      // add it to the inputString:
    if (inChar1 == '*' /*|| inChar1 == '\r\n' || inChar1 == '\r'*/)  {       // if the incoming character is a newline, set a flag
      int index1 = inputString1.indexOf('$');
      //Serial.println("index du $  ");Serial.println(index);
      inputString1=inputString1.substring(index1);
      stringComplete1 = true;                    // so the main loop can do something about it:                                                      $PRO,-45,10,100,-60
      break;
    }
  } 

}

//Fonstion de déblocage du variateur
void unlock(Servo propel) {
  int i=0;
  while(i<1) {
    propel.writeMicroseconds(2000);
    delay(250);
    propel.writeMicroseconds(1500);
    //delay(250);
    i++;
  }
  //Serial.println("Propeller Initiated"); 
}

//Fonction qui permet de mettre le variateur rokraft en pause. ATTENTION : PLUS DE COUPLE APPLIQUE SUR LES HELICES
void lock(Servo propel) {
  propel.writeMicroseconds(1500);
  propel.detach();
  //delay(100); 
  //Serial.println("Propeller STOPPED"); 
}

//Fonction qui permet de mettre le variateur rokraft au neutre. ATTENTION : TOUJOURS DU COUPLE APPLIQUE SUR LES HELICES
void neutral(Servo propel) {
  propel.writeMicroseconds(1500); 
  //Serial.println("Propeller NEUTRALISED"); 
}  

//Fonction qui permet de returner un tableau de int des valeurs pour chaque propulseur à partir des message reçu type: $PRO,-45,100,-100,0
bool extraction(String consigne, int tableau[], int taille) {
  //Serial.println("PB D'EXTRACTION");
  char paramChar[consigne.length()+1];                 // tableau de char de la taille du String param+1 (caractère de fin de ligne) 
  consigne.toCharArray(paramChar,consigne.length()+1); // récupère le param dans le tableau de char  
  //Serial.println(paramChar);                         // affiche le tableau de char
  char dlm[] = ",";                                    // delimiteur
  int cnt = 0;                                         // compteur
  char* tab[5] = { 0 };                                // tableau avec nos différente valeur
  char *pch = strtok(paramChar, dlm);                  // strtok insére des retour chariot "\0" à la place de dlm dans paramChar
  while ( pch != NULL ) {
            if (cnt < 10) {
                tab[cnt++] = pch;
            } else {
                break;
            }
            pch = strtok (NULL, dlm);
        }
   //Serial.println(cnt); Serial.println(sizeof(tab)); 
   //Serial.println("final");
   //Serial.print(tab[1]);Serial.print("  ");Serial.print(tab[2]);Serial.print("  ");Serial.print(tab[3]);Serial.print("  ");Serial.println(tab[4]);       // $PRO,-45,100,-100,0
   tableau[0]= atoi(tab[1]);                      // atoi -> converts the string argument to an integer (type int)
   tableau[1]= atoi(tab[2]);
   tableau[2]= atoi(tab[3]);
   tableau[3]= atoi(tab[4]);
   for (int i=0; i <= 3; i++){
    //Serial.println(tab[i+1]);
    if (tableau[i]>=-100 && tableau[i]<=100 && cnt==5 ) { // cnt==5 permet de vérifier qu'il y a que l'identifient et les 4 valeurs de propulsion -> $PRO/ propel_trib/ propel_babo/ propel_front/ propel_rear
      if (tableau[i]<0) {
        tableau[i]=map(tableau[i], -100, 0, 1000, 1500);  // Re-maps a number from one range to another -> map(value, fromLow, fromHigh, toLow, toHigh)
      }
      else if (tableau[i]>0) {
        tableau[i]=map(tableau[i], 0, 100, 1500, 2000);       
      }
      else if (tableau[i]==0 && *tab[i+1]=='0') {
        tableau[i]=1500;        
      }
      else if (tableau[i]<-100 || tableau[i]>100 ){
        return false;
      }   
    }
    else {
      return false;
    } 
   }
   for (int i=0; i <= 3; i++){
    if (tableau[i]==0){
      return false;
    }
   }
   return true;    
}

//Fonction qui permet de returner un tableau de int des valeurs pour chaque propulseur à partir des message reçu type: $PRO,-45,100,-100,0
bool compass(String consigne, String tableau[]) {   // float tableau[]
  //Serial.println("je rentre dans compass()");
  /*char tabl[2];
  consigne.substring(consigne.indexOf('*')+1).toCharArray(tabl, 3);
  long decimal_answer = strtol(tabl, NULL, 16); 
  Serial.print("sum of the characters between the $ and the * =  ");Serial.println(decimal_answer);
  int nb_char = consigne.indexOf('*')-consigne.indexOf('$');
  Serial.print("sum of the characters between the $ and the * =  ");Serial.println(nb_char);*/
  int index = consigne.indexOf(' ');
  consigne=consigne.substring(index+1);
  char paramChar[consigne.length()+1];                 // tableau de char de la taille du String param+1 (caractère de fin de ligne) 
  consigne.toCharArray(paramChar,consigne.length()+1); // récupère le param dans le tableau de char  
  //Serial.println(paramChar);                         // affiche le tableau de char
  char dlm[] = ",";                                    // delimiteur
  int cnt = 0;                                         // compteur
  char* tab[5] = { 0 };                                // tableau avec nos différente valeur
  char *pch = strtok(paramChar, dlm);                  // strtok insére des retour chariot "\0" à la place de dlm dans paramChar
  while ( pch != NULL ) {
            if (cnt < 10) {
                tab[cnt++] = pch;
            } else {
                break;
            }
            pch = strtok (NULL, dlm);
        }
   //Serial.println(cnt); Serial.println(sizeof(tab)); 
   //Serial.println("final");
   //Serial.print(tab[0]);Serial.print("  ");Serial.print(tab[1]);Serial.print("  ");Serial.print(tab[2]);Serial.print("  ");Serial.print(tab[3]);Serial.print("  ");Serial.println(tab[4]);
   /*tableau[0]= atoi(tab[0]);   // Azimuth                 // atof -> converts the char argument to an float
   tableau[1]= atof(tab[1]);   // Pitch Angle
   tableau[2]= atof(tab[2]);   // Roll Angle
   tableau[3]= atof(tab[3]);   // Temperature*/
   tableau[0]= String(tab[0]);   // Azimuth               
   tableau[1]= String(tab[1]);   // Pitch Angle
   tableau[2]= String(tab[2]);   // Roll Angle
   tableau[3]= String(tab[3]);   // Temperature
   /*for (int i=0; i <= 4; i++){
    //Serial.println(tab[i]);
   }*/
   if ( cnt != 5 ) { // cnt==5 permet de vérifier qu'il y a que l'identifient et les 4 valeurs de propulsion -> $PRO/ propel_trib/ propel_babo/ propel_front/ propel_rear
    //Serial.print("mince"); 
    return false; 
   }
  return true;    
}

//Fonction qui ecrit un message pour le CPU avec les valeurs des propulseurs, du capteur de pression, et du signal de début de mission, type: $INF, propel_trib, propel_babo, propel_front, propel_rear, pression, signal_go
String info() {
  //Serial.println("je rentre dans info()");
  //String compassAray[5];
  String info;
  //Serial.println("je suis dans info() et la seconde boucle");
  int pres = analogRead(pression);
  int go = analogRead(go_mission);      // 1023 -> lancer mission  0 -> interrompre mission
  String p_babo = String(map(propel_babo.read(),44,141,-100,100));
  String p_trib = String(map(propel_trib.read(),44,141,-100,100)); 
  String p_fron = String(map(propel_fron.read(),44,141,-100,100));
  String p_rear = String(map(propel_rear.read(),44,141,-100,100));
  String statue = String(propel_babo.attached()) + String(propel_trib.attached()) + String(propel_fron.attached()) + String(propel_rear.attached());
  
  //Serial.println(stringComplete1);
  if ( stringComplete1 == true ) {  
    if ( compass(inputString1,compassAray) == true ){
      info= "$INFO," + String( time ) + ',' + p_babo + ',' + p_trib + ',' + p_fron + ',' + p_rear + ',' + statue + ',' + String(pres) + ',' + String(go)+ ',' + compassAray[0] + ',' + compassAray[1] + ',' + compassAray[2] + ',' + compassAray[3];                     // $PRO,-45,100,-100,0
      inputString1 = "";                      // clear the string:
      stringComplete1 = false;                // remet la condition à false
      //Serial1.flush();
    }
  }
  else if ( stringComplete1 != true ) {
    info= "$INFO," + String( time ) + ',' + p_babo + ',' + p_trib + ',' + p_fron + ',' + p_rear + ',' +  statue + ',' + String(pres) + ',' + String(go) + ',' + ',' +  ',' + ','  ;
  } 
  //info= "$INFO," + p_babo + ',' + p_trib + ',' + p_fron + ',' + p_rear + ',' + String(pres) + ',' + String(go)+ ',' + ',' +  ',' + ','  ;
  //info= "$INFO," + p_babo + ',' + p_trib + ',' + p_fron + ',' + p_rear + ',' + String(pres) + ',' + String(go) /*+ ',' + compassAray[0] + ',' + compassAray[1] + ',' + compassAray[2] + ',' + compassAray[3] */;
  return info;
}

