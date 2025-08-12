"""**************************************************************

Biblioteca para comunicação com rede CAN e inversor de tração
Autor: Alex Luiz Cibien E Silva
Data de início: abril de 2024

**************************************************************"""

import os

import can


class CanBus:
    """Classe para comunicação com rede CAN e inversor de tração"""

    can_channel = ""
    can_bitrate = ""
    can_id = 0
    can_dlc = 0

    def __init__(self, _channel, _bustype, _bitrate):
        self.can0 = can.interface.Bus(channel=_channel, bustype=_bustype)
        print("iniciando biblioteca")
        self.can_channel = _channel
        self.can_bitrate = _bitrate

    def open_comm_can(self):
        """Função para abrir a comunicação CAN"""
        command_line = (
            "sudo ip link set "
            + self.can_channel
            + " type can bitrate "
            + self.can_bitrate
        )
        os.system(command_line)
        command_line = "sudo ifconfig " + self.can_channel + " up"
        os.system(command_line)

    def close_comm_can(self):
        """Desliga a interface CAN"""
        command_line = "sudo ifconfig " + self.can_channel + " down"
        os.system(command_line)

    # Função para enviar a mensagem CAN com até 4 informações
    def send_message_can(
        self,
        _can_id=0x00,
        send_info1=None,
        send_info2=None,
        send_info3=None,
        send_info4=None,
    ):
        """Função para enviar a mensagem CAN com até 4 informações"""

        self.open_comm_can()

        # Substitui valores None por 0
        send_info1 = 0 if send_info1 is None else send_info1
        send_info2 = 0 if send_info2 is None else send_info2
        send_info3 = 0 if send_info3 is None else send_info3
        send_info4 = 0 if send_info4 is None else send_info4

        # Converte cada info em 2 bytes separados (big-endian)
        data = [
            (send_info1 >> 8) & 0xFF,
            send_info1 & 0xFF,  # Byte alto e baixo de info1
            (send_info2 >> 8) & 0xFF,
            send_info2 & 0xFF,  # Byte alto e baixo de info2
            (send_info3 >> 8) & 0xFF,
            send_info3 & 0xFF,  # Byte alto e baixo de info3
            (send_info4 >> 8) & 0xFF,
            send_info4 & 0xFF,  # Byte alto e baixo de info4
        ]

        # Envia a mensagem CAN
        msg = can.Message(arbitration_id=_can_id, data=data, is_extended_id=False)

        self.can0.send(msg)

        self.close_comm_can()

    # Função para receber a mensagem CAN e retornar uma tupla com info1, info2, info3, info4
    def received_message_can(self):
        """Função para receber a mensagem CAN e retornar uma tupla com info1, info2, info3, info4"""
        self.open_comm_can()

        # Recebe a mensagem CAN
        msg = self.can0.recv(0.6)
        self.can_id = msg.arbitration_id
        self.can_dlc = msg.dlc

        if msg is None:
            print("Timeout occurred, no message.")
            return None, None, None, None
        print("Received message:", msg)

        # Reconstrói as informações originais de 2 bytes cada
        receive_info1 = (msg.data[0] << 8) | msg.data[1]
        receive_info2 = (msg.data[2] << 8) | msg.data[3]
        receive_info3 = (msg.data[4] << 8) | msg.data[5]
        receive_info4 = (msg.data[6] << 8) | msg.data[7]

        # Desliga a interface CAN
        self.close_comm_can()

        # Retorna as informações como uma tupla
        return receive_info1, receive_info2, receive_info3, receive_info4


if __name__ == "__main__":
    canBus = CanBus(_channel="can0", _bustype="socketcan", _bitrate="1000000")

    # Enviando apenas info1 e info2, info3 e info4 serão zeros
    canBus.send_message_can(300, 400)

    # Recebendo a mensagem e atribuindo os valores a info1, info2, info3, info4
    info1, info2, info3, info4 = canBus.received_message_can()
    print(f"Info1: {info1}, Info2: {info2}, Info3: {info3}, Info4: {info4}")
