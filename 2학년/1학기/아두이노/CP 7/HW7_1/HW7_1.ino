int pins_LED[4] = {2,3,4,5};

void setup( ) {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++)
  {
    pinMode(pins_LED[i], OUTPUT);
  }
}

void loop( ) {
  int adc = analogRead(A1); 
  int mapp = map(adc, 0, 1023, 11, 0);
  Serial.print("adc = ");
  Serial.println(adc);
  Serial.print("mapp = ");
  Serial.println(mapp);
  for (int i = 0; i < 4; i++)
  {
    if (mapp >= (i + 1) * 2)
    {
      digitalWrite(pins_LED[i], HIGH);
    }
    else
    {
      digitalWrite(pins_LED[i], LOW);
    }
  }
  delay(1000);
}
