"""**************************************************************

Programação para simulação do sistema de tomada de decisão
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""


from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from Simulacao_Monte_Carlo.monteCarloSim import MonteCarloSim
from datetime import datetime
from time import time, sleep

numberOfIterations = 1

INTERVALO = 0.1
app = DecisionMkg()
sim = MonteCarloSim()
workbook = app.initialize_excel()

ultimo_tempo = time()
count = 0
while count < numberOfIterations:
  tempo_atual = time()

  if tempo_atual - ultimo_tempo >= INTERVALO:
    pot_value, cam_value, rfid_value, monteCarloIndex = sim.generateSimulationNumbers()
    DMkgIndex = app.whichIndexMatrix(pot_value, cam_value, rfid_value)

    print(f'Este é o valor do potenciômetro: {pot_value}')
    print(f'Este é o valor do potenciômetro: {cam_value}')
    print(f'Este é o valor do potenciômetro: {rfid_value}')
    print(f'Este é o valor do índice de Monte Carlo: {monteCarloIndex}')
    print(f'Este é o valor do índice da tomada de decisão: {DMkgIndex}')

    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f'Este é o timestamp: {timestamp}')
    #app.saveLog(workbook, timestamp, pot_value, cam_value, rfid_value, monteCarloIndex, DMkgIndex)

    ultimo_tempo = tempo_atual
    count += 1