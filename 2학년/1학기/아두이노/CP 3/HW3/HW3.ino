int pins[] ={2,3,4,5};
int index = 0;
int shift;

void setup() 
{
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) 
  {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}
  
void loop() 
{
  if (index<4) 
      shift = index+1;
  else 
      shift = 7-index;
  
  for (int i=0; i<4; i++)
  {
    if (i < shift) 
    {    
      Serial.print("O ");
      digitalWrite(pins[i], HIGH);  
    } 
    else 
    {      
      Serial.print("X ");
      digitalWrite(pins[i], LOW);
    }
  }
  Serial.println();
  delay(1000);
  
  index = index + 1;
  
  if (index == 7)
      index = 0; 
}
