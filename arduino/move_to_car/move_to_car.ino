int vel = 200;
int velG = 150;

#define PwmI 5
#define PwmD 6
#define LlantaIT 8
#define LlantaID 9
#define LlantaDT 10
#define LlantaDD 11

void setup() {
  Serial.begin(9600);
  pinMode(LlantaIT,OUTPUT);
  pinMode(LlantaID,OUTPUT);
  pinMode(LlantaDT,OUTPUT);
  pinMode(LlantaDD,OUTPUT);
}

void loop() {
  while(Serial.available()>0){

    char date = Serial.read();
    Serial.print(date);
    //condition move
    //izq delante, izq tracera, der delante, der tracera, vel izq, vel der
    switch(date){
      case '0':{
        moveCar(false,false,false,false,0,0);
        Serial.println("0");
        break;
      }
      case '1':{
       moveCar(true,false,false,true,vel,vel);
        Serial.println("1");
        break;
      }
      case '2':{
         moveCar(false,true,false,true,velG,vel);
        Serial.println("2");
        break;
      }
      case '3':{
        //frente
        moveCar(false,true,false,true,vel,vel);
        Serial.println("3");
        break;
      }
      case '4':{
        moveCar(false,true,false,true,vel,velG);
        Serial.println("4");
        break;
      }
      case '5':{
        moveCar(false,true,true,false,vel,vel);
        Serial.println("5");
        break;
      }
      case '6':{
        moveCar(true,false,true,false,vel,velG);
        Serial.println("6");
        break;
      }
      case '7':{
        moveCar(true,false,true,false,vel,vel);
        Serial.println("7");
        break;
      }
      case '8':{
        moveCar(true,false,true,false,velG,vel);
        Serial.println("8");
        break;
      }
      default:{
        Serial.println("0");
        break;
      }
    }
    
  }
}

void moveCar(bool l1,bool l2,bool l11,bool l22, int vel1,int vel2){
   digitalWrite(LlantaID,l1);
   digitalWrite(LlantaIT,l11);
   analogWrite(PwmI,vel1);

   digitalWrite(LlantaDD,l2);
   digitalWrite(LlantaDT,l22);
   analogWrite(PwmD,vel2);
  
}
