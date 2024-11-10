#include <params.h>
#include <display.h>
#include <comms.h>

LCM Lcm(Serial);
extern Comms receptor;

/* LcmVar RpmMot(0); LcmVar CurMot(4, FOUR_BYTES); LcmVar FreMot(8); LcmString SttInv(52, 20); 
LcmVar VolInv(12, FOUR_BYTES); LcmVar VelCar(16); LcmVar TrqMot(20); LcmVar TmpFt1(24); LcmVar TmpFt2(28); 
LcmVar TmpAir(32); LcmVar OvrMot(36); LcmVar Alarme(40); LcmVar FalAtu(44); LcmVar FalAnt(48); */

LcmVar RpmMot(0); LcmVar VelCar(2); LcmVar TmpFt1(4); LcmString SttInv(6, 20);


Display::Display(uint16_t _baud_rate) {  //início das variáveis que irão ser principalmente alteradas
  baud_rate = _baud_rate;
}

void Display::initialization() {
  Serial.begin(BAUD_RATE);
  while(!Serial);

  Lcm.begin();

  Lcm.changePicId(0);
  Lcm.changeBacklight(40);
  delay(3000);
  Lcm.changeBacklight(100);
  Lcm.changePicId(1);
}

void Display::displayStatus() {
  switch (receptor.StatusInv) {
  case 0:
    _status_Display = "Ready";
    break;
  case 1:
    _status_Display = "Run";
    break;
  case 2:
    _status_Display = "Subtensão";
    break;
  case 3:
    _status_Display = "Falha";
    break;
  case 4:
    _status_Display = "Autoajuste";
    break;
  case 5:
    _status_Display = "Configuração";
    break;
  case 6:
    _status_Display = "Frenagem CC";
    break;
  
  default:
    _status_Display = "Sem Função";
    break;
  }
}

void Display::enviaDisplay() { //envia os dados para o display
  static unsigned long tempoAnt;
  unsigned long tempoAtual = millis();
  byte telaAtual = Lcm.readPicId();

  displayStatus();

  if(tempoAtual - tempoAnt >= INTERVALO) {  
    if(telaAtual == 1) { //informações que aparecerão na tela 1
      RpmMot.write(receptor.RotMotor);
      //CurMot.write(receptor.CurMotor);
      //FreMot.write(receptor.FreqMotor);
      SttInv.write(_status_Display);
      //VolInv.write(receptor.VeloCarro);
      VelCar.write(receptor.TorqMotor);
      //TrqMot.write(receptor.TorqMotor);
      TmpFt1.write(receptor.TempFET1);
      //TmpFt2.write(receptor.TempFET2);
      //TmpAir.write(receptor.TempAirInt);
      //OvrMot.write(receptor.OVCMotor);
      //Alarme.write(receptor.AlarmeAtual);
      //FalAtu.write(receptor.FalhaAtual);
      //FalAnt.write(receptor.FalhaAnt);
    }
    if(telaAtual == 3) {
    }
    tempoAnt = tempoAtual;
  }
}
//talvez fazer uma aba de configurações