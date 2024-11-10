#ifndef _COMMS_H_
#define _COMMS_H_

#include <Arduino.h>

#define DEFAULT_BAUDRATE 115200

class Comms {
private:
  unsigned long baud_rate;
  uint8_t pin_rx;
  uint8_t pin_tx;

public:
  uint16_t RotMotor;
  uint16_t CurMotor;
  uint16_t FreqMotor;
  uint16_t StatusInv;
  uint16_t VoltageInv;
  uint16_t VeloCarro;
  uint16_t TorqMotor;
  uint16_t TempFET1;
  uint16_t TempFET2;
  uint16_t TempAirInt;
  uint16_t OVCMotor;
  uint16_t AlarmeAtual;
  uint16_t FalhaAtual;
  uint16_t FalhaAnt;

  Comms(uint8_t _pin_rx, uint8_t _pin_tx, unsigned long _baud_rate);
  void initialization();
  void readMessage();
  void processMessage(String mensagem);
  void sendMessage(String, int);
  void sendMessage(String, float);
  void enviarAck();
};

#endif // _COMMS_H_