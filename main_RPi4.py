"""**************************************************************

Programação para comunicação com rede CAN, inversor de tração, 
câmera para leitura de placas e leitor RFID
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

from Serial_Protocol_TCC.CommsRPi_lib import Comms
from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from Sign_Detection_TCC.detection import indexVal, getClassName, capture_photo
from datetime import datetime
from time import time, sleep

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
usleep = lambda x: sleep(x/1000000.0)

app = DecisionMkg
transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
print("Iniciando Transmissor")
workbook = app.initialize_excel()

while True:
  tempo_atual = time()
  
  if tempo_atual - lastTime1 >= (INTERVALO / 10):
    raw_PotValue = transmissor.reqValuePot()
    PotVoltageValue = transmissor.reqVoltagePot()
    print(f"Valor do potenciômetro: {raw_PotValue}")
    print(f"Valor de tensão: {PotVoltageValue}")
    
    raw_CamValue = getClassName(indexVal)
    PotValue = app.getPotValue(raw_PotValue)
    CamValue = app.getCamValue(raw_CamValue)
    RFIDValue = app.getRFIDValue()
    lastTime1 = tempo_atual

  elif tempo_atual - lastTime2 >= INTERVALO:
    decisionFromLogic = app.decisionFromInput(PotValue, CamValue, RFIDValue)
    #app.executeDecision(decisionFromLogic)
    indexMatrix = app.whichIndexMatrix(PotValue, CamValue, RFIDValue)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app.saveLog(workbook, timestamp, PotValue, CamValue, RFIDValue, indexMatrix)
    capture_photo(timestamp)
    
    lastTime2 = tempo_atual