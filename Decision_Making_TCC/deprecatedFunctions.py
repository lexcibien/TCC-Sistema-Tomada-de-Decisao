def decisionFromInput(self, value_from_pot: int, value_from_cam: int, value_from_rfid: int) -> int: # substituida por decisionFromInputImproved
    if value_from_pot == self.PARAR:
      print("POT parou")
      
      if value_from_cam == self.PARAR:
        print("POT parou e CAM parou")
        if value_from_rfid == self.PARAR:
          print("POT parou, CAM parou e RFID parou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PEDESTRE:
          print("POT parou, CAM parou e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.VEL20KMH:
          print("POT parou, CAM parou e RFID 20 Km/h")
          print("o carro vai parar")
          return self.PARAR

      elif value_from_cam == self.N_DETECTOU:
        print("POT parou e CAM não detectou")
        if value_from_rfid == self.N_DETECTOU:
          print("POT parou, CAM não detectou e RFID não detectou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PARAR:
          print("POT parou, CAM não detectou e RFID parou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.VEL20KMH:
          print("POT parou, CAM não detectou e RFID 20 Km/h")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PEDESTRE:
          print("POT parou, CAM não detectou e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR

      elif value_from_cam == self.VEL20KMH:
        print("POT parou e CAM 20 Km/h")
        if value_from_rfid == self.PARAR:
          print("POT parou, CAM 20 Km/h e RFID parou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PEDESTRE:
          print("POT parou, CAM 20 Km/h e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.VEL20KMH:
          print("POT parou, CAM 20 Km/h e RFID 20 Km/h")
          print("o carro vai parar")
          return self.PARAR

    elif value_from_pot in (self.ACELERAR, self.OCIOSO):
      print("POT acelerou")

      if value_from_cam == self.PARAR:
        print("POT acelerou e CAM parou")
        if value_from_rfid == self.PARAR:
          print("POT acelerou, CAM parou e RFID parou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PEDESTRE:
          print("POT acelerou, CAM parou e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.VEL20KMH:
          print("POT acelerou, CAM parou e RFID 20 Km/h")
          print("o carro vai parar")
          return self.PARAR

      elif value_from_cam == self.N_DETECTOU:
        print("POT acelerou e CAM não detectou")
        if value_from_rfid == self.N_DETECTOU:
          print("POT acelerou, CAM não detectou e RFID não detectou")
          print("o carro vai acelerar sem limite")
          return self.N_LIMITE
        elif value_from_rfid == self.PARAR:
          print("POT acelerou, CAM não detectou e RFID parou")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PEDESTRE:
          print("POT acelerou, CAM não detectou e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.VEL20KMH:
          print("POT acelerou, CAM não detectou e RFID 20 Km/h")
          print("o carro vai manter em 20km/h")
          return self.VEL20KMH

      elif value_from_cam == self.VEL20KMH:
        print("POT acelerou e CAM 20 Km/h")
        if value_from_rfid == self.VEL20KMH:
          print("POT acelerou, CAM 20 Km/h e RFID 20 Km/h")
          print("o carro vai manter em 20km/h")
          return self.VEL20KMH 
        elif value_from_rfid == self.PEDESTRE:
          print("POT acelerou, CAM 20 Km/h e RFID pedestre")
          print("o carro vai parar")
          return self.PARAR
        elif value_from_rfid == self.PARAR:
          print("POT acelerou, CAM 20 Km/h e RFID parou")
          print("o carro vai parar")
          return self.PARAR

    return self.PARAR
