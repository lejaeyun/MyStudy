#include <SoftwareSerial.h>
SoftwareSerial mySerial(4,5);
int button_pin = A0;
boolean previous_state= false;

void setup() {
  mySerial.begin(9600);     // 메가2560(2번)과의 시리얼 연결
  Serial.begin(9600);   // 컴퓨터와의 시리얼 연결
  pinMode(button_pin, INPUT);
}

void loop() {
  int state = analogRead(button_pin);
  float temp_voltage = Read_temp * 5.0 / 1024.0;
  float temp_C = temp_voltage * 100.0;  
  String Send = String(temp_C) + "\n";
  mySerial.print(Send);
  Serial.print("Send Temp C : ");
  Serial.println(temp_C);
  delay(1000)
}
