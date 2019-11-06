
//Microsoft Store 을 이용하여 다운로드 된 아두이노인데 관리자 권한 어쩌고 오류가 발생하여 하드코딩 하였습니다. 양해 부탁드립니다 T.T
int piano[] = {0, 262, 294, 330, 349, 392, 440, 494, 523};

void setup( ) {
  Serial.begin(9600);
}

int tone_length = 1000;
void loop( ) {
  //static const uint8_t A2 = 56; 
  int speakerPin = A1; // 스피커 연결 핀 55
  int adc = analogRead(A2);
  //map 0,8 설정 시 2옥타브 도가 안 나오는 상황이 나와서 9로 설정, 9를 8로 바꿔줘 2옥타브 도 출력 잘 되게 하였습니다.
  int mapp = map(adc, 0, 1023, 0, 9);
  if (mapp == 9)
    mapp = 8;
  Serial.print("adc = ");
  Serial.println(adc);
  Serial.print("mapp = ");
  Serial.println(mapp);
  tone(speakerPin, piano[mapp], tone_length);
  delay(tone_length);
  noTone(speakerPin);
}
