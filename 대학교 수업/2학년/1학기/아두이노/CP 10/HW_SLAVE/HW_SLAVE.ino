void setup(){
    Serial.begin(9600);
    Serial1.begin(9600);
}

void loop(){
  int state = 1, len = 0;
  char buffer[128];
  while (true) {
    if (Serial1.available()) 
    {
      if (state == 1) {
        Serial.print("Current Temp C : ");
        state = 2;
      }
      while (Serial1.available()) { 
        char data = Serial1.read();
        if (data == '\n') 
        {  
          buffer[len] = '\0';
          String in_str = buffer;
          Serial.println(in_str + " C");          
          state = 1;
          len = 0;        
          break;
        }
        buffer[len++] = data;
       }
    }
  }
}
