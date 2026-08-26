// C++ code
/*
Name:Thejas Shetty
ID: 2026B5PS1257H
*/
#include<LiquidCrystal.h>

int led=13;
int pb=12;
int lcd3=11;
int lcdrs=10;
int db7=5;
int db6=4;
int db5=3;
int db4=2;
int dsts=9; //for distance sensor
int buzz=6;

int pht=A0;
LiquidCrystal lcd(10,11,2,3,4,5);

unsigned long sstrt=0UL;
unsigned long cstrt=0UL;

void setup()
{
  pinMode(13, OUTPUT);//LED
  pinMode(12, INPUT);//PUSHBUTTON
  pinMode(11, OUTPUT);//LCD 3
  pinMode(10, OUTPUT);//LCD RS
  pinMode(5, OUTPUT);//LCD DB7
  pinMode(4, OUTPUT);//LCD DB6
  pinMode(3, OUTPUT);//LCD DB5
  pinMode(2, OUTPUT);//LCD DB4
  //pinMode(9, INPUT);//distance sensor 3pin
  pinMode(6, OUTPUT); //BUZZER
  lcd.begin(16,2);
  lcd.setCursor(0,0);
}
int mode=0;
float dst=0;
bool sstarted=false;
bool cstarted=false;
void loop()
{
  int brightness=analogRead(pht);
  pinMode(dsts, OUTPUT);
  digitalWrite(dsts, HIGH);
  delayMicroseconds(5);
  digitalWrite(dsts,LOW);
  pinMode(dsts, INPUT);
  unsigned long t=pulseIn(dsts,HIGH, 15000);
  dst=(t)*0.0343/2.0;
  //lcd.begin(16,2);
  const char *modes[]={"OPEN SEA        ","ANCHOR DROPPED      ",
                       "WRECKED         ",
                       "STORM                ","CHARYBDIS       "};
  if (digitalRead(pb)==HIGH && mode !=2)
  {
    lcd.setCursor(0,0);
    //lcd.print("BUTTON PRESSED      ");//idk man when i remove this lcd part it wasn't working this reminds me of that coconut thing though it was false..nvm figured it out
    delay(250);
    if (mode==1) mode=0;//OPEN SEA
    else
    {
      mode=1;//ANCHOR DROPPED
      cstarted=false;
      sstarted=false;
      digitalWrite(buzz,LOW);
      digitalWrite(led,LOW);
    }
  }

  else
  {
    if (mode!=2 && mode!=1)
    {
      //mode=0;//OPEN SEA
      if (brightness<512 && mode!=1 && mode!=2 && mode!=4)
      {
        if (mode==3 && sstarted==true)
        {
          unsigned long now=millis();
          if (now-sstrt>5000)
          {
            mode=2;//WRECKED
          }
        }
        if (sstarted==false) sstrt=millis();
        if (mode!=2 && mode!=1)//added this before modifying upper if, equivalent to if true
        {
        	
        	mode=3;//STORM
            if (millis()%1000>100)digitalWrite(13, HIGH);
            // FLASH (this part was sample code that was here from the start ;) : 
  			//delay(1000); // Wait for 1000 millisecond(s)
  			else digitalWrite(13, LOW);
  			//delay(1000); // Wait for 1000 millisecond(s)
            sstarted=true;
            if (dst>100) 
            {
              digitalWrite(buzz,LOW);
              cstarted=false;
            }
        }
      }
      if (brightness>512 && mode==3)
      {
        mode=0;
        //pinMode(buzz, INPUT);
        //if (false) mode=4;//tried something else here didnt work
        digitalWrite(13, LOW);
        sstarted=false;
      }
      /*float dst=0;/*a quick search told me distance sensors
      are used underwater for ships but this poor sensor might
      get damaged by saltwater so i'll assume we're using it in air
      and won't account for relative motion or wind, if even possible */
      /*pinMode(dsts, OUTPUT);
      digitalWrite(dsts, HIGH);
      delayMicroseconds(5);
      digitalWrite(dsts,LOW);
      pinMode(dsts, INPUT);
      unsigned long dstrt=micros();
      while (digitalRead(dsts)==LOW)
      {
        continue;
      }
      while (digitalRead(dsts)==HIGH)
      {
        continue;
      }
      dend=micros();
      unsigned long t=(dend-dstrt)/2;*/
      /*pinMode(dsts, OUTPUT);
      digitalWrite(dsts, HIGH);
      delayMicroseconds(5);
      digitalWrite(dsts,LOW);
      pinMode(dsts, INPUT);
      unsigned long t=pulseIn(dsts,HIGH, 15000);*/
      //dst=(t)*0.0343/2.0;
      if (dst<100 && dst!=0 && mode!=1 && mode!=3)
      {
        if (mode==4 && cstarted == true)
        {
          unsigned long now=millis();
          if (now-cstrt>5000)
          {
            mode=2;//WRECKED
          }
        }
        if (mode!=2 && mode!=1 && cstarted==false)
        {
            cstarted=true;
        	cstrt=millis();
        	digitalWrite(buzz,HIGH);
            mode=4;//CHARYBDIS
        }
        //if (mode!=2) mode=4;//CHARYBDIS
      }	
    }
    if (dst>100 && mode==4)
    {
      mode=0;
      digitalWrite(buzz,LOW);
      cstarted=false;
    }
    
  }
  if (mode==0 || mode==1)
  {
    digitalWrite(buzz,LOW);
    digitalWrite(led,LOW);
    cstarted=false;
    sstarted=false;
  }
  lcd.setCursor(0,0);
  //lcd.print('                              ');
  lcd.print(modes[mode]);
  //lcd.print(brightness);
}
//idk why but u gotta press the button several times for the anchor dropped/open sea thing to work
//need to make a way to stop timer reset for s and c .... nvm DONE!!! 
