"""**************************************************************

Biblioteca para comunicação com rede CAN e inversor de tração
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

import os
import can

class canBus:
  """Classe para comunicação com rede CAN e inversor de tração"""
  
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
    """Função para abrir a comunicação CAN"""
    commandLine = 'sudo ip link set ' + self.CAN_Channel + ' type can bitrate ' + self.CAN_bitrate
    os.system(commandLine)
    commandLine = 'sudo ifconfig ' + self.CAN_Channel + ' up'
    os.system(commandLine)

  def closeCommCAN(self):
    """Desliga a interface CAN"""
    commandLine = 'sudo ifconfig ' + self.CAN_Channel + ' down'
    os.system(commandLine)
  
  # Função para enviar a mensagem CAN com até 4 informações
  def sendMessageCAN(self, _CAN_id=0x00, sendInfo1=None, sendInfo2=None, sendInfo3=None, sendInfo4=None):
    """Função para enviar a mensagem CAN com até 4 informações"""
      
    self.openCommCAN()

    # Substitui valores None por 0
    sendInfo1 = 0 if sendInfo1 is None else sendInfo1
    sendInfo2 = 0 if sendInfo2 is None else sendInfo2
    sendInfo3 = 0 if sendInfo3 is None else sendInfo3
    sendInfo4 = 0 if sendInfo4 is None else sendInfo4

    # Converte cada info em 2 bytes separados (big-endian)
    data = [
        (sendInfo1 >> 8) & 0xFF, sendInfo1 & 0xFF,  # Byte alto e baixo de info1
        (sendInfo2 >> 8) & 0xFF, sendInfo2 & 0xFF,  # Byte alto e baixo de info2
        (sendInfo3 >> 8) & 0xFF, sendInfo3 & 0xFF,  # Byte alto e baixo de info3
        (sendInfo4 >> 8) & 0xFF, sendInfo4 & 0xFF   # Byte alto e baixo de info4
    ]

    # Envia a mensagem CAN
    msg = can.Message(arbitration_id=_CAN_id, data=data, is_extended_id=False)
    
    self.can0.send(msg)

    self.closeCommCAN()

  # Função para receber a mensagem CAN e retornar uma tupla com info1, info2, info3, info4
  def receivedMessageCAN(self):
    """Função para receber a mensagem CAN e retornar uma tupla com info1, info2, info3, info4"""
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
      receiveInfo1 = (msg.data[0] << 8) | msg.data[1]
      receiveInfo2 = (msg.data[2] << 8) | msg.data[3]
      receiveInfo3 = (msg.data[4] << 8) | msg.data[5]
      receiveInfo4 = (msg.data[6] << 8) | msg.data[7]
      
      # Desliga a interface CAN
      self.closeCommCAN()

      # Retorna as informações como uma tupla
      return receiveInfo1, receiveInfo2, receiveInfo3, receiveInfo4

if __name__ == "__main__":   
  canBus = canBus(_channel='can0', _bustype='socketcan', _bitrate='1000000')

  # Enviando apenas info1 e info2, info3 e info4 serão zeros
  canBus.sendMessageCAN(300, 400)

  # Recebendo a mensagem e atribuindo os valores a info1, info2, info3, info4
  info1, info2, info3, info4 = canBus.receivedMessageCAN()
  print(f'Info1: {info1}, Info2: {info2}, Info3: {info3}, Info4: {info4}')
