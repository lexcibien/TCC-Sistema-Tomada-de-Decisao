#include <params.h>
#include <sensors.h>
//RP2040
//Nano

int numOfSamples = 1002;

extern Sensors sensores;

void potAccSetup1Time() {
  Serial.begin(BAUD_RATE);
  pinMode(LED_BUILTIN, OUTPUT);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  sensores.initialization();
  digitalWrite(LED_BUILTIN, LOW);

  int count = 0;
  unsigned long lastTime = millis();

  while (count < numOfSamples) {
    float voltageRawValue = sensores.calculaRawVoltage();
    float voltageValue = sensores.calculaVoltage();

    unsigned long nowTime = millis();
    if(nowTime - lastTime >= INTERVALO) {
      Serial.print(voltageRawValue);
      Serial.print(",");
      Serial.print(voltageValue);
      Serial.println();
    
      count += 1;
      lastTime = nowTime;
    }
  }
  Serial.println("teste finalizado");
}