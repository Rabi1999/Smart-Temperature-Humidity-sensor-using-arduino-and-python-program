#include <SimpleDHT.h>
#include <LiquidCrystal.h>
char d;
// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 8;
SimpleDHT11 dht11(pinDHT11);
LiquidCrystal lcd(2,3,4,5,6,7);

void setup() {
  Serial.begin(9600);
   lcd.begin(16, 2);
}

void loop() {
  if(Serial.available())
{
  d=Serial.read();
}
if (d=='a')
{
  
  
  // read without samples.
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    return;
  }
  //lcd.setCursor(0,0);
  //lcd.print("Temp is ");
  //lcd.print((int)temperature); lcd.print(" *C, "); 
  //lcd.setCursor(0,1);
  //lcd.print("Humidity:");
  //lcd.print((float)humidity);
  Serial.println(temperature);
  Serial.println(humidity);
  // DHT11 sampling rate is 1HZ.
  delay(1500);
}
}
