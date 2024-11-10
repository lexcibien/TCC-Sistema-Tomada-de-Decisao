/*****************************************************************************
 * | File      	 :   DEV_Config.h
 * | Author      :   waveshare
 * | Function    :   
 * | Info        :
 *----------------
 * | This version:   V1.0
 * | Date        :   2023-02-17
 * | Info        :
 * -----------------------------------------------------------------------------
 ******************************************************************************/
#ifndef _DEV_CONFIG_H_
#define _DEV_CONFIG_H_

#include <stdint.h>
#include "stdio.h"
#include <unistd.h>
#include "wiringPi.h"
#include "wiringPiSPI.h"

/**
 * data
**/
#define UBYTE   uint8_t
#define UWORD   uint16_t
#define UDOUBLE uint32_t

/**
 * GPIOI config
**/

#define SPI_CLK_PIN  14
#define SPI_MOSI_PIN 12
#define SPI_MISO_PIN 13
#define MCP2515_CS_PIN  15
/*------------------------------------------------------------------------------------------------------*/
void DEV_Digital_Write(UWORD Pin, UBYTE Value);
UBYTE DEV_Digital_Read(UWORD Pin);

void DEV_GPIO_Mode(UWORD Pin, UWORD Mode);

void DEV_Digital_Write(UWORD Pin, UBYTE Value);
UBYTE DEV_Digital_Read(UWORD Pin);

void DEV_SPI_WriteByte(UBYTE Value);
uint8_t DEV_SPI_ReadByte(void);
void DEV_SPI_Write_nByte(uint8_t *pData, uint32_t Len);

void DEV_Delay_ms(UDOUBLE xms);
void DEV_Delay_us(UDOUBLE xus);


UBYTE DEV_Module_Init(void);
void DEV_Module_Exit(void);


#endif
