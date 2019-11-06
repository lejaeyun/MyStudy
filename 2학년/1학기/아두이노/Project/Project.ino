int pump = 7;
int mud_pin = A1;
int analogPin = A0;
int val, sensorVal,vval;
int speakerPin = A2;

#include <LiquidCrystal.h>
LiquidCrystal lcd(24, 25, 26, 27, 28, 29); // LCD 연결

void setup()
{
  Serial.begin (9600); 
  pinMode(pump, OUTPUT);
  digitalWrite(pump, HIGH);
  lcd.begin(16, 2); // LCD 초기화
  lcd.clear();
}
 
void loop()
{
  delay(2000);
  
  val = analogRead(analogPin);
  sensorVal = analogRead(mud_pin);
  Serial.println(val);
  Serial.println(sensorVal);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Water   Humidity");
  lcd.setCursor(0,1);
  vval = map(val, 0, 1024, 0, 8);
  for(int i = 0; i < vval; i++){
     lcd.setCursor(i,1);
     lcd.write(B11111111);
  }
  
  vval = map(sensorVal, 0, 100, 0, 8);
  for(int i = 0; i < vval; i++){
     lcd.setCursor(i+8,1);
     lcd.write(B11111111);
  }

  if (val <= 300){
    tone(speakerPin, 392, 500);
    delay(700);
    return 0;
  }
  else {
    noTone(speakerPin);
  }
  
  if (sensorVal <= 20) {
    digitalWrite(pump, LOW);
    delay(500);
    digitalWrite(pump, HIGH);
  }
}
