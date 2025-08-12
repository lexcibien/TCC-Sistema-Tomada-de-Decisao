"""**************************************************************

Biblioteca para tomada de decisão entre a câmera, RFID e potenciômetro
Autor: Alex Luiz Cibien E Silva
Data de início: setembro de 2024

**************************************************************"""

from datetime import datetime
from random import randint
from time import time

from DecisionMkgRPI_lib import DecisionMkg

app = DecisionMkg()


actionList: list = []


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
            (3, 3, 3),  # Padrão para index 0
            (3, 3, 5),  # Padrão para index 1
            # Adicione outros padrões conforme necessário
        ]
        # adicionar as outras placas e testar removendo a parte do DecisionMaking repetido.

    def find_pattern_index(self, pot, cam, rfid):
        for i, (p, c, r) in enumerate(self.patterns):
            if (pot, cam, rfid) == (p, c, r):
                return i + 1
        return -1

    def generate_simulation_numbers(self) -> tuple:
        value_from_pot = randint(1, 3)
        value_from_cam = randint(2, 4)
        value_from_rfid = randint(2, 5)
        index_monte_carlo = app.which_index_matrix(
            value_from_pot, value_from_cam, value_from_rfid
        )

        return value_from_pot, value_from_cam, value_from_rfid, index_monte_carlo


if __name__ == "__main__":
    INTERVALO = 1
    ultimo_tempo = time()
    sim = MonteCarloSim()
    workbook = app.initialize_excel()

    count = 0
    while count < 5:
        tempo_atual = time()

        if tempo_atual - ultimo_tempo >= INTERVALO:
            pot_value, cam_value, rfid_value, monteCarloIndex = (
                sim.generate_simulation_numbers()
            )
            indexDMkg = app.which_index_matrix(pot_value, cam_value, rfid_value)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            app.save_log(
                workbook,
                timestamp,
                pot_value,
                cam_value,
                rfid_value,
                monteCarloIndex,
                indexDMkg,
            )

            ultimo_tempo = tempo_atual
            count += 1
