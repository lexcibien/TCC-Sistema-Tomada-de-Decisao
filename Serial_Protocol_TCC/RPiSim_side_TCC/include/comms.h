#ifndef _COMMS_H_
#define _COMMS_H_

#include <Arduino.h>

class Comms { //transmissor
private:
  int velocidade;
  int timeout;
  bool respostaRecebida;

public:
  Comms(int velInicial, int timeoutMs) {
    velocidade = velInicial;
    timeout = timeoutMs;
    respostaRecebida = false;
    Serial.setTimeout(timeout); // Define o tempo de espera para a leitura serial
  }

  void enviarMensagem() {
    String mensagem = "velo:" + String(velocidade) + "\n";
    Serial.print(mensagem); // Envia a mensagem
    digitalWrite(LED_BUILTIN, LOW);
  }

  bool verificarResposta() {
    String resposta = Serial.readStringUntil('\n'); // Lê até receber \n ou atingir o timeout
    if (resposta == "ACK") {
      digitalWrite(LED_BUILTIN, HIGH);
      respostaRecebida = true;
    } else {
      digitalWrite(LED_BUILTIN, LOW);
      respostaRecebida = false;
    }
    return respostaRecebida;
  }

  void alterarVelocidade() {
    // Incrementa ou altera a velocidade
    velocidade += 10;
    if (velocidade > 200) {
      velocidade = 100; // Limite superior para a velocidade
    }
  }    
};

Comms transmissor(100, 500); // Timeout de 200ms

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  
  Serial.begin(115200); // Inicia a comunicação serial
  Serial.println("Iniciando Transmissor");
}

void loop() {
  transmissor.enviarMensagem();

  // Esperar mais tempo por uma resposta
  if (transmissor.verificarResposta()) {
    transmissor.alterarVelocidade(); // Resposta correta recebida, envia nova velocidade
  } else {
    Serial.println("Reenviando..."); // Não recebeu resposta, reenvia
  }

  delayMicroseconds(1); // Tempo menor para evitar travamentos na comunicação
}

#endif // _COMMS_H_