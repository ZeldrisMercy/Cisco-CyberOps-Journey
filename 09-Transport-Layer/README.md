# 📁 Module 09: Transport Layer (TCP & UDP) & Network Analysis

> [!NOTE]
> **Resumo Executivo:** Este módulo explora a **Camada de Transporte (Camada 4 do modelo OSI)**, responsável por mover dados entre aplicações através da rede. Discutiremos suas principais responsabilidades, como segmentação, multiplexação e o uso de portas.
> O módulo detalha os dois principais protocolos desta camada: **TCP (Transmission Control Protocol)**, que é confiável e orientado a conexão, e o **UDP (User Datagram Protocol)**, que é rápido e de "melhor esforço". 
> Por fim, trazemos a aplicação tática desses conceitos através de ferramentas essenciais de CyberOps: a análise de tráfego com **Wireshark** e o escaneamento de portas com **Nmap**.

---

## 🧭 9.1 Responsabilidades da Camada de Transporte

Enquanto a camada de Rede (IP) foca em levar o pacote do host de origem ao host de destino, a Camada de Transporte garante que os dados cheguem ao **aplicativo correto**. Suas principais funções incluem:

* **Rastreamento de Conversas (Tracking Conversations):** Mantém e acompanha múltiplas conversas ocorrendo simultaneamente (ex: abas do navegador, e-mail, chat).
* **Segmentação e Remontagem:** Divide os dados da aplicação em blocos menores (segmentos ou datagramas) para facilitar o transporte e os remonta no destino.
* **Identificação de Aplicações:** Utiliza **números de porta** para direcionar o tráfego para a aplicação correta.
* **Multiplexação de Conversas:** Permite que diferentes fluxos de comunicação sejam intercalados na mesma rede sem que um monopolize a banda.

### 9.1.10 Socket Pairs

Um **Socket** é a combinação de um endereço IP e um número de porta.
Para que a comunicação ocorra, são necessários dois sockets (um par):
* **Socket de Origem:** IP de Origem + Porta de Origem (geralmente uma porta dinâmica/efêmera).
* **Socket de Destino:** IP de Destino + Porta de Destino (geralmente uma *well-known port* como 80 para HTTP ou 25 para SMTP).

---

## ⚖️ 9.1.3 TCP vs. UDP

A camada de transporte oferece dois protocolos distintos, dependendo da necessidade da aplicação.

### TCP (Transmission Control Protocol)
* **Características:** *Stateful* (rastreia o estado da sessão), confiável, orientado a conexão.
* **Overhead:** Cabeçalho de **20 bytes**.
* **Uso:** HTTP, FTP, SMTP (quando a entrega perfeita dos dados é mais importante que a velocidade).
* **Campos do Cabeçalho:** Source Port, Destination Port, Sequence Number, Acknowledgment Number, Header Length, Reserved, Control Bits (Flags), Window, Checksum, Urgent.

### UDP (User Datagram Protocol)
* **Características:** *Stateless*, não confiável ("best effort"), sem conexão. Não retransmite dados perdidos.
* **Overhead:** Cabeçalho muito leve de apenas **8 bytes**.
* **Uso:** Streaming de vídeo, VoIP, DNS, Jogos online (onde a velocidade e a continuidade são mais importantes que um pacote perdido).
* **Campos do Cabeçalho:** Source Port, Destination Port, Length, Checksum.

---

## 🤝 9.2 TCP Communication Process

O TCP gerencia cada sessão de forma meticulosa, utilizando "Flags" (Bits de Controle) no seu cabeçalho. As principais flags são: **SYN, ACK, FIN, RST, PSH, URG**.

### 9.2.2 Estabelecimento de Conexão (Three-Way Handshake)
Antes de enviar qualquer dado, o TCP estabelece uma sessão em 3 passos:
1.  **SYN:** O Cliente envia um segmento com a flag SYN para solicitar a conexão (informa seu número de sequência inicial).
2.  **SYN-ACK:** O Servidor responde com SYN e ACK, reconhecendo a solicitação do cliente e enviando seus próprios parâmetros.
3.  **ACK:** O Cliente responde com um ACK final. A conexão está estabelecida.

### 9.2.3 Encerramento de Sessão (Four-Way Termination)
Para encerrar a conexão de forma limpa, utiliza-se a flag FIN:
1.  **FIN:** O Cliente (ou servidor) envia um FIN indicando que não tem mais dados para enviar.
2.  **ACK:** O receptor confirma o recebimento do FIN.
3.  **FIN:** O receptor envia seu próprio FIN para encerrar a sua via de comunicação.
4.  **ACK:** O iniciador confirma com um ACK. A conexão é fechada.

---

## 🛡️ 9.3 TCP Reliability & Flow Control

O TCP garante que os dados cheguem intactos, em ordem e sem sobrecarregar a rede ou o receptor.

* **Reordenação de Segmentos:** Segmentos podem tomar rotas diferentes e chegar fora de ordem. O TCP usa o *Sequence Number* para reorganizá-los.
* **Perda de Dados e Retransmissão:** O receptor usa *Acknowledgment Numbers* (ACK) para informar qual o próximo byte que espera receber. Se o remetente não recebe o ACK no tempo esperado, ele retransmite o segmento.
* **Controle de Fluxo (Window Size):** O campo *Window* indica a quantidade de dados (em bytes) que o destino pode aceitar de uma vez. O tamanho da janela pode ser ajustado dinamicamente.
* **Maximum Segment Size (MSS):** É o maior tamanho de payload TCP que um dispositivo pode receber. Em uma rede Ethernet padrão (MTU 1500), o MSS costuma ser **1460 bytes** (1500 - 20 bytes IP - 20 bytes TCP).
* **Prevenção de Congestionamento:** Se os ACKs demoram, o TCP assume que a rede está congestionada e reduz a taxa de envio automaticamente.

---

## 📑 Tactical Field Report: Lab Executions (Wireshark & Nmap)

Neste módulo, executamos laboratórios práticos focados na visibilidade da Camada de Transporte.

### 🦈 Laboratório 1: Analisando o 3-Way Handshake com Wireshark
* **Cenário:** Captura de tráfego (usando `tcpdump` no terminal Mininet) durante uma requisição HTTP.
* **Análise:** Ao aplicar o filtro `tcp` no Wireshark, isolamos os pacotes da camada de transporte.
* **Observação de Flags:** Foi possível expandir o cabeçalho TCP no Wireshark para visualizar os *Control Bits* em ação: `[SYN]`, seguido de `[SYN, ACK]`, e finalmente `[ACK]`, comprovando a teoria do handshake em um ambiente real. O Wireshark também mostra os números de sequência e reconhecimento (Sequence/Ack numbers) evoluindo de 0 para 1.

### 🗺️ Laboratório 2: Explorando o Nmap (Network Mapper)
* **Propósito:** Ferramenta open-source vital para auditoria de segurança e descoberta de rede (Port Scanning).
* **Comando chave:** `nmap -A -T4 <alvo>`
    * `-A`: Habilita detecção de SO (Sistema Operacional), detecção de versão de serviços, *script scanning* e *traceroute*.
    * `-T4`: Ajusta o *timing* para uma execução mais rápida (agressiva).
* **Resultados:** O Nmap retorna uma lista de portas, seus estados (`open`, `filtered`, `closed`) e o serviço/versão rodando nelas (ex: `22/tcp open ssh OpenSSH 8.2`). Portas *filtered* geralmente indicam a presença de um firewall bloqueando as sondagens (probes).
