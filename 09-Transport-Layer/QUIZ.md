# 🧠 Simulado Definitivo: Module 09 (Transport Layer, TCP/UDP & Nmap)
Este simulado contém 15 questões de nível de certificação, focadas nos objetivos oficiais do exame **Cisco CBROPS 200-201**. Ele testa a sua capacidade de compreender os protocolos da Camada de Transporte (TCP e UDP), o processo de handshake, campos de cabeçalho, controle de fluxo e a aplicação tática utilizando Wireshark e Nmap.

---

### 📦 Domínio 1: Conceitos da Camada de Transporte e Sockets

**1. Qual é a principal função da Camada de Transporte no modelo TCP/IP?**
- [ ] A) Roteamento de pacotes entre redes distintas.
- [ ] B) Converter nomes de domínio em endereços IP.
- [ ] C) Mover dados entre aplicações em dispositivos na rede e realizar multiplexação.
- [ ] D) Controle de acesso ao meio físico (MAC).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A Camada de Transporte é responsável por rastrear conversas individuais, segmentar dados, remontá-los e identificar as aplicações corretas através do uso de portas, permitindo a multiplexação.
</details>
<br>

**2. O que compõe um "Socket" em redes de computadores?**
- [ ] A) Endereço MAC de origem e Endereço MAC de destino.
- [ ] B) Endereço IP e Endereço MAC.
- [ ] C) O tamanho da janela (Window Size) e o número de sequência.
- [ ] D) A combinação de um Endereço IP e um Número de Porta.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> Um socket identifica unicamente uma conexão de ponta a ponta. Ele é formado pela junção do endereço lógico do host (IP) com o identificador da aplicação (Porta).
</details>
<br>

---

### ⚖️ Domínio 2: TCP vs. UDP

**3. Qual das alternativas apresenta características exclusivas do protocolo UDP?**
- [ ] A) Orientado a conexão, entrega garantida e controle de fluxo.
- [ ] B) Stateless, overhead de 8 bytes, entrega de "melhor esforço" (best-effort).
- [ ] C) Utiliza o Three-way Handshake antes de transmitir dados.
- [ ] D) Overhead de 20 bytes e ordenação de pacotes.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O UDP é um protocolo simples, rápido e sem estado (stateless). Ele não garante a entrega nem a ordem, possuindo um cabeçalho enxuto de apenas 8 bytes.
</details>
<br>

**4. Quantos bytes tem o cabeçalho padrão do protocolo TCP e do protocolo UDP, respectivamente?**
- [ ] A) 20 bytes e 8 bytes.
- [ ] B) 32 bytes e 16 bytes.
- [ ] C) 8 bytes e 20 bytes.
- [ ] D) 40 bytes e 20 bytes.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> O TCP adiciona 20 bytes de overhead devido aos seus múltiplos campos de controle (Seq, Ack, Flags, Window), enquanto o UDP adiciona apenas 8 bytes (Portas, Length, Checksum).
</details>
<br>

**5. Uma aplicação de streaming de vídeo ao vivo está sofrendo com pequenos atrasos na rede. Qual protocolo de transporte é o mais adequado para essa aplicação e por quê?**
- [ ] A) TCP, porque garante que todos os quadros de vídeo cheguem em ordem.
- [ ] B) TCP, porque o controle de congestionamento acelera o vídeo.
- [ ] C) UDP, porque aplicações de voz e vídeo ao vivo toleram pequenas perdas de dados e preferem a velocidade em vez de esperar retransmissões.
- [ ] D) ICMP, porque é mais rápido que o TCP e o UDP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O UDP é o padrão para tráfego em tempo real. Uma retransmissão no TCP causaria travamentos (buffering), enquanto o UDP simplesmente continua o fluxo aceitando a perda de alguns frames.
</details>
<br>

---

### 🤝 Domínio 3: Estabelecimento e Encerramento de Sessões (TCP)

**6. Qual é a sequência correta de Flags enviadas durante o estabelecimento de uma conexão TCP (Three-way Handshake)?**
- [ ] A) SYN, ACK, FIN.
- [ ] B) SYN, SYN-ACK, ACK.
- [ ] C) ACK, SYN, SYN-ACK.
- [ ] D) PSH, SYN, ACK.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O cliente inicia com SYN. O servidor responde com SYN e ACK simultaneamente. O cliente finaliza confirmando a conexão com um ACK.
</details>
<br>

**7. Quantas trocas de mensagens ocorrem para que uma sessão TCP seja completamente encerrada por ambas as partes de forma limpa?**
- [ ] A) Duas (FIN e ACK).
- [ ] B) Três (FIN, FIN-ACK, ACK).
- [ ] C) Quatro (FIN, ACK, FIN, ACK).
- [ ] D) Apenas uma (RST).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O encerramento do TCP é independente para cada lado (full-duplex). Um lado manda FIN e recebe ACK, depois o outro lado manda seu FIN e recebe o ACK final (4 passos no total).
</details>
<br>

---

### 📏 Domínio 4: Confiabilidade, Controle de Fluxo e Campos TCP

**8. Qual campo do cabeçalho TCP é utilizado para gerenciar o Controle de Fluxo (Flow Control), indicando a quantidade de dados que o destino pode receber?**
- [ ] A) Sequence Number.
- [ ] B) Checksum.
- [ ] C) Window Size.
- [ ] D) Urgent Pointer.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O campo "Window Size" (Tamanho da Janela) informa ao remetente quantos bytes o receptor pode armazenar no seu buffer no momento, controlando a taxa de envio.
</details>
<br>

**9. Em uma interface Ethernet com MTU padrão de 1500 bytes, qual será o tamanho típico do MSS (Maximum Segment Size) para uma conexão TCP sobre IPv4?**
- [ ] A) 1500 bytes.
- [ ] B) 1460 bytes.
- [ ] C) 1480 bytes.
- [ ] D) 64 bytes.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O MSS calcula apenas os dados da aplicação. Subtrai-se do MTU (1500) o cabeçalho IPv4 (20 bytes) e o cabeçalho TCP (20 bytes), resultando em 1460 bytes úteis.
</details>
<br>

**10. Se um pacote com múltiplos segmentos TCP sofrer roteamento assimétrico e os segmentos chegarem fora de ordem ao destino, como o host receptor reconstrói os dados originais?**
- [ ] A) Solicitando retransmissão imediata através da flag RST.
- [ ] B) Usando os números de porta de origem.
- [ ] C) Reordenando os segmentos com base no campo "Sequence Number".
- [ ] D) O TCP não lida com reordenação, repassando o erro para a aplicação.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O "Sequence Number" identifica o primeiro byte de dados do segmento, permitindo que o receptor remonte a sequência exata mesmo que os pacotes cheguem fora de ordem.
</details>
<br>

---

### 🚩 Domínio 5: Flags (Control Bits) do TCP

**11. Qual das flags a seguir, presente no campo "Control Bits" do cabeçalho TCP, é usada para redefinir imediatamente a conexão caso ocorra um erro grave ou timeout?**
- [ ] A) URG
- [ ] B) PSH
- [ ] C) RST
- [ ] D) FIN

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A flag RST (Reset) é utilizada para abortar uma conexão imediatamente de forma anormal ou rejeitar um pacote direcionado a uma porta fechada.
</details>
<br>

**12. Ao analisar uma captura de tráfego de um ataque de DoS (Denial of Service), o analista de segurança nota milhares de pacotes com o valor hexadecimal "0x002" no campo de flags. Qual tipo de ataque é esse?**
- [ ] A) ACK Flood
- [ ] B) SYN Flood
- [ ] C) UDP Flood
- [ ] D) ARP Spoofing

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A flag com valor 0x02 corresponde ao bit SYN ligado. Um grande volume de pacotes SYN sem o respectivo encerramento do handshake caracteriza um ataque de SYN Flood.
</details>
<br>

---

### 🦈 Domínio 6: Análise de Rede com Wireshark e Nmap

**13. Ao realizar uma captura de pacotes no Wireshark para isolar APENAS o tráfego da camada de transporte orientado a conexão, qual filtro de exibição (Display Filter) deve ser utilizado?**
- [ ] A) http
- [ ] B) tcp
- [ ] C) arp
- [ ] D) udp

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O filtro `tcp` exibirá apenas os segmentos Transmission Control Protocol, ocultando protocolos sem conexão como UDP, ICMP e ARP.
</details>
<br>

**14. Um analista do SOC executou o comando `nmap -A -T4 scanme.nmap.org`. Qual das alternativas abaixo NÃO é uma ação realizada por esse comando devido à flag `-A`?**
- [ ] A) Detecção do Sistema Operacional (OS detection).
- [ ] B) Escaneamento de portas UDP de 1 a 65535.
- [ ] C) Detecção de versão dos serviços.
- [ ] D) Rastreamento de rota (Traceroute).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A flag `-A` (Agressive) habilita detecção de SO, detecção de versão, script scanning e traceroute. Ela NÃO muda o scan padrão do Nmap de TCP para UDP de todas as portas (o que exigiria `-sU -p-`).
</details>
<br>

**15. Ao verificar os resultados de um scan do Nmap, um host apresentou a porta 135/tcp com o estado "filtered". O que esse estado geralmente indica na análise de CyberOps?**
- [ ] A) A porta está ativamente aceitando conexões (Open).
- [ ] B) A porta não tem nenhum serviço rodando (Closed).
- [ ] C) As sondagens do Nmap estão sendo bloqueadas por um Firewall ou filtro de pacotes.
- [ ] D) O tráfego foi redirecionado para um honeypot.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O estado "filtered" no Nmap significa que a ferramenta não consegue determinar se a porta está aberta ou fechada porque as requisições (probes) estão sendo dropadas por um dispositivo de filtragem de rede, como um firewall.
</details>
