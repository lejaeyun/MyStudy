
int num1, num2, sum;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(3000); // setting parseint timeout
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Enter 2 Integer to add");
  num1 = Serial.parseInt();
  num2 = Serial.parseInt();
  sum = num1 + num2;
  Serial.print(num1);Serial.print(" + ");Serial.print(num2);Serial.print(" = ");Serial.println(sum);
  
}
