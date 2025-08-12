"""**************************************************************

Programação para comunicação com rede CAN, inversor de tração, 
câmera para leitura de placas e leitor RFID
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

from datetime import datetime
from time import sleep, time

from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from Serial_Protocol_TCC.CommsRPi_lib import Comms
from Sign_Detection_TCC.detection import capture_photo, getClassName, indexVal

SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 115200
SERIAL_TIMEOUT_MS = 500
INTERVALO = 1  #segundo(s)

newRotMotor = 0
RotMotor = 0
StatusInv = ''
TempFET1 = 0
VeloCarro = 0
newVeloCarro = 0

PotValue = 0
PotVoltageValue = 0

lastTime1 = time()
lastTime2 = time()
def usleep(x): 
    sleep(x/1000000.0)

app = DecisionMkg()
transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
print("Iniciando Transmissor")
workbook = app.initialize_excel()

while True:
  tempo_atual = time()
  
  if tempo_atual - lastTime1 >= (INTERVALO / 10):
    raw_PotValue = transmissor.req_value_pot()
    PotVoltageValue = transmissor.req_voltage_pot()
    print(f"Valor do potenciômetro: {raw_PotValue}")
    print(f"Valor de tensão: {PotVoltageValue}")
    
    raw_CamValue = getClassName(indexVal)
    PotValue = app.get_pot_value(raw_PotValue)
    CamValue = app.get_cam_value(raw_CamValue)
    RFIDValue = app.get_rfid_value()
    lastTime1 = tempo_atual

  elif tempo_atual - lastTime2 >= INTERVALO:
    decisionFromLogic = app.decision_from_input_improved(PotValue, CamValue, RFIDValue)
    #app.executeDecision(decisionFromLogic)
    indexMatrix = app.which_index_matrix(PotValue, CamValue, RFIDValue)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app.save_log(workbook, timestamp, PotValue, CamValue, RFIDValue, indexMatrix)
    capture_photo(timestamp)
    
    lastTime2 = tempo_atual
