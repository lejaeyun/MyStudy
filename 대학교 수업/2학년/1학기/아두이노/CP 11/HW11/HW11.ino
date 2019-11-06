#include <Wire.h>
#include <ADXL345.h>
int Tap_pin = 2;
int Active_pin = 3;

ADXL345 adxl;

void setup(){
  Serial.begin(9600);
  pinMode(Tap_pin, OUTPUT);
  pinMode(Active_pin, OUTPUT);
  adxl.powerOn();

  adxl.setActivityThreshold(75);
  adxl.setInactivityThreshold(75);
  adxl.setTimeInactivity(10);
 
  adxl.setActivityX(1);
  adxl.setActivityY(1);
  adxl.setActivityZ(1);
 
  adxl.setInactivityX(1);
  adxl.setInactivityY(1);
  adxl.setInactivityZ(1);
 
  adxl.setTapDetectionOnX(0);
  adxl.setTapDetectionOnY(0);
  adxl.setTapDetectionOnZ(1);
 
  adxl.setTapThreshold(50);
  adxl.setTapDuration(15);
  adxl.setDoubleTapLatency(80);
  adxl.setDoubleTapWindow(200);
 
  adxl.setFreeFallThreshold(7);
  adxl.setFreeFallDuration(45);
 
  adxl.setInterruptMapping( ADXL345_INT_SINGLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_DOUBLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_FREE_FALL_BIT,    ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_ACTIVITY_BIT,     ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_INACTIVITY_BIT,   ADXL345_INT1_PIN );
  
  adxl.setInterrupt( ADXL345_INT_SINGLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_DOUBLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_FREE_FALL_BIT,  1);
  adxl.setInterrupt( ADXL345_INT_ACTIVITY_BIT,   1);
  adxl.setInterrupt( ADXL345_INT_INACTIVITY_BIT, 1);
}

int Tap_Num = 0;
int Act_Num = 0;
bool State_Tap = false;
bool State_Active = false;

void loop()
{
  byte interrupts = adxl.getInterruptSource();
  
  if(adxl.triggered(interrupts, ADXL345_SINGLE_TAP))
  {
    State_Tap = !State_Tap;
    digitalWrite(Tap_pin, State_Tap);
    Tap_Num += 1;
    Serial.print("Tap Num : " + String(Tap_Num) + "\n");
  }

  if(adxl.triggered(interrupts, ADXL345_ACTIVITY))
  {
    State_Active = !State_Active;
    digitalWrite(Active_pin, State_Active);
    Act_Num += 1;
    Serial.print("Active Num : " + String(Act_Num) + "\n");
  }
}
