"""**************************************************************

Biblioteca para tomada de decisão entre a câmera, RFID e potenciômetro
Autor: Alex Luiz Cibien E Silva
Data de início: setembro de 2024

**************************************************************"""

from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from datetime import datetime
from time import time, sleep
from random import randint

actionList:list = []

class MonteCarloSim:

  PEDESTRE = 5
  VEL20KMH = 4
  PARAR = 3
  OCIOSO = 2
  N_DETECTOU = 2
  N_LIMITE = 2
  ACELERAR = 1

  def __init__(self):
    print("iniciando biblioteca Monte Carlo")
    self.patterns = [
        (3, 3, 3),  # vai do index 1 para frente
        (3, 3, 5),
        (3, 3, 4),
        (3, 2, 2),
        (3, 2, 3),
        (3, 2, 4),
        (3, 2, 5),
        (3, 4, 3),
        (3, 4, 5),
        (3, 4, 4),
        ([1, 2], 3, 3), #estou num impasse aqui
        ([1, 2], 3, 5),
        ([1, 2], 3, 4),
        ([1, 2], 2, 2),
        ([1, 2], 2, 3),
        ([1, 2], 2, 5),
        ([1, 2], 2, 4),
        ([1, 2], 4, 4),
        ([1, 2], 4, 5),
        ([1, 2], 4, 3),
    ]
    # adicionar as outras placas e testar removendo a parte do DecisionMaking repetido.
  def findMonteCarloIndex(self, pot, cam, rfid) -> int:
    for i, (p, c, r) in enumerate(self.patterns):
      if (pot, cam, rfid) == (p, c, r):
        return i
    return -1
  
  def generateSimulationNumbers(self) -> tuple:
    value_from_pot = randint(1, 3)
    value_from_cam = randint(2, 4)
    value_from_rfid = randint(2, 5)
    indexMC = self.findMonteCarloIndex(value_from_pot, value_from_cam, value_from_rfid)
    
    return value_from_pot, value_from_cam, value_from_rfid, indexMC

if __name__ == "__main__":
  INTERVALO = 1
  ultimo_tempo = time()
  sim = MonteCarloSim()
  app = DecisionMkg()
  workbook = app.initialize_excel()

  count = 0
  while count < 5:
    tempo_atual = time()

    if tempo_atual - ultimo_tempo >= INTERVALO:
      pot_value, cam_value, rfid_value, monteCarloIndex = sim.generateSimulationNumbers()
      indexDMkg = app.whichIndexMatrix(pot_value, cam_value, rfid_value)
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      app.saveLog(workbook, timestamp, pot_value, cam_value, rfid_value, monteCarloIndex, indexDMkg)
      
      ultimo_tempo = tempo_atual
      count += 1