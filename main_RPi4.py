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

#ajeitar as pastas e consertar o retorno -1 para ambos os casos de valor no mesmo índice

ultimo_tempo = time()
count = 0
while count < numberOfIterations:
  tempo_atual = time()

  if tempo_atual - ultimo_tempo >= INTERVALO:
    #pot_value, cam_value, rfid_value, monteCarloIndex = sim.generateSimulationNumbers()
    #indexDMkg = app.whichIndexMatrix(pot_value, cam_value, rfid_value)
    #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #app.saveLog(workbook, timestamp, pot_value, cam_value, rfid_value, monteCarloIndex, indexDMkg)

    print(sim.findMonteCarloIndex(1, 3, 3))  # Deve retornar o índice que corresponde ao primeiro padrão
    print(sim.findMonteCarloIndex(2, 3, 3))  # Deve retornar o mesmo índice
    print(sim.findMonteCarloIndex(1, 4, 3))  # Retorna o índice correspondente ao padrão adequado
    
    ultimo_tempo = tempo_atual
    count += 1