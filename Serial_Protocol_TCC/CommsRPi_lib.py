"""**************************************************************

Biblioteca para comunicação com o Arduino N
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

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

  def sendMessageHandler(self, ack_string, info_int=''):
    mensagem = f"{ack_string}:{info_int}\n"
    try:
      self.serial_port.write(mensagem.encode("ascii"))  # Envia a mensagem com codificacao ASCII
      print(f"Mensagem enviada: {mensagem.strip()}")
    except UnicodeEncodeError as e:
      print(f"Erro ao enviar mensagem: {e}")

  def changeNum(self, number):
    number += 10
    if number > 200:
      number = 100  # Limita a velocidade
    print(f"Nova velocidade: {number}")

  def sendMessage(self, ack_string, info_int, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
      self.sendMessageHandler(ack_string, info_int)
      hasReceived, valueType, value = self.receiveMessage()
      if hasReceived and valueType == "ACK":
        self.changeNum(info_int)
        return
      attempts += 1
      print(f"Tentativa {attempts} falhou. Reenviando...")
      sleep(0.1)
    print("Máximo de tentativas de envio alcançado, encerrando operação.")

  def receiveMessage(self) -> tuple:
    if self.serial_port.in_waiting > 0:
      try:
        resposta = self.serial_port.readline().decode("ascii").strip()
        if resposta == "ACK":
          print("Resposta recebida: ACK")
          return True, "ACK", None

        elif resposta.startswith("PotRes:"):
          valor_pot = int(resposta.split(":")[1])
          return True, "PotRes", valor_pot

        elif resposta.startswith("VopRes:"):
          valor_vop = float(resposta.split(":")[1])
          return True, "VopRes", valor_vop

      except UnicodeDecodeError as e:
        print(f"Erro ao decodificar resposta: {e}")
      except ValueError as e:
        print(f"Erro ao converter valor: {e}")
    else:
      print("Nenhuma resposta ou resposta inválida.")
    return False, None, None


  def reqVoltagePot(self) -> int:
    self.sendMessageHandler("PotReq")
    hasReceived, valueType, valuePot = self.receiveMessage()
    if hasReceived and valueType == "PotRes":
      sleep(0.003)
      return valuePot
    else:
      print("Erro: Mensagem de resposta de Potência esperada, mas outra foi recebida ou houve falha.")
      return None


  def reqValuePot(self) -> float:
    self.sendMessageHandler("VopReq")
    hasReceived, valueType, voltagePot = self.receiveMessage()
    if hasReceived and valueType == "VopRes":
      sleep(0.003)
      return voltagePot
    else:
      print("Erro: Mensagem de resposta de Voltagem esperada, mas outra foi recebida ou houve falha.")
      return None

from time import sleep, time

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
  usleep = lambda x: sleep(x/1000000.0)

  transmissor = Comms(SERIAL_PORT, BAUD_RATE, SERIAL_TIMEOUT_MS)
  print("Iniciando Transmissor")

  while True:
    tempo_atual = time()
    
    if tempo_atual - lastTime1 >= (INTERVALO / 10):
      raw_PotValue = transmissor.reqValuePot()
      PotVoltageValue = transmissor.reqVoltagePot()
      print(f"Valor do potenciômetro: {raw_PotValue}")
      print(f"Valor de tensão: {PotVoltageValue}")
      
      lastTime1 = tempo_atual
