int motorPin1 = 9;
int motorPin2 = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  delay(1000);
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  delay(1000);
}
