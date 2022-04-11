#define SendSignal 7
#define RecSignal 6
#define RED 5
#define YELLOW 4
#define GREEN 3

void setup() {
  // put your setup code here, to run once:
  pinMode(SendSignal, OUTPUT);
  pinMode(RecSignal, INPUT);
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  long duration, distance;
  digitalWrite(SendSignal, LOW);
  delayMicroseconds(2);
  digitalWrite(SendSignal, HIGH);
  delayMicroseconds(10);
  digitalWrite(SendSignal, LOW);
  duration = pulseIn(RecSignal, HIGH);
  distance = duration*0.034/2;
  if (distance <= 10)
  {
      Serial.println("DANGER to close");
      Serial.print(distance);
      Serial.println(" cm");
      digitalWrite(RED, HIGH);
      digitalWrite(YELLOW, LOW);
      digitalWrite(GREEN, LOW);
      delay(1000);
  }
  else if (distance <= 20)
  { 
    Serial.println("Distance currently: ");
    Serial.print(distance);
    Serial.println(" cm");
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, HIGH);
    delay(1000);
  }
  else if (distance > 20)
  {
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, HIGH);
    digitalWrite(GREEN, LOW);
    delay(1000);
  }
}
