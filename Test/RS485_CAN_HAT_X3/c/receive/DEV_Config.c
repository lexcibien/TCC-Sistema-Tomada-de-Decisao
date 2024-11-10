/*****************************************************************************
 * | File      	 :   DEV_Config.c
 * | Author      :   waveshare
 * | Function    :   
 * | Info        :
 *----------------
 * | This version:   V1.0
 * | Date        :   2023-02-17
 * | Info        :
 * -----------------------------------------------------------------------------
 ******************************************************************************/
#include "DEV_Config.h"

#define SPI_PORT 0

/**
 * GPIO read and write
**/
void DEV_Digital_Write(UWORD Pin, UBYTE Value)
{
    digitalWrite(Pin, Value);
}

UBYTE DEV_Digital_Read(UWORD Pin)
{
    return digitalRead(Pin);
}

/**
 * SPI
**/
void DEV_SPI_WriteByte(uint8_t Value)
{
    wiringPiSPIDataRW(SPI_PORT, &Value, 1);
}

uint8_t DEV_SPI_ReadByte(void)
{
    uint8_t buf[1];
    wiringPiSPIDataRW(SPI_PORT, buf, 1);
    return buf[0];
}


void DEV_SPI_Write_nByte(uint8_t pData[], uint32_t Len)
{
    wiringPiSPIDataRW(SPI_PORT, pData, Len);
}

/**
 * GPIO Mode
**/
void DEV_GPIO_Mode(UWORD Pin, UWORD Mode)
{
    if(Mode == 0 || Mode == INPUT) {
        pinMode(Pin, INPUT);
    } else {
        pinMode(Pin, OUTPUT);
    }
}

/**
 * delay x ms
**/
void DEV_Delay_ms(UDOUBLE xms)
{
    delay(xms);
}

void DEV_Delay_us(UDOUBLE xus)
{
    usleep(xus);
}

void DEV_GPIO_Init(void)
{
    wiringPiSetupGpio();
    
    DEV_GPIO_Mode(MCP2515_CS_PIN, 1);
    DEV_Digital_Write(MCP2515_CS_PIN, 1);
}
/******************************************************************************
function:	Module Initialize, the library and initialize the pins, SPI protocol
parameter:
Info:
******************************************************************************/
UBYTE DEV_Module_Init(void)
{ 
    
    // SPI Config
    wiringPiSPISetup(SPI_PORT, 10000 * 1000);
    
    // GPIO Config
    DEV_GPIO_Init();

    printf("DEV_Module_Init OK \r\n");
    return 0;
}

/******************************************************************************
function:	Module exits, closes SPI and BCM2835 library
parameter:
Info:
******************************************************************************/
void DEV_Module_Exit(void)
{

}
