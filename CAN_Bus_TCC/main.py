"""
Executar o código no terminal do Raspberry Pi
python3 main.py
"""

from CANBusRPi_lib import CanBus

newRotMotor = 110
RotMotor = 100
CurMotor = 90
FreqMotor = 80
StatusInv = 70
VoltageInv = 60
VeloCarro = 50
TorqMotor = 40
TempFET1 = 30
TempFET2 = 20
TempAirInt = 10
OVCMotor = 9
AlarmeAtual = 8
FalhaAtual = 7
FalhaAnt = 6

canBus = CanBus(_channel="can0", _bustype="socketcan", _bitrate="1000000")

while True:
    canBus.can_id = 0x00
    canBus.can_dlc = 8
    canBus.send_message_can(newRotMotor)

    # Recebendo a mensagem e atribuindo os valores a info1, info2, info3, info4
    info1, info2, info3, info4 = canBus.received_message_can()

    if canBus.can_id == 0x0E:
        RotMotor = info1
        CurMotor = info2
        FreqMotor = info3
        StatusInv = info4
    elif canBus.can_id == 0x0F:
        VoltageInv = info1
        VeloCarro = info2
        TorqMotor = info3
        TempFET1 = info4
    elif canBus.can_id == 0x10:
        TempFET2 = info1
        TempAirInt = info2
        OVCMotor = info3
        AlarmeAtual = info4
    elif canBus.can_id == 0x11:
        FalhaAtual = info1
        FalhaAnt = info2
    else:
        info1 = 0
        info2 = 0
        info3 = 0
        info4 = 0

    print(f"Info1: {info1}, Info2: {info2}, Info3: {info3}, Info4: {info4}")
