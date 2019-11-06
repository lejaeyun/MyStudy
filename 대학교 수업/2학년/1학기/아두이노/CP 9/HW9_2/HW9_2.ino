int DIR1 = 41;
int PWM1 = 9;
int button = 14;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(DIR1, OUTPUT);
  pinMode(PWM1, OUTPUT);
  pinMode(button, INPUT);
}

bool bef_but = 0, now_but = 0;
int pwm_value = 0;
void loop() {
  bef_but = now_but;
  now_but = digitalRead(button);
  if (bef_but != now_but and now_but == 1)
  {
    pwm_value += 127;
    if (pwm_value > 255)
      pwm_value = 0;
  }

  digitalWrite(DIR1, HIGH);
  analogWrite(PWM1, pwm_value);
}
