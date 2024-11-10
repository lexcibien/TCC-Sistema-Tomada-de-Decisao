#ifndef _PARAMS_H_
#define _PARAMS_H_

#include <Arduino.h>

// DEFINIÇÕES DOS PINOS
#define VELO_PIN 2          //2
#define ROT_PIN 3           //3
#define SENSUP_PIN 4       //4
#define SENSDWN_PIN 5        //5
#define ROTDISPLAY_PIN 7    //7
#define BAT_PIN A1          //A1

// DEFINIÇÕES PARA A MAIN
#define BAUD_RATE 250000
#define INTERVALO 100           //250     250ms
#define INTERVALO_EEPROM 60000  //60000   60s
#define PULSOS_VEL 19
#define PULSOS_ROT 1
#define DIAM_RODA 0.560131
#define REL_RODA_DISCO 4.5833
#define EMISSIVITY_OBJECT 0.97  //Emissividade da borracha
#define COMB_HYSTERESIS 3000
#define N_SAMPLES 10

void calculaDados();
void enviaSerial(), lerEntradas();

#endif // _PARAMS_H_
