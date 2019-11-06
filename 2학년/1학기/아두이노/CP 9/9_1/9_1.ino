int DIR1 = 41;
int PWM1 = 9;
int button_pin = 14;
int direction = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(DIR1, OUTPUT);
  pinMode(PWM1, OUTPUT);
}

void loop() {
  if (digitalRead(button_pin)) {
    direction = !direction;
    if (direction) // clockwise
      Serial.println("Clockwise...");
    else
      Serial.println("Anti-clockwise...");
    digitalWrite(DIR1, direction);
    digitalWrite(PWM1, !direction);
    delay(2000);
  }
}
