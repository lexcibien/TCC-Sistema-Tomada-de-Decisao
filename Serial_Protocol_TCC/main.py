from time import sleep
from CommsRPi_lib import Comms

SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 115200
SERIAL_TIMEOUT_MS = 500

""" newRotMotor = 110;
RotMotor = 100;
CurMotor = 90;
FreqMotor = 80;
StatusInv = 70;
VoltageInv = 60;
VeloCarro = 50;
TorqMotor = 40;
TempFET1 = 30;
TempFET2 = 20;
TempAirInt = 10;
OVCMotor = 09;
AlarmeAtual = 08;
FalhaAtual = 07;
FalhaAnt = 06; """
VeloCarro = 50
newVeloCarro = 0

def usleep(x): 
    sleep(x/1000000.0)

transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
print("Iniciando Transmissor")

while True:
    """transmissor.sendMessage("RpmMot", RotMotor)
    transmissor.sendMessage("CurMot", CurMotor)
    transmissor.sendMessage("FreMot", FreqMotor)
    transmissor.sendMessage("SttInv", StatusInv)
    transmissor.sendMessage("VolInv", VoltageInv)
    transmissor.sendMessage("VelCar", VeloCarro)
    transmissor.sendMessage("TrqMot", TorqMotor)
    transmissor.sendMessage("TmpFt1", TempFET1)
    transmissor.sendMessage("TmpFt2", TempFET2)
    transmissor.sendMessage("TmpAir", TempAirInt)
    transmissor.sendMessage("OvrMot", OVCMotor)
    transmissor.sendMessage("Alarme", AlarmeAtual)
    transmissor.sendMessage("FalAtu", FalhaAtual)
    transmissor.sendMessage("FalAnt", FalhaAnt)"""

    # transmissor.sendMessage("VelCar", newVeloCarro)
    # transmissor.sendMessage("VelCar", VeloCarro)

    pot_value = transmissor.req_value_pot()
    voltage_pot = transmissor.req_voltage_pot()
    print(pot_value)
    print(voltage_pot)

    usleep(5)  # Tempo menor entre envios3
