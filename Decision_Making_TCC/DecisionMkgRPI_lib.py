"""**************************************************************

Biblioteca para tomada de decisão entre a câmera, RFID e potenciômetro
Autor: Alex Luiz Cibien E Silva
Data de início: setembro de 2024

**************************************************************"""


from openpyxl import Workbook, load_workbook
from datetime import datetime
from time import time, sleep
from os import path

class DecisionMkg:

  POT_reading:int = 0
  POT_value:int = 0
  CAMERA_value:int = 0
  RFID_value:int = 0
  Vel_value:int = 0
  VelReal_value:int = 0
  car_hadStopped:bool = 0
  last_detected_sign:int = None
  previous_detected_sign:int = None

  PEDESTRE = 5
  VEL20KMH = 4
  PARAR = 3
  OCIOSO = 2
  N_DETECTOU = 2
  N_LIMITE = 2
  ACELERAR = 1

  def __init__(self):
    print("iniciando biblioteca Decision Making")

  def getCamValue(self, _cam_value) -> int:    
    if _cam_value == '20km/h':
      self.CAMERA_value = self.VEL20KMH
    elif _cam_value == 'PARE':
      self.CAMERA_value = self.PARAR
    elif _cam_value == '':
      self.CAMERA_value = self.N_DETECTOU
    
    print(f"O valor da camera é: {self.CAMERA_value}")
    
    return self.CAMERA_value

  def getPotValue(self, _pot_reading) -> int:
    if _pot_reading >= 10:
      self.POT_value = self.ACELERAR
    elif _pot_reading <= -10:
      self.POT_value = self.PARAR
    else:
      self.POT_value = self.OCIOSO
    
    print(f"O valor do potenciometro é: {self.POT_value}")
    
    return self.POT_value
    
  def getRFIDValue(self) -> int:
    if self.RFID_value == self.VEL20KMH:
      self.RFID_value = self.VEL20KMH
    elif self.RFID_value == self.N_DETECTOU:
      self.RFID_value = self.N_DETECTOU
    elif self.RFID_value == self.PEDESTRE:
      self.RFID_value = self.PEDESTRE
    elif self.RFID_value == self.PARAR:
      self.RFID_value = self.PARAR
    
    print(f"O valor do RFID é: {self.RFID_value}")
    
    return self.RFID_value
  
  def update_detected_sign(self, new_sign: int) -> None:
    self.previous_detected_sign = self.last_detected_sign
    self.last_detected_sign = new_sign

  def brakeAndGoCommand(self, reading_from_pot: int) -> None:
    if self.car_hadStopped:
      self.Vel_value = 0
      sleep(5) # Aguarda cinco segundos por segurança
      
      if reading_from_pot == self.ACELERAR:
        return
      else:
        self.car_hadStopped = False
  
  def decisionFromInputImproved(self, value_from_pot: int, value_from_cam: int, value_from_rfid: int) -> int:
    if self.PARAR in (value_from_pot, value_from_cam, value_from_rfid):
      print(f"POT {value_from_pot}, CAM {value_from_cam} e RFID {value_from_rfid}")
      return self.PARAR
    elif value_from_rfid == self.PEDESTRE:
      print(f"POT {value_from_pot}, CAM {value_from_cam} e RFID {value_from_rfid}")
      return self.PEDESTRE
    
    elif value_from_pot in (self.ACELERAR, self.OCIOSO):
      print(f"POT {value_from_pot}")
      if value_from_cam == self.N_DETECTOU:
        print(f"CAM {value_from_cam}")
        if value_from_rfid == self.N_DETECTOU:
          print(f"RFID {value_from_rfid}")
          return self.N_LIMITE
        elif value_from_rfid == self.VEL20KMH:
          print(f"RFID {value_from_rfid}")
          return self.VEL20KMH
        
      elif value_from_cam == self.VEL20KMH:
        print(f"CAM {value_from_cam}")
        if value_from_rfid == self.N_DETECTOU:
          print(f"RFID {value_from_rfid}")
          return self.N_LIMITE
        elif value_from_rfid == self.VEL20KMH:
          print(f"RFID {value_from_rfid}")
          return self.VEL20KMH
        
    return self.PARAR
  
  # simulação de montecarlo - jogar dados aleatórios
  # 100000 dados
  # utilizar uma lista com as ações e respostas em ordem aleatória, isto é não precisa ser 1,2,3...22, o importante é ser o mais aleatório possível
  # a simulação de montecarlo pode ser utilizada para validar
  # a entrada é o "montecarlo" e a saída é o meu programa (whichIndexMatrix)
  # da de fazer tudo pelo pc

  def whichIndexMatrix(self, value_from_pot: int, value_from_cam: int, value_from_rfid: int) -> int:
    if value_from_pot == self.PARAR:
      if value_from_cam == self.PARAR:
        if value_from_rfid == self.PARAR:
          return 1
        elif value_from_rfid == self.PEDESTRE:
          return 2
        elif value_from_rfid == self.VEL20KMH:
          return 3
      elif value_from_cam == self.N_DETECTOU:
        if value_from_rfid == self.N_DETECTOU:
          return 4
        elif value_from_rfid == self.PARAR:
          return 5
        elif value_from_rfid == self.VEL20KMH:
          return 6
        elif value_from_rfid == self.PEDESTRE:
          return 7
      elif value_from_cam == self.VEL20KMH:
        if value_from_rfid == self.PARAR:
          return 8
        elif value_from_rfid == self.PEDESTRE:
          return 9
        elif value_from_rfid == self.VEL20KMH:
          return 10
        
    elif value_from_pot in (self.ACELERAR, self.OCIOSO):
      if value_from_cam == self.PARAR:
        if value_from_rfid == self.PARAR:
          return 11
        elif value_from_rfid == self.PEDESTRE:
          return 12
        elif value_from_rfid == self.VEL20KMH:
          return 13
      elif value_from_cam == self.N_DETECTOU:
        if value_from_rfid == self.N_DETECTOU:
          return 14
        elif value_from_rfid == self.PARAR:
          return 15
        elif value_from_rfid == self.PEDESTRE:
          return 16
        elif value_from_rfid == self.VEL20KMH:
          return 17     
      elif value_from_cam == self.VEL20KMH:
        if value_from_rfid == self.VEL20KMH:
          return 18
        elif value_from_rfid == self.PEDESTRE:
          return 19
        elif value_from_rfid == self.PARAR:
          return 20
        
  def executeDecision(self, valueFromDecision: int) -> None:
    if valueFromDecision == self.PARAR:
      self.brakeAndGoCommand(potentiometer_reading)
    elif valueFromDecision == self.N_LIMITE:
      self.Vel_value == potentiometer_reading/2
    elif valueFromDecision == self.VEL20KMH:
      if self.VelReal_value <= 18:
        print("deixa o comando do motorista")
        self.Vel_value == potentiometer_reading/2
      elif self.VelReal_value >= 22:
        print("abaixa pra 20km/hr")
        self.Vel_value == 20    
      
  def initialize_excel(self, filename="log_data.xlsx"):
    if path.exists(filename):
      workbook = load_workbook(filename)
    
    else:
      workbook = Workbook()
      sheet = workbook.active
      sheet.title = "DataLog"
      sheet.append(["Timestamp", "Potenciometro", "Camera", "RFID", "index de Entrada", "index de Saida"])      
      workbook.save(filename)

    return workbook
  
  def saveLog(self, workbook, _timestamp:str, value_from_pot:int, value_from_cam:int, value_from_rfid:int, 
              index_from_enter, index_from_exit, filename="log_data.xlsx") -> None:
    sheet = workbook.active
    _timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([_timestamp, value_from_pot, value_from_cam, value_from_rfid, index_from_enter, index_from_exit])
    workbook.save(filename)
    print(f"Dados salvos no Excel com timestamp {_timestamp}")

if __name__ == "__main__":
  from ..Sign_Detection_TCC.detection import getClassName, capture_photo, indexVal

  INTERVALO = 1
  ultimo_tempo = time() 
  app = DecisionMkg()
  workbook = app.initialize_excel()

  while True:
    tempo_atual = time()
    raw_cam_value = getClassName(indexVal)
    potentiometer_reading = app.POT_reading
    potentiometer_value = app.getPotValue()
    cam_value = app.getCamValue(raw_cam_value)
    rfid_value = app.getRFIDValue()

    if tempo_atual - ultimo_tempo >= INTERVALO:
      #decisionFromLogic = app.decisionFromInputImproved(potentiometer_value, cam_value, rfid_value)
      decisionFromLogic = app.decisionFromInputImproved(potentiometer_value, cam_value, rfid_value)
      #app.executeDecision(decisionFromLogic)
      indexExit = app.whichIndexMatrix(potentiometer_value, cam_value, rfid_value)
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      app.saveLog(workbook, timestamp, potentiometer_value, cam_value, rfid_value, 0, indexExit)
      capture_photo(timestamp)

      ultimo_tempo = tempo_atual