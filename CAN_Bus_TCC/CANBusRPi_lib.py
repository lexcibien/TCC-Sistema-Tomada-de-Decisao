"""**************************************************************

Biblioteca para comunicação com rede CAN e inversor de tração
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

import os
import can

class canBus:
  
  CAN_Channel = ''
  CAN_bitrate = ''
  CAN_id = 0
  CAN_dlc = 0

  def __init__(self, _channel, _bustype, _bitrate):
    self.can0 = can.interface.Bus(channel=_channel, bustype=_bustype)
    print("iniciando biblioteca")
    self.CAN_Channel = _channel
    self.CAN_bitrate = _bitrate

  def openCommCAN(self):
    # Configurações da interface CAN
    commandLine = 'sudo ip link set ' + self.CAN_Channel + ' type can bitrate ' + self.CAN_bitrate
    os.system(commandLine)
    commandLine = 'sudo ifconfig ' + self.CAN_Channel + ' up'
    os.system(commandLine)

  def closeCommCAN(self):
    # Desliga a interface CAN
    commandLine = 'sudo ifconfig ' + self.CAN_Channel + ' down'
    os.system(commandLine)
  
  # Função para enviar a mensagem CAN com até 4 informações
  def sendMessageCAN(self, _CAN_id=0x00, info1=None, info2=None, info3=None, info4=None):
      
    self.openCommCAN()

    # Substitui valores None por 0
    info1 = 0 if info1 is None else info1
    info2 = 0 if info2 is None else info2
    info3 = 0 if info3 is None else info3
    info4 = 0 if info4 is None else info4

    # Converte cada info em 2 bytes separados (big-endian)
    data = [
        (info1 >> 8) & 0xFF, info1 & 0xFF,  # Byte alto e baixo de info1
        (info2 >> 8) & 0xFF, info2 & 0xFF,  # Byte alto e baixo de info2
        (info3 >> 8) & 0xFF, info3 & 0xFF,  # Byte alto e baixo de info3
        (info4 >> 8) & 0xFF, info4 & 0xFF   # Byte alto e baixo de info4
    ]

    # Envia a mensagem CAN
    msg = can.Message(arbitration_id=_CAN_id, data=data, is_extended_id=False)
    
    self.can0.send(msg)

    self.closeCommCAN()

  # Função para receber a mensagem CAN e retornar uma tupla com info1, info2, info3, info4
  def receivedMessageCAN(self):
    # Configurações da interface CAN
    self.openCommCAN()

    # Recebe a mensagem CAN
    msg = self.can0.recv(0.6)
    self.CAN_id = msg.arbitration_id
    self.CAN_dlc = msg.dlc

    if msg is None:
      print('Timeout occurred, no message.')
      return None, None, None, None
    else:
      print('Received message:', msg)
        
      # Reconstrói as informações originais de 2 bytes cada
      info1 = (msg.data[0] << 8) | msg.data[1]
      info2 = (msg.data[2] << 8) | msg.data[3]
      info3 = (msg.data[4] << 8) | msg.data[5]
      info4 = (msg.data[6] << 8) | msg.data[7]
      
      # Desliga a interface CAN
      self.closeCommCAN()

      # Retorna as informações como uma tupla
      return info1, info2, info3, info4

if __name__ == "__main__":   
  canBus = canBus(_channel='can0', _bustype='socketcan', _bitrate='1000000')

  # Enviando apenas info1 e info2, info3 e info4 serão zeros
  canBus.sendMessageCAN(300, 400)

  # Recebendo a mensagem e atribuindo os valores a info1, info2, info3, info4
  info1, info2, info3, info4 = canBus.receivedMessageCAN()
  print(f'Info1: {info1}, Info2: {info2}, Info3: {info3}, Info4: {info4}')
