#include <LiquidCrystal.h>
// 핀 번호 (RS, E, DB4, DB5, DB6, DB7)
LiquidCrystal lcd(44, 45, 46, 47, 48, 49); // LCD 연결

// 사용자 정의 문자 데이터
byte user1[8] = {
  B00000, B10001, B00000, B00000, B10001, B01110, B00000, B00000
};
byte user2[8] = {
  B00000, B10001, B01010, B10001, B00000, B10001, B01110, B00000
};

void setup() {
  lcd.createChar(0, user1); // 사용자 정의 문자 1 생성
  Serial.print("1");
  lcd.createChar(1, user2); // 사용자 정의 문자 2 생성
  Serial.print("2");
  lcd.begin(16, 2); // LCD 크기 설정
  Serial.print("3");
  lcd.clear(); // LCD 화면 지우기
  Serial.print("4");
  lcd.write(byte(0)); // 사용자 정의 문자 1 출력
  Serial.print("5");
  lcd.setCursor(0, 1); // 두 번째 행으로 이동
  Serial.print("6");
  lcd.write(byte(1)); // 사용자 정의 문자 2 출력
  Serial.print("7");
}

void loop() {
}
