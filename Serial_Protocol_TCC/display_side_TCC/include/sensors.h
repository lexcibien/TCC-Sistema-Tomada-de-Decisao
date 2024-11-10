#ifndef _SENSORS_H_
#define _SENSORS_H_

#include <params.h>

class Sensors {
public:
  enum ERROR {
    ERROR_OK = 0,
    ERROR_FAIL = 1
  };
    
  // variáveis globais das funções e seus protótipos
  Sensors();
  void initialization();
  long analogFilter(uint16_t, uint16_t []);
  int calculaPerCent();
  float calculaVoltage();
private:
  // pelo visto são as variáveis locais que todas tem
};

#endif // _SENSORS_H_