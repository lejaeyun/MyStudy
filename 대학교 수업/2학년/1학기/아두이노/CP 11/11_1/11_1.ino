int motionPin = 8;
int trigPin = 3;
int echoPin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(motionPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  int motion = digitalRead(motionPin);
  
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);
  float duration = pulseIn(echoPin, HIGH);
  float distance = duration * 340 / 10000 / 2;  
  Serial.println(String("Distance(cm): ") + distance);
  
  if(motion == 1) {
    Serial.println("Motion detected");
  }

  delay(500);
}
