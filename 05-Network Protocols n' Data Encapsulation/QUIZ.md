# 🧠 Simulado Definitivo: Module 05 (Protocols & Encapsulation)

Estas questões foram elaboradas baseando-se estritamente na dissecação de pacotes e modelos de referência cobrados no módulo, fundamentais para a certificação **Cisco CBROPS 200-201**.

---

**1. Durante uma análise de tráfego, você captura a PDU da Camada 4 do modelo OSI. Qual é o nome correto desta unidade e qual tipo de endereçamento vital ela adiciona ao processo de encapsulamento?**
- [ ] A) Pacote (Packet); adiciona o Endereço IP.
- [ ] B) Quadro (Frame); adiciona o Endereço MAC.
- [ ] C) Segmento (Segment); adiciona os Números de Porta.
- [ ] D) Dados (Data); adiciona o cabeçalho HTTP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Na Camada de Transporte (L4), a PDU é chamada de Segmento (ou Datagrama para UDP). O cabeçalho de transporte, seja TCP ou UDP, insere o endereçamento de protocolo através dos números de Porta.
</details>
<br>

**2. O utilitário `traceroute` é crucial para identificar a cadeia de custódia do tráfego através de redes externas. Como ele determina o caminho tomado pelo pacote do início ao fim?**
- [ ] A) Listando todos os switches Ethernet encontrados na rede local do usuário usando protocolos ARP.
- [ ] B) Enviando e medindo pacotes ICMP, onde cada "hop" (salto) listado na tela representa um Roteador diferente pelo qual o pacote foi encaminhado.
- [ ] C) Utilizando o DNS para mapear o FQDN e retornar a topologia física completa do servidor de destino.
- [ ] D) Forçando os firewalls no caminho a enviarem relatórios SNMP de volta para a origem.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O traceroute mapeia cada dispositivo de roteamento ("hop") pelo qual o pacote passa do host de origem até o destino, permitindo identificar provedores (ISPs) e atrasos (em milissegundos) em cada segmento.
</details>
<br>

**3. Uma comunicação via TCP/IP exige o uso de "Três Endereços" distintos. Se um cliente na rede A precisa se comunicar com um servidor na rede B, qual afirmação descreve corretamente o comportamento da Camada de Enlace de Dados?**
- [ ] A) O cabeçalho de Enlace de Dados manterá o endereço físico (MAC) do servidor da rede B como destino em toda a viagem do pacote.
- [ ] B) O cabeçalho de Enlace de Dados especificará o endereço de hardware do dispositivo na rede local (LAN) que deve manipular o Frame, neste caso, o Gateway/Roteador padrão.
- [ ] C) A Camada de Enlace não usa endereçamento; ela apenas traduz bits em pulsos elétricos.
- [ ] D) A Camada de Enlace usa números de porta para identificar a aplicação no servidor da rede B.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O endereço físico (MAC) é usado exclusivamente para comunicação na rede local (LAN). Ao enviar dados para uma rede remota, o MAC de destino será o do roteador local. O endereço IP (L3) é o que permanece como o destino final.
</details>
<br>

**4. Na suíte TCP/IP, protocolos de Transporte como o TCP são considerados "Orientados a Conexão" (Connection-Oriented), enquanto o UDP é "Sem Conexão" (Connectionless). Quais são protocolos da Camada de Internet/Rede que ficam imediatamente abaixo desta camada, fornecendo o endereçamento lógico e o repasse de mensagens?**
- [ ] A) HTTP, HTTPS e DNS.
- [ ] B) Ethernet, WLAN e ARP.
- [ ] C) IPv4, IPv6 e ICMP.
- [ ] D) FTP, TFTP e SMTP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A Camada de Internet (Internet Layer) do modelo TCP/IP engloba o Internet Protocol (IPv4/IPv6) para endereçamento lógico, ICMP para mensagens/erros, e protocolos de roteamento como OSPF e BGP.
</details>
<br>

**5. Você iniciou o script Mininet (`cyberops_topo.py`) no CyberOps VM para estudar pacotes no Wireshark. Após capturar tráfego, você analisa o Frame Ethernet e vê que o cabeçalho adicionou informações ao redor do pacote IP e do segmento TCP. Quando a mensagem for recebida pelo cliente Web, como esse encapsulamento é tratado?**
- [ ] A) O cliente mantém o cabeçalho Ethernet intacto e o salva no disco rígido junto com os dados HTTP.
- [ ] B) O processo reverso ocorre (Desencapsulamento). O destino processa os cabeçalhos de baixo para cima, removendo-os a cada camada até que os dados cheguem puros à aplicação cliente.
- [ ] C) O roteador decodifica a camada de aplicação e reenvia apenas o texto puro para o cliente.
- [ ] D) O cliente Web converte todo o Frame em um Broadcast para checar erros com outros hosts.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Quando os dados são recebidos, ocorre o desencapsulamento. A PDU é processada e as informações dos cabeçalhos são lidas e removidas de baixo para cima na pilha de protocolos, de modo que os dados puros possam ser utilizados pelo aplicativo do cliente.
</details>
