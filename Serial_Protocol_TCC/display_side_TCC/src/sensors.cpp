#include <sensors.h>

uint16_t numbersPot[N_SAMPLES];

// Definição do pino onde o potenciômetro está conectado
#define POT_PIN A1
#define REF_VOLTAGE 4.947
#define ANALOG_RESOLUTION 1023.0

Sensors::Sensors() {
}

void Sensors::initialization() {
  pinMode(POT_PIN, INPUT);
}

long Sensors::analogFilter(uint16_t rawValue, uint16_t numbers[]) {
  for(uint8_t i = N_SAMPLES-1; i > 0; i--) numbers[i] = numbers[i-1];
  numbers[0] = rawValue;

  long acc = 0;
  for(uint8_t i = 0; i < N_SAMPLES; i++) acc += numbers[i];
  delay(1);

  return acc/N_SAMPLES;
}

int Sensors::calculaPerCent() {
  uint16_t rawValue = analogRead(POT_PIN);
  uint16_t filteredValue = analogFilter(rawValue, numbersPot);
  int percent = ((filteredValue / ANALOG_RESOLUTION) * 200) - 100;
  
  return percent;
}

float Sensors::calculaVoltage() {
  uint16_t rawValue = analogRead(POT_PIN);
  uint16_t filteredValue = analogFilter(rawValue, numbersPot);
  float voltage = (filteredValue / ANALOG_RESOLUTION) * REF_VOLTAGE;
  
  return voltage;
}

float Sensors::calculaRawVoltage() {
  uint16_t rawValue = analogRead(POT_PIN);
  float voltage = float(rawValue / ANALOG_RESOLUTION * REF_VOLTAGE);
  
  return voltage;
}