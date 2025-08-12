"""
  Main file for the Decision Making module of the TCC project.
  This file is responsible for the decision making process of the project.
  It uses the DecisionMkg class from the DecisionMkgRPI_lib.py file to make decisions based on the input values.
"""

from datetime import datetime
from time import time
from DecisionMkgRPI_lib import DecisionMkg
from Sign_Detection_TCC.detection import getClassName, indexVal

INTERVALO = 1
ultimo_tempo = time()
   
app = DecisionMkg()
workbook = app.initialize_excel()

while True:
  tempo_atual = time()
  raw_cam_value = getClassName(indexVal)
  potentiometer_reading = app.pot_reading
  potentiometer_value = app.get_pot_value(potentiometer_reading)
  cam_value = app.get_cam_value(raw_cam_value)
  rfid_value = app.get_rfid_value()

  if tempo_atual - ultimo_tempo >= INTERVALO:
    decision_from_logic = app.decision_from_input_improved(potentiometer_value, cam_value, rfid_value)
    indexExit = app.which_index_matrix(potentiometer_value, cam_value, rfid_value)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app.save_log(workbook, timestamp, potentiometer_value, cam_value, rfid_value, 0, indexExit)
    ultimo_tempo = tempo_atual
