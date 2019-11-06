int pin_LED = 13; // LED 연결 핀
unsigned long time_previous, time_current;
unsigned long interval = 1000; // 점멸 간격
boolean LED_state = false; // LED 상태

void setup() {
  pinMode(A0, INPUT);
  pinMode(pin_LED, OUTPUT);
  digitalWrite(pin_LED, LED_state);
  Serial.begin(9600);
  time_previous = millis(); // 현재 시간
}
void loop() {
  time_current = millis();
  if (time_current - time_previous >= interval) {
    Serial.print("Current interval is ");
    Serial.print(interval);
    Serial.println(" ms.");
    time_previous = time_current;
    LED_state = !LED_state;
    digitalWrite(pin_LED, LED_state);
  }
  int adc = analogRead(A0);
  Serial.print(adc);
  delay(100);
  Serial.println();
  interval = map(adc, 0, 1023, 500, 1500);
}
