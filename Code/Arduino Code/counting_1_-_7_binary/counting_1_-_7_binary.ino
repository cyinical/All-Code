#define R4 5
#define O2 6
#define G1 7

void setup() {
  // put your setup code here, to run once:
  pinMode(R4, OUTPUT);
  pinMode(O2, OUTPUT);
  pinMode(G1, OUTPUT);
}

void loop() {
  //1
  digitalWrite(G1, HIGH);
  delay(1000);
  //2
  digitalWrite(G1, LOW);
  delay(1000);
  digitalWrite(O2, HIGH);
  delay(1000);
  //3
  digitalWrite(G1, HIGH);
  delay(1000);
  //4
  digitalWrite(G1, LOW);
  digitalWrite(O2, LOW);
  delay(1000);
  digitalWrite(R4, HIGH);
  //5
  digitalWrite(G1, HIGH);
  //6
  digitalWrite(G1, LOW);
  digitalWrite(R4, LOW);
  delay(1000);
  digitalWrite(R4, HIGH);
  digitalWrite(02, HIGH);
  delay(1000);
  //7
  digitalWrite(G1, HIGH);
  delay(1000);
  digitalWrite(G1, LOW);
  digitalWrite(R4, LOW);
  digitalWrite(G1, LOW);

  //1
  //digitalWrite(G1, HIGH);
  //delay(100);
  //digitalWrite(G1, LOW);

}
