"""**************************************************************

Biblioteca para tomada de decisão entre a câmera, RFID e potenciômetro
Autor: Alex Luiz Cibien E Silva
Data de início: setembro de 2024

**************************************************************"""

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
        (self.PARAR, self.PARAR, self.PARAR),  # Vai do index 1 para frente
        (self.PARAR, self.PARAR, self.PEDESTRE),
        (self.PARAR, self.PARAR, self.VEL20KMH),
        (self.PARAR, self.N_DETECTOU, self.N_DETECTOU),
        (self.PARAR, self.N_DETECTOU, self.PARAR),
        (self.PARAR, self.N_DETECTOU, self.VEL20KMH),
        (self.PARAR, self.N_DETECTOU, self.PEDESTRE),
        (self.PARAR, self.VEL20KMH, self.PARAR),
        (self.PARAR, self.VEL20KMH, self.PEDESTRE),
        (self.PARAR, self.VEL20KMH, self.VEL20KMH),
        ([self.ACELERAR, self.OCIOSO], self.PARAR, self.PARAR),
        ([self.ACELERAR, self.OCIOSO], self.PARAR, self.PEDESTRE),
        ([self.ACELERAR, self.OCIOSO], self.PARAR, self.VEL20KMH),
        ([self.ACELERAR, self.OCIOSO], self.N_DETECTOU, self.N_DETECTOU),
        ([self.ACELERAR, self.OCIOSO], self.N_DETECTOU, self.PARAR),
        ([self.ACELERAR, self.OCIOSO], self.N_DETECTOU, self.PEDESTRE),
        ([self.ACELERAR, self.OCIOSO], self.N_DETECTOU, self.VEL20KMH),
        ([self.ACELERAR, self.OCIOSO], self.VEL20KMH, self.VEL20KMH),
        ([self.ACELERAR, self.OCIOSO], self.VEL20KMH, self.PEDESTRE),
        ([self.ACELERAR, self.OCIOSO], self.VEL20KMH, self.PARAR), # Este é o index 20
    ]
  
  def findMonteCarloIndex(self, pot, cam, rfid) -> int:
    for i, (p, c, r) in enumerate(self.patterns):
      # Verifica se `p` é uma lista (ou conjunto de valores) ou um valor único
      pot_matches = pot in p if isinstance(p, list) else pot == p
      if pot_matches and cam == c and rfid == r:
        return i + 1
    return -1

  def generateSimulationNumbers(self) -> tuple:
    value_from_pot = randint(1, 3)
    value_from_cam = randint(2, 4)
    value_from_rfid = randint(2, 5)
    indexMC = self.findMonteCarloIndex(value_from_pot, value_from_cam, value_from_rfid)
    
    return value_from_pot, value_from_cam, value_from_rfid, indexMC

if __name__ == "__main__":
  INTERVALO = 1
  last_time = time()
  sim = MonteCarloSim()

  count = 0
  while count < 5:
    now_time = time()

    if now_time - last_time >= INTERVALO:
      pot_value, cam_value, rfid_value, monteCarloIndex = sim.generateSimulationNumbers()

      print(f'Este é o valor do potenciômetro: {pot_value}')
      print(f'Este é o valor do potenciômetro: {cam_value}')
      print(f'Este é o valor do potenciômetro: {rfid_value}')
      print(f'Este é o valor do índice de Monte Carlo: {monteCarloIndex}')
      
      
      last_time = now_time
      count += 1