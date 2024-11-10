#ifndef _DISPLAY_H_
#define _DISPLAY_H_

#include <UnicViewAD.h>
#include <params.h>

class Display {
private:
  uint16_t baud_rate;
public:
  enum ERROR {
    ERROR_OK = 0,
    ERROR_FAIL = 1
  };
    
  // variáveis globais das funções e seus protótipos
  Display(uint16_t _baud_rate);
  void initialization();
  void displayStatus();
  void enviaDisplay();
private:
  String _status_Display;
  // pelo visto são as variáveis locais que todas tem
};

#endif // _DISPLAY_H_