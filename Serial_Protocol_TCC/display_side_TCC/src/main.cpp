#include <params.h>
#include <comms.h>
//#include <display.h>
#include <sensors.h>
//RP2040
//Nano

//puxa os dados do serial e enviar ao display.
void testPot();

Sensors sensores;
Comms receptor(SERIAL_SIM_RX, SERIAL_SIM_TX, BAUD_RATE);
//Display display(BAUD_RATE);

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  sensores.initialization();
  receptor.initialization();
  //display.initialization();
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  //testPot();
  receptor.readMessage();
  //display.enviaDisplay();
}

unsigned long lastTime = millis();

void testPot() {
  unsigned long nowTime = millis();

  int perCentValue = sensores.calculaPerCent();
  float voltageValue = sensores.calculaVoltage();

  if(nowTime - lastTime >= 62) {
    Serial.print("Porcentagem do potenciômetro:");
    Serial.println(perCentValue);

    Serial.print("Tensão do potenciômetro:");
    Serial.println(voltageValue);
    lastTime = nowTime;
  }
}