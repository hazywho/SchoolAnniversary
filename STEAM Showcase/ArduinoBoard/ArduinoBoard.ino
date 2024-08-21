String serialData;

void setup(){
  Serial.begin(9600);
  Serial.setTimeout(10);
  servo1.attach(9);
  servo2.attach(10);
}

void loop()
{ }

void serialEvent() {
  serialData = Serial.readString();
  x = parseX(serialData);
  y = parseY(serialData);
  
}

int parseX(String data) {
  return data[0].toInt();
}

int parseY(String data) {
  return data[1].toInt();
}
