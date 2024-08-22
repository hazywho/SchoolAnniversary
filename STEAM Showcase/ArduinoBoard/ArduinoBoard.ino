String serialData;

void setup(){
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT); 
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(28, OUTPUT);
  pinMode(29, OUTPUT);
  pinMode(30, OUTPUT);
  pinMode(31, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(34, OUTPUT);
  pinMode(35, OUTPUT);
  pinMode(36, OUTPUT);
  pinMode(37, OUTPUT);
  pinMode(38, OUTPUT);
  pinMode(39, OUTPUT);
  pinMode(40, OUTPUT);
  pinMode(41, OUTPUT);
  pinMode(42, OUTPUT);
  pinMode(43, OUTPUT);
  pinMode(44, OUTPUT);
  pinMode(45, OUTPUT);
  pinMode(46, OUTPUT);
  pinMode(47, OUTPUT);
  pinMode(48, OUTPUT);
  pinMode(49, OUTPUT);
  pinMode(50, OUTPUT);
  pinMode(51, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop()
{
  if(Serial.available()){
    serialEvent();   
  }
}
int switch1=0; 
int switch2=0; 
int switch3=0;
int switch4=0; 
int switch5=0; 
int switch6=0; 
int switch7=0; 
int switch8=0; 
int switch9=0; 
int switch10=0; 
int switch11=0;
int switch12=0;  
int switch13=0; 
int switch14=0; 
int switch15=0; 
int switch16=0; 
int switch17=0; 
int switch18=0; 
int switch19=0; 
int switch20=0; 
int switch21=0; 
int switch22=0; 
int switch23=0; 
int switch24=0; 
int switch25=0; 
int switch26=0;
int switch27=0; 
int switch28=0; 
int switch29=0; 
int switch30=0; 
int switch31=0; 
int switch32=0; 
int switch33=0; 
int switch34=0; 
int switch35=0; 
int switch36=0; 


void serialEvent() {
  serialData = Serial.readString();
  if(serialData.toInt()==11){if(switch1==0){digitalWrite(26,HIGH); switch1=1;}else{digitalWrite(26,LOW); switch1=0;}}      
  
  if(serialData.toInt()==16){if(switch2==0){digitalWrite(27,HIGH); switch2=1;}else{digitalWrite(27,LOW); switch2=0;}}      
  
  if(serialData.toInt()==15){if(switch3==0){digitalWrite(24,HIGH); switch3=1;}else{digitalWrite(24,LOW); switch3=0;}}      
  
  if(serialData.toInt()==14){if(switch4==0){digitalWrite(25,HIGH); switch4=1;}else{digitalWrite(25,LOW); switch4=0;}}      
  
  if(serialData.toInt()==13){if(switch5==0){digitalWrite(22,HIGH); switch5=1;}else{digitalWrite(22,LOW); switch5=0;}}      
  
  if(serialData.toInt()==12){if(switch6==0){digitalWrite(23,HIGH); switch6=1;}else{digitalWrite(23,LOW); switch6=0;}}      
  
  if(serialData.toInt()==21){if(switch7==0){digitalWrite(32,HIGH); switch7=1;}else{digitalWrite(32,LOW); switch7=0;}}      
  
  if(serialData.toInt()==26){if(switch8==0){digitalWrite(33,HIGH); switch8=1;}else{digitalWrite(33,LOW); switch8=0;}}      
  
  if(serialData.toInt()==25){if(switch9==0){digitalWrite(30,HIGH); switch9=1;}else{digitalWrite(30,LOW); switch9=0;}}      
  
  if(serialData.toInt()==24){if(switch10==0){digitalWrite(31,HIGH); switch10=1;}else{digitalWrite(31,LOW); switch10=0;}}  
  
  if(serialData.toInt()==23){if(switch11==0){digitalWrite(28,HIGH); switch11=1;}else{digitalWrite(28,LOW); switch11=0;}}  
  
  if(serialData.toInt()==22){if(switch12==0){digitalWrite(29,HIGH); switch12=1;}else{digitalWrite(29,LOW); switch12=0;}}  
  
  if(serialData.toInt()==31){if(switch13==0){digitalWrite(38,HIGH); switch13=1;}else{digitalWrite(38,LOW); switch13=0;}}  
  
  if(serialData.toInt()==36){if(switch14==0){digitalWrite(39,HIGH); switch14=1;}else{digitalWrite(39,LOW); switch14=0;}}  
  
  if(serialData.toInt()==33){if(switch15==0){digitalWrite(34,HIGH); switch15=1;}else{digitalWrite(34,LOW); switch15=0;}}  
  
  if(serialData.toInt()==34){if(switch16==0){digitalWrite(37,HIGH); switch16=1;}else{digitalWrite(37,LOW); switch16=0;}}  
  
  if(serialData.toInt()==35){if(switch17==0){digitalWrite(36,HIGH); switch17=1;}else{digitalWrite(36,LOW); switch17=0;}}  
  
  if(serialData.toInt()==32){if(switch18==0){digitalWrite(35,HIGH); switch18=1;}else{digitalWrite(35,LOW); switch18=0;}}  
  
  if(serialData.toInt()==41){if(switch19==0){digitalWrite(44,HIGH); switch19=1;}else{digitalWrite(44,LOW); switch19=0;}}  
  
  if(serialData.toInt()==46){if(switch20==0){digitalWrite(45,HIGH); switch20=1;}else{digitalWrite(45,LOW); switch20=0;}}  
  
  if(serialData.toInt()==45){if(switch21==0){digitalWrite(42,HIGH); switch21=1;}else{digitalWrite(42,LOW); switch21=0;}}  
  
  if(serialData.toInt()==44){if(switch22==0){digitalWrite(43,HIGH); switch22=1;}else{digitalWrite(43,LOW); switch22=0;}}  
  
  if(serialData.toInt()==43){if(switch23==0){digitalWrite(40,HIGH); switch23=1;}else{digitalWrite(40,LOW); switch23=0;}}  
  
  if(serialData.toInt()==42){if(switch24==0){digitalWrite(41,HIGH); switch24=1;}else{digitalWrite(41,LOW); switch24=0;}}  
  
  if(serialData.toInt()==51){if(switch25==0){digitalWrite(50,HIGH); switch25=1;}else{digitalWrite(50,LOW); switch25=0;}}  
  
  if(serialData.toInt()==56){if(switch26==0){digitalWrite(51,HIGH); switch26=1;}else{digitalWrite(51,LOW); switch26=0;}}  
  
  if(serialData.toInt()==55){if(switch27==0){digitalWrite(48,HIGH); switch27=1;}else{digitalWrite(48,LOW); switch27=0;}}  
  
  if(serialData.toInt()==54){if(switch28==0){digitalWrite(49,HIGH); switch28=1;}else{digitalWrite(49,LOW); switch28=0;}}  
  
  if(serialData.toInt()==53){if(switch29==0){digitalWrite(46,HIGH); switch29=1;}else{digitalWrite(46,LOW); switch29=0;}}  
  
  if(serialData.toInt()==52){if(switch30==0){digitalWrite(47,HIGH); switch30=1;}else{digitalWrite(47,LOW); switch30=0;}}  
  
  if(serialData.toInt()==61){if(switch31==0){digitalWrite(4,HIGH); switch31=1;}else{digitalWrite(4,LOW); switch31=0;}}  
  
  if(serialData.toInt()==62){if(switch32==0){digitalWrite(9,HIGH); switch32=1;}else{digitalWrite(9,LOW); switch32=0;}}  
  
  if(serialData.toInt()==63){if(switch33==0){digitalWrite(8,HIGH); switch33=1;}else{digitalWrite(8,LOW); switch33=0;}}    
  
  if(serialData.toInt()==64){if(switch34==0){digitalWrite(7,HIGH); switch34=1;}else{digitalWrite(8,LOW); switch34=0;}}    
  
  if(serialData.toInt()==65){if(switch35==0){digitalWrite(6,HIGH); switch35=1;}else{digitalWrite(6,LOW); switch35=0;}}    
  
  if(serialData.toInt()==66){if(switch36==0){digitalWrite(5,HIGH); switch36=1;}else{digitalWrite(5,LOW); switch36=0;}}

  if(serialData.toInt()==99){
    digitalWrite(,LOW)
  }
  }
