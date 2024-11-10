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
    uint8_t rdata[dlc];

    printf("Press CTRL-C to end the program\r\n");
    while(1)
    {
        MCP2515_Receive(id, rdata);
        printf("The received data is : ");
        for(int i = 0; i < dlc; i++)
            printf("%x ", rdata[i]);
        printf("\r\n");
    }
    
    return 0;
}
