from DecisionMkgRPI_lib import DecisionMkg
from ..Sign_Detection_TCC.detection import getClassName, indexVal
from datetime import datetime
from time import time, sleep

INTERVALO = 1
ultimo_tempo = time()
   
app = DecisionMkg()
workbook = app.initialize_excel()

while True:
  tempo_atual = time()
  raw_cam_value = getClassName(indexVal)
  potentiometer_reading = app.POT_reading
  potentiometer_value = app.getPotValue()
  cam_value = app.getCamValue(raw_cam_value)
  rfid_value = app.getRFIDValue()

  if tempo_atual - ultimo_tempo >= INTERVALO:
    #decisionFromLogic = app.decisionFromInputImproved(potentiometer_value, cam_value, rfid_value)
    decisionFromLogic = app.decisionFromInput(potentiometer_value, cam_value, rfid_value)
    #app.executeDecision(decisionFromLogic)
    indexExit = app.whichIndexMatrix(potentiometer_value, cam_value, rfid_value)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app.saveLog(workbook, timestamp, potentiometer_value, cam_value, rfid_value, 0, indexExit)
    
    app.saveLog()
    ultimo_tempo = tempo_atual