#include <LiquidCrystal.h>
int SEGMENT_DELAY = 5;
int Button = 14;
byte patterns[] = { 0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0xBE, 0xE4, 0xFE, 0xE6 };
int digit_select_pin[] = {66, 67, 68, 69};
int segment_pin[] = {58, 59, 60, 61, 62, 63, 64, 65};

void setup()
{
  Serial.begin(9600);
  pinMode(Button, INPUT);
  for(int i = 0; i < 8; i++){
    pinMode(segment_pin[i],OUTPUT);
  }
  for(int i = 0; i < 4; i++){
    pinMode(digit_select_pin[i],OUTPUT);
  }
}

void show_digit(int pos, int number) {
  for (int i = 0; i < 4; i++) {
    if (i + 1 == pos)
      digitalWrite(digit_select_pin[i], LOW);
    else
      digitalWrite(digit_select_pin[i], HIGH);
  }
  for (int i = 0; i < 8; i++) {
    boolean on_off = bitRead(patterns[number], 7 - i);
    digitalWrite(segment_pin[i], on_off);
  }
}

void show_4_digit(int number) {  
  number = number % 1000;       // 4자리로 제한
  int hundreads = number / 100;  // 백 자리
  number = number % 100;
  int tens = number / 10;        // 십 자리
  int ones = number % 10;        // 일 자리
  show_digit(2, hundreads);
  delay(SEGMENT_DELAY);
  show_digit(3, tens);
  delay(SEGMENT_DELAY);
  show_digit(4, ones);
  delay(SEGMENT_DELAY);
}

int time_previous , time_current, seconds = 0, minutes = 0;
bool bef_but = 0, now_but = 0,reverse = false;
void loop() {
  bef_but = now_but;
  now_but = digitalRead(Button);
  if (bef_but != now_but and now_but == 1)
  {
    reverse = !reverse;
  }
  
  time_current = millis();
  if (time_current - time_previous >= 1000) {
    time_previous = time_current;
    if (reverse == false)
      seconds++;
    else
      seconds--;
    if (seconds == -1) { // 60초가 되면 분 증가
      seconds = 999;
    }
  }
  show_4_digit(seconds); // 시간 표시를 위해 4자리 숫자로 만듦
}
