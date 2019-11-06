void setup() {
  Serial.begin(9600);     // 시리얼 포트 초기화
}

void loop() {
  
  String str[5] = {};

  int state = 1;
  char buffer[128];
  int index = 0;

  while (true) 
  {
    
    
    if (state == 1) 
    {
      if (index == 5)
      {
        break;
      }
      Serial.print("Enter the " + String((index + 1))  + "th  Word --> ");
      state = 2;
      index++;
    }
    
    while (Serial.available()) 
    { 
      int len = Serial.readBytesUntil('\n', buffer, 127);
      if (len > 0) 
      {     
        buffer[len] = '\0';
        String in_str = String(buffer);
        str[index - 1] = in_str;
        Serial.print(in_str);
        Serial.println();     
        state = 1;
        break;
      }
    }
  }
  
  // 문자열 정렬
  for (int i = 0; i < 4; i++) 
  {
    for (int j = i + 1; j < 5; j++) 
    {
      int compare = str[i].compareTo(str[j]);
      if (compare > 0) 
      {
        String temp = str[i];
        str[i] = str[j];
        str[j] = temp;
      }
    }
  }
  
  Serial.println("After Sorting");
  for (int i = 0; i < 5; i++) 
  {
    Serial.println(String(i) + "th String : " + str[i]);
  }
}
