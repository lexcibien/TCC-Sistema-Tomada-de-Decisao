"""**************************************************************

Programação para simulação do sistema de tomada de decisão
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

#AVISO: Rodar esse código irá substituir a matriz de confusão já criada

from Decision_Making_TCC.DecisionMkgRPI_lib import DecisionMkg
from Simulacao_Monte_Carlo.monteCarloSim import MonteCarloSim
from numpy import zeros
from pandas import DataFrame

numberOfIterations = 100000
confusion_matrix = zeros((20, 20), dtype=int)

sim = MonteCarloSim()
app = DecisionMkg()

unmatched_count = 0
for _ in range(numberOfIterations):
  pot_value, cam_value, rfid_value, indexMC = sim.generateSimulationNumbers()
  indexDMkg = app.whichIndexMatrix(pot_value, cam_value, rfid_value)
  
  if 0 <= indexMC <= 20 and 0 <= indexDMkg <= 20:
    confusion_matrix[indexMC-1][indexDMkg-1] += 1
  else:
    unmatched_count += 1

  #print(f'Este é o valor do potenciômetro: {pot_value}')
  #print(f'Este é o valor do potenciômetro: {cam_value}')
  #print(f'Este é o valor do potenciômetro: {rfid_value}')
  #print(f'Este é o valor do índice de Monte Carlo: {indexMC}')
  #print(f'Este é o valor do índice da tomada de decisão: {indexDMkg}')
print(confusion_matrix)

header = [str(indexMatrix) for indexMatrix in range(1, 21)]
df_confusion_matrix = DataFrame(confusion_matrix, index=header, columns=header)

file_name = "matriz_confusao.xlsx"
df_confusion_matrix.to_excel(file_name, sheet_name="Matriz de Confusão")

print(f"Matriz de confusão exportada com sucesso para '{file_name}'")
print(f"\nTotal de resultados da simulação não encontrados na matriz de confusão: {unmatched_count}")
