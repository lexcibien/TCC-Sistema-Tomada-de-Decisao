#include "MCP2515.h"   //Examples
#include "DEV_Config.h"

#define dlc 8

int main(void)
{
    DEV_Delay_ms(500);
    DEV_Module_Init();
    
    MCP2515_Init(KBPS1000);
    DEV_Delay_ms(500);

    uint32_t id = 0x0;
    uint8_t data[dlc] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07};
    
    
    printf("Press CTRL-C to end the program\r\n");
    printf("Data is sent at one-second intervals\r\n");
    while(1)
    {
        printf("The data sent is : ");
        for(int i = 0; i < dlc; i++)
            printf("%x ", data[i]);
        printf("\r\n");
        
        MCP2515_Send(id, data, dlc);
        DEV_Delay_ms(1000);
    }
    
    return 0;
}
