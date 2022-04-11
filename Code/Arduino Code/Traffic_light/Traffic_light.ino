#define RED 5
#define ORANGE 4
#define GREEN 3

void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(ORANGE, OUTPUT);
  pinMode(GREEN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(RED, HIGH);
  delay(2000);
  digitalWrite(ORANGE, HIGH);
  delay(2000);
  digitalWrite(ORANGE, LOW);
  digitalWrite(RED, LOW);
  digitalWrite(GREEN, HIGH);
  delay(2000);
  digitalWrite(GREEN, LOW);
  digitalWrite(ORANGE, HIGH);
  delay(2000);
  digitalWrite(ORANGE, LOW);
}
