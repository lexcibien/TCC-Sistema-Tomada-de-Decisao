#include <comms.h>
#include <sensors.h>
//#include <SoftwareSerial.h>

//SoftwareSerial* RPiSerial = nullptr; // Ponteiro para o objeto SoftwareSerial
Sensors* sensor = nullptr; // Ponteiro para o objeto SoftwareSerial

Comms::Comms(uint8_t _pin_rx, uint8_t _pin_tx,unsigned long _baud_rate) {
  pin_rx = _pin_rx;
  pin_tx = _pin_tx;
  baud_rate = _baud_rate;

  RotMotor = 0;
  CurMotor = 0;
  FreqMotor = 0;
  StatusInv = 0;
  VoltageInv = 0;
  VeloCarro = 0;
  TorqMotor = 0;
  TempFET1 = 0;
  TempFET2 = 0;
  TempAirInt = 0;
  OVCMotor = 0;
  AlarmeAtual = 0;
  FalhaAtual = 0;
  FalhaAnt = 0;
}

void Comms::initialization() {
  //Serial = new SoftwareSerial(pin_rx, pin_tx);
  sensor = new Sensors();
  Serial.begin(baud_rate);
}

void Comms::readMessage() {
  if (Serial.available() > 0) {
    String mensagemRecebida = Serial.readStringUntil('\n');
    processMessage(mensagemRecebida);
  }
}

void Comms::processMessage(String message) {
  String recMessage = message.substring(7);

  if (message.startsWith("PotReq")) {
    int potPerCent = sensor->calculaPerCent();
    sendMessage("PotRes:", potPerCent); // usar o sensors.h e fazer o handshake do arduino para o RPi
    return;
  }

  else if (message.startsWith("VopReq")) {
    float potVoltage = sensor->calculaVoltage();
    sendMessage("VopRes:", potVoltage); // usar o sensors.h e fazer o handshake do arduino para o RPi
    return;
  }

  else if (message.startsWith("RpmMot:")) RotMotor = recMessage.toInt();
  else if (message.startsWith("CurMot:")) CurMotor = recMessage.toInt();
  else if (message.startsWith("FreMot:")) FreqMotor = recMessage.toInt();
  else if (message.startsWith("SttInv:")) StatusInv = recMessage.toInt();
  else if (message.startsWith("VolInv:")) VoltageInv = recMessage.toInt();
  else if (message.startsWith("VelCar:")) VeloCarro = recMessage.toInt();
  else if (message.startsWith("TrqMot:")) TorqMotor = recMessage.toInt();
  else if (message.startsWith("TmpFt1:")) TempFET1 = recMessage.toInt();
  else if (message.startsWith("TmpFt2:")) TempFET2 = recMessage.toInt();
  else if (message.startsWith("TmpAir:")) TempAirInt = recMessage.toInt();
  else if (message.startsWith("OvrMot:")) OVCMotor = recMessage.toInt();
  else if (message.startsWith("Alarme:")) AlarmeAtual = recMessage.toInt();
  else if (message.startsWith("FalAtu:")) FalhaAtual = recMessage.toInt();
  else if (message.startsWith("FalAnt:")) FalhaAnt = recMessage.toInt();
  else {Serial.print("NACK\n"); return;}
  enviarAck(); // Envia confirmação "ACK"
}

void Comms::sendMessage(String str_msg, int message) {
  String mensagem = str_msg + String(message) + "\n";
  Serial.print(mensagem);
}

void Comms::sendMessage(String str_msg, float message) {
  String mensagem = str_msg + String(message, 2) + "\n"; // Definindo 2 casas decimais para float
  Serial.print(mensagem);
}

void Comms::enviarAck() {
  Serial.print("ACK\n"); // Envia a confirmação "ACK"
}