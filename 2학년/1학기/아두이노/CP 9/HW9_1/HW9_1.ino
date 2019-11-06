#include <Servo.h>
Servo myServo;

int angle_step = 0, angle = 0;
int servoPin = 11;
int Pbutton = 14;
int Mbutton = 15;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(Pbutton, INPUT);
  pinMode(Mbutton, INPUT);
}

bool Pbef_but = 0, Pnow_but = 0;
bool Mbef_but = 0, Mnow_but = 0;

void loop() {
  
  Pbef_but = Pnow_but;
  Pnow_but = digitalRead(Pbutton);
  if (Pbef_but != Pnow_but and Pnow_but == 1)
  {
    angle_step = 10;
  }
    
    
  Mbef_but = Mnow_but;
  Mnow_but = digitalRead(Mbutton);
  if (Mbef_but != Mnow_but and Mnow_but == 1)
  {
    angle_step = -10;
  }
    
  angle += angle_step; // 현재 각도 조정
  myServo.write(angle);
  angle_step = 0;
  Serial.println(angle);
  if (angle < 0 or angle > 180)
    angle = 0;
}
