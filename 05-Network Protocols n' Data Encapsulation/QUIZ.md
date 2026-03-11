# 🧠 Simulado Definitivo: Module 05 (Protocols & Encapsulation) - Edição CyberOps

Este simulado contém 15 questões de nível de certificação, focadas nos objetivos oficiais do exame **Cisco CBROPS 200-201**. Ele testa a sua capacidade de compreender o fluxo de dados, dissecar pacotes e entender o comportamento de protocolos em cenários reais de defesa.

---

**1. Durante o processo de encapsulamento em um host de origem, os dados descem pela pilha de protocolos. Qual é o nome correto da Protocol Data Unit (PDU) criada na Camada de Rede (L3) e qual o principal identificador que ela adiciona?**
- [ ] A) Segmento; adiciona as Portas Lógicas.
- [ ] B) Quadro; adiciona o Endereço MAC.
- [ ] C) Pacote; adiciona o Endereço IP.
- [ ] D) Datagrama; adiciona o cabeçalho Ethernet.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Na Camada de Rede (L3), os dados recebidos da Camada de Transporte são encapsulados em um <b>Pacote</b> (Packet), que inclui o cabeçalho IP contendo os endereços lógicos (IP) de origem e destino.
</details>
<br>

**2. Um analista de SOC (Tier 1) está analisando um PCAP no Wireshark. O tráfego flui do Host A (192.168.1.10) para o Servidor B (10.0.0.50), passando pelo Roteador R1. Ao inspecionar o Quadro Ethernet capturado no segmento de rede do Servidor B, quais endereços serão encontrados?**
- [ ] A) MAC de Origem: Host A | IP de Origem: Host A
- [ ] B) MAC de Origem: Roteador R1 | IP de Origem: Roteador R1
- [ ] C) MAC de Origem: Roteador R1 | IP de Origem: Host A
- [ ] D) MAC de Origem: Host A | IP de Origem: Roteador R1

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O Endereço IP (L3) mantém-se o mesmo de ponta a ponta (Origem: Host A). No entanto, o Endereço MAC (L2) muda a cada salto (hop). No segmento final, o MAC de origem será o da interface de saída do Roteador R1, e não o do Host A.
</details>
<br>

**3. Qual campo específico no cabeçalho de um pacote IPv4 é manipulado por utilitários de diagnóstico como o `traceroute` para descobrir o caminho de roteamento até o destino?**
- [ ] A) Checksum
- [ ] B) Time to Live (TTL)
- [ ] C) Differentiated Services (DiffServ)
- [ ] D) Protocol

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O traceroute envia pacotes incrementando artificialmente o valor do TTL (1, depois 2, depois 3...). Quando um roteador recebe um pacote e o TTL chega a 0, ele descarta o pacote e retorna uma mensagem ICMP "Time Exceeded" à origem, revelando sua identidade.
</details>
<br>

**4. Na arquitetura TCP/IP, qual camada é diretamente responsável por fornecer o que no Modelo OSI é dividido entre as camadas de Sessão, Apresentação e Aplicação?**
- [ ] A) Camada de Transporte
- [ ] B) Camada de Aplicação
- [ ] C) Camada de Acesso à Rede
- [ ] D) Camada de Internet

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O modelo TCP/IP consolidou as camadas 5 (Sessão), 6 (Apresentação) e 7 (Aplicação) do modelo OSI em uma única camada chamada <b>Camada de Aplicação</b>.
</details>
<br>

**5. Um atacante está realizando um ataque de "UDP Flood" contra um servidor DNS. Como analista CyberOps, por que você sabe que esse ataque é mais fácil de mascarar (fazer IP Spoofing) do que um ataque baseado em TCP?**
- [ ] A) Porque o UDP criptografa o endereço de origem por padrão.
- [ ] B) Porque o UDP é um protocolo "Connectionless" e não exige o 3-Way Handshake para validar a origem antes de enviar os dados.
- [ ] C) Porque firewalls não conseguem inspecionar portas UDP.
- [ ] D) Porque o UDP opera na Camada 2, ignorando o roteamento IP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O TCP exige o estabelecimento de uma sessão (SYN, SYN-ACK, ACK) antes de enviar dados, dificultando a falsificação da origem. O UDP apenas "joga" os dados na rede sem verificação prévia, tornando o IP Spoofing trivial.
</details>
<br>

**6. Ao examinar um Quadro Ethernet capturado, você percebe um campo no final do quadro chamado FCS (Frame Check Sequence). Qual é o propósito vital deste campo no encapsulamento da Camada 2?**
- [ ] A) Definir a prioridade de tráfego na rede (QoS).
- [ ] B) Permitir que o receptor detecte se os bits do quadro foram corrompidos ou alterados durante a transmissão física.
- [ ] C) Criptografar o payload de dados usando um hash MD5.
- [ ] D) Identificar o tipo de protocolo contido no pacote (ex: IPv4 ou IPv6).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O FCS (Frame Check Sequence) usa um cálculo de redundância cíclica (CRC) sobre todo o quadro. O receptor refaz o cálculo; se o valor não bater com o FCS, ele sabe que houve interferência/corrupção e descarta o quadro.
</details>
<br>

**7. O que caracteriza o processo de Multiplexação realizado pela Camada de Transporte (Camada 4)?**
- [ ] A) A capacidade de enviar o mesmo pacote para múltiplos roteadores simultaneamente.
- [ ] B) A divisão de um endereço IP público em vários endereços privados usando NAT.
- [ ] C) A utilização de números de Porta Lógica para permitir que múltiplos aplicativos no mesmo host enviem e recebam dados na rede simultaneamente sem que as informações se misturem.
- [ ] D) A combinação de múltiplos cabos físicos em um único link lógico (EtherChannel).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A multiplexação na camada de transporte usa Portas (ex: porta 80 para navegação, 443 para HTTPS, 53 para DNS). Isso permite que o sistema operacional direcione o fluxo de dados correto para o aplicativo correto dentro do mesmo computador.
</details>
<br>

**8. Um analista precisa filtrar o tráfego no Wireshark para exibir APENAS pacotes HTTP destinados ou originados de um servidor web seguro. Qual filtro de exibição está correto para esta tarefa?**
- [ ] A) `ip.addr == 80`
- [ ] B) `tcp.port == 443`
- [ ] C) `http.secure`
- [ ] D) `udp.port == 443`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O tráfego web seguro (HTTPS) utiliza o protocolo TCP na porta 443. O filtro correto no Wireshark para capturar tanto o tráfego de ida quanto o de volta nessa porta é `tcp.port == 443`.
</details>
<br>

**9. Para que dois hosts na mesma sub-rede (LAN) se comuniquem diretamente, o Host A precisa conhecer o endereço MAC do Host B. Qual protocolo é usado na rede IPv4 para descobrir dinamicamente o MAC associado a um IP conhecido?**
- [ ] A) DNS
- [ ] B) DHCP
- [ ] C) ARP (Address Resolution Protocol)
- [ ] D) ICMP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O ARP é usado para mapear um endereço IPv4 conhecido para um endereço físico MAC desconhecido na mesma rede local. Ele envia um Broadcast perguntando "Quem tem o IP X? Diga-me o seu MAC".
</details>
<br>

**10. Qual termo descreve corretamente a combinação de um Endereço IP associado a um número de Porta (ex: 192.168.1.100:443), criando um canal de comunicação de ponta a ponta único?**
- [ ] A) MAC Address
- [ ] B) Socket
- [ ] C) PDU
- [ ] D) Datagrama

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Um Socket é a combinação lógica de um endereço IP (que identifica a máquina na rede) e um número de porta (que identifica o serviço/processo específico na máquina).
</details>
<br>

**11. Como o Modelo de Referência OSI classifica o processo de formatação dos dados, compressão e criptografia nativa (ex: converter dados em JPEG, ASCII, ou encriptação a nível de SO) antes de enviá-los para a rede?**
- [ ] A) Camada de Sessão (Camada 5)
- [ ] B) Camada de Apresentação (Camada 6)
- [ ] C) Camada de Aplicação (Camada 7)
- [ ] D) Camada de Transporte (Camada 4)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A Camada de Apresentação (Camada 6 do OSI) é o "tradutor" da rede. Ela lida com a formatação de dados, sintaxe, compressão e encriptação antes de passar os dados para a Camada de Aplicação ou de Sessão.
</details>
<br>

**12. Em relação ao Desencapsulamento (De-encapsulation) em um roteador intermediário no caminho da rede, até qual camada o roteador normalmente precisa abrir a PDU para tomar sua decisão de repasse (forwarding)?**
- [ ] A) Abre até a Camada de Enlace (L2) para ler o MAC.
- [ ] B) Abre até a Camada de Transporte (L4) para ler a porta.
- [ ] C) Abre até a Camada de Rede (L3) para ler o IP de destino.
- [ ] D) Não desencapsula o pacote; ele atua apenas fisicamente (L1).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Roteadores são dispositivos de Camada 3. Eles retiram o cabeçalho Ethernet (L2) para inspecionar o pacote IP (L3) e consultar sua tabela de roteamento com base no IP de Destino. Depois, reencapsulam o IP em um novo quadro Ethernet.
</details>
<br>

**13. Você captura um pacote onde o endereço MAC de destino é `FF:FF:FF:FF:FF:FF`. O que este endereço indica?**
- [ ] A) É um endereço de loopback para testar a placa de rede interna.
- [ ] B) É um Broadcast da Camada 2, indicando que todos os dispositivos no segmento de rede local (LAN) devem processar o quadro.
- [ ] C) É o endereço MAC fixo do Roteador Padrão (Default Gateway).
- [ ] D) É um endereço Multicast reservado para protocolos de roteamento.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O MAC composto apenas por Fs (tudo 1s em binário) é o endereço de Broadcast Ethernet. O Switch repassa esse quadro para todas as portas, e todas as placas de rede ativas na LAN o recebem e processam.
</details>
<br>

**14. Por que um Sniffer de rede (como o Wireshark) requer que a placa de rede (NIC) seja colocada no modo "Promíscuo" (Promiscuous Mode) para funcionar de forma eficaz em análises de segurança?**
- [ ] A) Para permitir que a placa de rede descriptografe pacotes SSL/TLS automaticamente.
- [ ] B) Porque o modo promíscuo eleva os privilégios do usuário para Root no sistema operacional.
- [ ] C) Para forçar a NIC a aceitar e processar todos os quadros que chegam a ela, mesmo aqueles em que o endereço MAC de destino não pertença à própria máquina.
- [ ] D) Para aumentar a velocidade de clock da NIC e capturar gigabits por segundo sem perder pacotes.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Por padrão, uma placa de rede descarta qualquer quadro que não seja endereçado ao seu próprio MAC ou ao MAC de Broadcast. O modo promíscuo desativa esse filtro, forçando a placa a capturar absolutamente todo o tráfego que passa pelo cabo/ar.
</details>
<br>

**15. No protocolo TCP, o que ocorre caso um "Segmento" de dados não receba um Acknowledgment (ACK) do dispositivo de destino dentro de um tempo predeterminado (Timeout)?**
- [ ] A) O sistema de origem assume que a rede está congestionada e encerra a conexão.
- [ ] B) O protocolo TCP é "Best-Effort", portanto o segmento é ignorado e o próximo é enviado.
- [ ] C) O transmissor irá retransmitir automaticamente o segmento não confirmado, garantindo a entrega confiável.
- [ ] D) O roteador intermediário envia um pacote ICMP Echo Reply falso para manter a sessão ativa.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Esta é a base da confiabilidade do TCP. Ele exige um ACK (reconhecimento) para cada dado enviado. Se o tempo limite expirar sem um ACK, o transmissor retransmite o segmento perdido.
</details>
