#include <LiquidCrystal.h>
LiquidCrystal lcd(44, 45, 46, 47, 48, 49); // LCD 연결

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2); // LCD 크기 설정
  lcd.clear(); // LCD 화면 지우기
}


void loop()
{
  int Read_temp = analogRead(A1);
  float temp_voltage = Read_temp * 5.0 / 1024.0;
  float temp_C = temp_voltage * 100.0;
  lcd.print("Temp C ");
  lcd.setCursor(7, 0);
  lcd.print(temp_C);

  // Display Light on second row
  int Read_light = analogRead(A2);
  lcd.setCursor(0, 1);
  lcd.print("Light "); 
  lcd.setCursor(6, 1);
  lcd.print(Read_light);
  delay(1000);
  lcd.clear(); // LCD 화면 지우기
}
