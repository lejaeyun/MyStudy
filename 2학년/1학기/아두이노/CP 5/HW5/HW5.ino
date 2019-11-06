int pins_LED[] = {2, 3, 4, 5}; // LED 연결 핀
int led_value[4] = {0, 63, 127, 191};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(pins_LED[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) 
  {
    Serial.print(String(led_value[i]) + ", ");
    analogWrite(pins_LED[i], led_value[i]); // LED 밝기 조절
    led_value[i] = led_value[i] + 1;
    if (led_value[i] == 256)
    {
      led_value[i] = 0 ;
    }
  }
  Serial.println();
}
