"""**************************************************************

Biblioteca para comunicação com o Arduino N
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

from time import sleep, time

from serial import Serial

# configurar o /boot/firmware/config.txt
# dtoverlay=pi3-miniuart-bt
# dtoverlay=disable-bt
# enable_uart=1

# raspi-gpio set 14 a0  # Definir GPIO14 como TXD0 (função UART)
# raspi-gpio set 15 a0  # Definir GPIO15 como RXD0 (função UART)

class Comms:
  def __init__(self, serial_port, baud_rate, timeout_ms):
    self.timeout = timeout_ms / 1000.0  # Converte o timeout para segundos
    self.serial_port = Serial(serial_port, baud_rate, timeout=self.timeout)  # Usando UART no GPIO
    self.serial_port.flush()  # Limpa o buffer da porta serial

  def send_message_handler(self, ack_string, info_int=''):
    mensagem = f"{ack_string}:{info_int}\n"
    try:
      self.serial_port.write(mensagem.encode("ascii"))  # Envia a mensagem com codificacao ASCII
      print(f"Mensagem enviada: {mensagem.strip()}")
    except UnicodeEncodeError as e:
      print(f"Erro ao enviar mensagem: {e}")

  def change_num(self, number):
    number += 10
    if number > 200:
      number = 100  # Limita a velocidade
    print(f"Nova velocidade: {number}")

  def receive_message(self) -> tuple:
    if self.serial_port.in_waiting > 0:
      try:
        resposta = self.serial_port.readline().decode("ascii").strip()
        if resposta == "ACK":
          print("Resposta recebida: ACK")
          return True, "ACK", None

        if resposta.startswith("PotRes:"):
          valor_pot = int(resposta.split(":")[1])
          return True, "PotRes", valor_pot

        if resposta.startswith("VopRes:"):
          valor_vop = float(resposta.split(":")[1])
          return True, "VopRes", valor_vop

      except UnicodeDecodeError as e:
        print(f"Erro ao decodificar resposta: {e}")
      except ValueError as e:
        print(f"Erro ao converter valor: {e}")
    else:
      print("Nenhuma resposta ou resposta inválida.")
    return False, None, None

  def send_message(self, ack_string, info_int, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
      self.send_message_handler(ack_string, info_int)
      has_received, value_type, _ = self.receive_message()
      if has_received and value_type == "ACK":
        self.change_num(info_int)
        return
      attempts += 1
      print(f"Tentativa {attempts} falhou. Reenviando...")
      sleep(0.1)
    print("Máximo de tentativas de envio alcançado, encerrando operação.")

  def req_voltage_pot(self) -> int | None:
    self.send_message_handler("PotReq")
    has_received, value_type, value_pot = self.receive_message()
    if has_received and value_type == "PotRes":
      sleep(0.003)
      return value_pot
    print("Erro: Mensagem de resposta de Potência esperada, mas outra foi recebida ou houve falha.")
    return None


  def req_value_pot(self) -> float | None:
    self.send_message_handler("VopReq")
    has_received, value_type, voltage_pot = self.receive_message()
    if has_received and value_type == "VopRes":
      sleep(0.003)
      return voltage_pot
    print("Erro: Mensagem de resposta de Voltagem esperada, mas outra foi recebida ou houve falha.")
    return None

if __name__ == "__main__":
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
  def usleep(x): 
    sleep(x/1000000.0)

  transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
  print("Iniciando Transmissor")

  while True:
    tempo_atual = time()
    
    if tempo_atual - lastTime1 >= (INTERVALO / 10):
      raw_PotValue = transmissor.req_value_pot()
      PotVoltageValue = transmissor.req_voltage_pot()
      print(f"Valor do potenciômetro: {raw_PotValue}")
      print(f"Valor de tensão: {PotVoltageValue}")
      
      lastTime1 = tempo_atual
