#include <LiquidCrystal.h>
const int rs=3, en=4, d4=5, d5=7, d6=6,d7=8;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.setCursor(0,0);
  lcd.print("Hello");
  lcd.setCursor(0,3);
  lcd.print("World");
}
