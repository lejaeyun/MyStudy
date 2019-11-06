unsigned long time_previous_arr[2], time_current;
boolean LED_state[2] = {false, false};
int pins_LED[2] = {2,3}, interval_arr[2];

void setup() {
  pinMode(A0, INPUT);
  for (int i = 0; i < 2; i++)
  {
    pinMode(pins_LED[i], OUTPUT);
    digitalWrite(pins_LED[i], LED_state);
    time_previous_arr[i] = millis();
  }
  Serial.begin(9600);
}

void loop() {
  
  int adc = analogRead(A0);
  Serial.println(adc);
  delay(100);
  //interval = map(adc, 0, 1023, 500, 1500)
  interval_arr[0] = map(adc, 0, 1023, 500, 1500);
  interval_arr[1] = map(adc, 0, 1023, 1500, 500);
  
  time_current = millis();
  for (int i = 0; i < 2; i++)
  {
    if (time_current - time_previous_arr[i] >= interval_arr[i]) {
      time_previous_arr[i] = time_current;
      LED_state[i] = !LED_state[i];
      digitalWrite(pins_LED[i], LED_state[i]);
    }
  }
  
}
