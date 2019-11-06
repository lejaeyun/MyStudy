int pins[] ={2,3,4,5};
int led_state = 0, type = 0;
boolean but_state;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}
  
void loop() {
  but_state = digitalRead(15);

  if (but_state == 1)
  {
    if (type == 0)
    {
      type = 1;
      led_state = 0;
    }
    else
    {
      type = 0;
      led_state = 3;
    }
  }
  
  for (int i = 0; i < 4; i++) 
  {
    if (i == led_state) 
    {
      digitalWrite(pins[i], HIGH);  
    } else 
    {
      digitalWrite(pins[i], LOW);
    }
  }
  

  if (type == 0) 
  {
    led_state = (led_state + 1) %4 ;
  }
  else  
  {
    led_state = (led_state - 1) %4 ;
    if (led_state == -1)
     {
      led_state = 3;
     }
  }
  delay(500);
}
