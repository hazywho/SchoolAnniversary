#include <Servo.h> 

Servo servo1;
Servo servo2;
Servo servoCLAW;
int servoX,servoY=0
int joystickX,joystickY = 0;
int calibrationX,calibrationY = 0;
int button = 0;
int factor = 1;

void setup(){
  servo1.attach(9); //servo1
  servo2.attach(10); //servo2
  servoCLAW.attach(13); //servo3
  calibrationX = analogRead(A0); //controler x pin
  calibrationY = analogRead(A1); //controler y pin
  pinMode(11,INPUT);
}

void loop(){ 
  joystickX = analogRead(A0);
  joystickY = analogRead(A1);
  if(joystickX-calibrationX>=552 && servoX<=180){
    servoX+=round((joystickX-calibrationX-552)/1023*180*factor);
  }
  else if(joystickX-calibrationX<552 && servoX>=0){
    servoX-=round((551-joystickX-calibrationX)/1023*180*factor);
  }
  if(joystickY-calibrationY>=552 && servoY<=180){
    servoY+=round((joystickY-calibrationY-552)/1023*180*factor);
  }
  else if(joysticY-calibrationY<552 && servoY>=0){
    servoY-=round((551-joystickY-calibrationY)/1023*180*factor);
  }
  servo1.write(servoX);
  servo2.write(servoY);
  button = digitalRead(11);
  if(button){
    servoCLAW.write(180);
  }
  else{
    servoCLAW.write(0);
  }
}
