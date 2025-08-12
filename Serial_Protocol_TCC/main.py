from time import sleep
from CommsRPi_lib import Comms

SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 115200
SERIAL_TIMEOUT_MS = 500

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
newVeloCarro = 0


def usleep(x):
    sleep(x / 1000000.0)


transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
print("Iniciando Transmissor")

while True:
    transmissor.send_message("RpmMot", RotMotor)
    transmissor.send_message("CurMot", CurMotor)
    transmissor.send_message("FreMot", FreqMotor)
    transmissor.send_message("SttInv", StatusInv)
    transmissor.send_message("VolInv", VoltageInv)
    transmissor.send_message("VelCar", VeloCarro)
    transmissor.send_message("TrqMot", TorqMotor)
    transmissor.send_message("TmpFt1", TempFET1)
    transmissor.send_message("TmpFt2", TempFET2)
    transmissor.send_message("TmpAir", TempAirInt)
    transmissor.send_message("OvrMot", OVCMotor)
    transmissor.send_message("Alarme", AlarmeAtual)
    transmissor.send_message("FalAtu", FalhaAtual)
    transmissor.send_message("FalAnt", FalhaAnt)

    pot_value = transmissor.req_value_pot()
    voltage_pot = transmissor.req_voltage_pot()
    print(pot_value)
    print(voltage_pot)

    usleep(5)  # Tempo menor entre envios
