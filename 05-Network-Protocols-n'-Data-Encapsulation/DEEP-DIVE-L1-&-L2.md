# 📁 Base Fixa: Deep Dive nas Camadas 1 e 2 (Physical & Data Link)

> [!NOTE]
> **Resumo Executivo:** Antes de avançarmos para a Camada 3 (Rede/Roteamento) no Módulo 06, é crucial consolidar a base da infraestrutura. A Camada 1 dita *como* a energia (eletricidade, luz ou rádio) viaja pelo mundo físico. A Camada 2 dita *quem* pode falar e *quando* pode falar na rede local, garantindo que a energia crua seja transformada em dados organizados e livres de erros antes de serem entregues ao roteador. 

---

## ⚡ Camada 1: Física (O Motor do Transporte)

A Camada Física é responsável pela conversão de bits (0s e 1s) em sinais que podem ser transmitidos pelo meio físico. Ela não entende IPs, MACs ou protocolos; ela entende apenas voltagem, frequência e luz.

### 1. A Física das Ondas (Wireless e Rádio)
Toda a comunicação sem fio baseia-se na manipulação de campos eletromagnéticos (ondas/fótons).
* **Frequência e Comprimento de Onda:**
    * **2.4 GHz (Ondas Longas):** Possui alta **Difração** (capacidade de contornar obstáculos pesados como paredes e móveis) e baixa **Atenuação** (perda de energia). Chega mais longe, mas transporta menos dados.
    * **5 GHz (Ondas Curtas):** Altíssima capacidade de dados, mas sofre muita atenuação. Comporta-se quase como luz: se houver muitos obstáculos físicos (tijolo/concreto), o sinal "morre" rápido.
* **Fenômenos Físicos Críticos:**
    * **Reflexão:** Ondas batendo em metal/espelhos e ricocheteando (usado a favor no 5G/Wi-Fi moderno através da tecnologia MIMO).
    * **SNR (Signal-to-Noise Ratio):** A relação entre o "Sinal" (o que você quer ouvir) e o "Ruído" (interferência). Um SNR alto é vital para manter velocidades altas.



### 2. Modulação: Transformando Ondas e Luz em Bits
Ondas puras e lasers acesos não transmitem dados. Eles precisam ser "modulados" (alterados em frações de segundo):
* **No Cobre (Elétrico):** Alteração de voltagem. Pulsos quadrados (ex: +5V para bit 1, -5V para bit 0).
* **Na Fibra (Luz/Fótons):** O laser liga/desliga bilhões de vezes por segundo. Usa-se o **WDM (Wavelength Division Multiplexing)** para enviar várias "cores" de laser no mesmo fio de vidro, multiplicando a capacidade.
* **No Wireless (QAM - Quadrature Amplitude Modulation):** Altera-se a "altura" (Amplitude) e o "ritmo" (Fase) da onda de rádio simultaneamente. Modulações altas como **256-QAM** conseguem transportar 8 bits em uma única crista de onda, exigindo um ambiente com baixíssimo ruído.

### 3. Meios Guiados (Cabos)
* **Cobre (UTP):** Sujeito à **EMI** (Interferência Eletromagnética). Se passar perto de motores ou cabos de alta tensão, o campo magnético externo deforma os pulsos de dados.
* **Fibra Óptica:** * *Monomodo (SMF):* Núcleo finíssimo (laser), viaja em linha reta. Longas distâncias (Cabos submarinos, Backhaul de operadoras).
    * *Multimodo (MMF):* Núcleo espesso (LED), luz viaja em zig-zag (Reflexão Interna Total). Curtas distâncias (Data Centers, LANs). Imune à EMI.

---

## 🚦 Camada 2: Enlace de Dados (O Código de Trânsito Local)

A Camada de Enlace (L2) pega os bits brutos da Camada 1 e os organiza em "blocos" com significado, chamados **Quadros (Frames)**. Ela só se importa com a comunicação dentro da *mesma rede local (LAN)*.

### 1. Subcamadas do Enlace (LLC e MAC)
No padrão IEEE 802 (Ethernet/Wi-Fi), a L2 é dividida em duas metades:
* **LLC (Logical Link Control - 802.2):** A metade "de cima". Conversa com a Camada 3 (IPv4/IPv6), identificando qual protocolo de rede está sendo transportado no payload.
* **MAC (Media Access Control - 802.3):** A metade "de baixo". Conversa com o hardware. Responsável pelo endereçamento físico e por ditar as regras de quem pode acessar o cabo/ar.

### 2. Endereçamento MAC (Physical Address)
* Endereço fixo de 48 bits, gravado na placa de rede (NIC). Geralmente expresso em formato Hexadecimal (ex: `00:1A:2B:3C:4D:5E`).
* **Estrutura:** * Os primeiros 24 bits são o **OUI** (Organizationally Unique Identifier), que identifica a fabricante da placa.
    * Os últimos 24 bits são o número de série único da placa.
* **Limitação Vitais:** Endereços MAC **nunca** atravessam Roteadores. Eles só sobrevivem dentro da rede local.



### 3. A Anatomia do Quadro Ethernet (Frame)
Quando o IP desce para a L2, ele é envelopado. O Quadro contém:
1.  **Preâmbulo:** Sequência de bits para sincronizar o relógio do emissor e receptor.
2.  **MAC de Destino:** Quem deve receber o quadro na LAN (pode ser Unicast, Multicast ou Broadcast `FF:FF:FF:FF:FF:FF`).
3.  **MAC de Origem:** Quem enviou o quadro.
4.  **EtherType:** Identifica o que tem dentro (Ex: 0x0800 significa que há um IPv4 no payload).
5.  **Payload (Dados):** O pacote IP encapsulado.
6.  **Trailer (FCS - Frame Check Sequence):** Um cálculo matemático (CRC) executado sobre todo o quadro. O receptor refaz o cálculo; se o valor for diferente do FCS, ele sabe que a Camada 1 sofreu interferência e descarta o quadro na hora.

### 4. Controle de Acesso ao Meio (Como evitar colisões)
Dispositivos não podem simplesmente gritar na rede ao mesmo tempo.
* **CSMA/CD (Collision Detection):** Usado em cabos antigos (Half-duplex). O dispositivo transmite e "ouve" o cabo. Se detectar um pico de voltagem (colisão), ele para, envia um sinal de erro, aguarda um tempo aleatório e tenta novamente.
* **CSMA/CA (Collision Avoidance):** Usado no Wi-Fi (802.11). Como a placa de rádio não consegue transmitir e ouvir ao mesmo tempo (Half-duplex rádio), ela envia um pequeno "aviso" prévio reservando o canal por alguns milissegundos para evitar que outros transmitam por cima.

### 5. O Switch (O Guarda de Trânsito da Camada 2)
Diferente dos hubs antigos, o Switch é inteligente, mas sua inteligência se limita à Camada 2.
* **Tabela CAM (MAC Address Table):** O Switch aprende ativamente a topologia da rede. Ele olha para o **MAC de Origem** de todo quadro que entra em uma porta e anota: "A porta 5 tem o MAC X".
* **Forwarding:** Quando um quadro chega destinado ao MAC X, o Switch entrega *apenas* na porta 5 (Unicast), isolando o tráfego e protegendo contra interceptações simples (sniffing de rede não-promíscuo).
* **Flooding:** Se o Switch não sabe onde está o MAC de Destino, ele envia o quadro para *todas* as portas (exceto a que originou o tráfego) na esperança de que o destino responda e ele aprenda a porta.

---

### 🔗 A Ponte para o Módulo 06 (A Camada 3)
A Camada 2 é perfeita, mas tem um problema fatal: **ela não escala**. Se a internet inteira funcionasse apenas com MAC Addresses e Switches fazendo Flooding/Broadcast, a rede colapsaria em 5 minutos devido a uma tempestade de pacotes (Broadcast Storm). 

É por isso que, para sair da sua casa e chegar ao Google, o quadro Ethernet L2 deve ser entregue ao seu **Gateway Padrão (Roteador)**. O Roteador vai destruir o quadro L2, ler o IP L3 e tomar a decisão de encaminhamento global. Esse é o foco exato do Módulo 06.
