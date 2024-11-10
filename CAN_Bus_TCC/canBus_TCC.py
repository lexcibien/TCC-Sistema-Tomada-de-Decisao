"""**************************************************************

Biblioteca para comunicação com rede CAN e inversor de tração
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

class canBus:

  __privateVar = None

  def __init__(self):
    print("iniciando biblioteca")

  def __privateFunction(self) :
    print("Acessei uma função privada")

  def imprimir(self):
    textInput = input("escreva um texto para imprimir: ")
    __privateVar = textInput
    self.__privateFunction()
    return __privateVar
  
if __name__ == "__main__":   
  msg1 = canBus()
  print(msg1.imprimir())