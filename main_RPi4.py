"""**************************************************************

Programação para simulação do sistema de tomada de decisão
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""


from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from Simulacao_Monte_Carlo.monteCarloSim import MonteCarloSim
from datetime import datetime
from time import time, sleep

numberOfIterations = 5

INTERVALO = 0.5
app = DecisionMkg()
sim = MonteCarloSim()
workbook = app.initialize_excel()

ultimo_tempo = time()
count = 0
while count < numberOfIterations:
  tempo_atual = time()

  if tempo_atual - ultimo_tempo >= INTERVALO:
    pot_value, cam_value, rfid_value, monteCarloIndex = sim.generateSimulationNumbers()
    indexDMkg = app.whichIndexMatrix(pot_value, cam_value, rfid_value)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app.saveLog(workbook, timestamp, pot_value, cam_value, rfid_value, monteCarloIndex, indexDMkg)
    
    ultimo_tempo = tempo_atual
    count += 1