#include <Servo.h> 

Servo servo1;
Servo servo2;
String serialData;

void setup(){
  Serial.begin(115200);
  servo1.attach(9);
  servo2.attach(10);
}

void loop()
{ }

void serialEvent() {
  serialData = Serial.readString();
  servo1.write(parseX(serialData));
  servo2.write(parseY(serialData));
}

int parseX(String data) {
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseY(String data) {
  data.remove(0, data.indexOf("Y") + 1);
  return data   .toInt();
}
