# 📁 Module 05: Network Protocols & Data Encapsulation

> [!NOTE]
> **Resumo Executivo:** Este módulo é o coração da comunicação de redes no currículo CyberOps. Descodifica como os dispositivos conversam através de regras padronizadas (Protocolos) e como os dados são preparados, divididos e endereçados para viajar pelo mundo físico. Dominar os modelos OSI e TCP/IP, em conjunto com o processo de Encapsulamento, é o que permite a um analista utilizar ferramentas como o Wireshark para caçar ameaças nos pacotes.

---

## 🏛️ Modelos de Referência: A Arquitetura da Comunicação

Para organizar a complexidade das redes, utilizamos modelos em camadas. Estes evitam que mudanças numa camada afetem as outras e padronizam o desenvolvimento.



### 1. Modelo OSI (7 Camadas) vs. Modelo TCP/IP (4 Camadas)
Enquanto o modelo OSI é teórico e detalhado, o TCP/IP é o padrão prático da internet.
* **Aplicação (OSI L7, L6, L5 = TCP/IP L4):** Representa os dados para o utilizador e gere diálogos. Protocolos: HTTP, DNS, DHCP, FTP, SMTP.
* **Transporte (OSI L4 = TCP/IP L3):** Segmenta os dados e suporta a comunicação entre dispositivos distintos. 
    * *TCP:* Orientado à ligação (Connection-Oriented).
    * *UDP:* Sem ligação (Connectionless).
* **Internet/Rede (OSI L3 = TCP/IP L2):** Determina o melhor caminho através da rede. Protocolos: IPv4, IPv6, ICMP, OSPF, BGP.
* **Acesso à Rede / Enlace e Física (OSI L2, L1 = TCP/IP L1):** Controla os dispositivos de hardware e o meio físico. Protocolos: ARP, Ethernet, WLAN.

---

## 📦 O Processo de Encapsulamento (A Jornada do Bit)

Mensagens grandes não podem ser enviadas de uma só vez, pois monopolizariam a rede. São divididas em partes menores (Segmentação), o que permite que várias conversas ocorram ao mesmo tempo na mesma rede (Multiplexagem).



### A Evolução das PDUs (Protocol Data Units)
À medida que os dados descem na pilha de protocolos para serem enviados, informações vitais são adicionadas. No exame, é crucial saber os nomes exatos:
1.  **Data (Dados):** A PDU geral da Camada de Aplicação.
2.  **Segment (Segmento):** A PDU da Camada de Transporte (adiciona o cabeçalho TCP/UDP com as **Portas**).
3.  **Packet (Pacote):** A PDU da Camada de Rede (adiciona o cabeçalho IP com os **Endereços IP** de origem/destino).
4.  **Frame (Quadro/Trama):** A PDU da Camada de Enlace (adiciona o cabeçalho Ethernet com os **Endereços MAC** e o Trailer para verificação de erros).
5.  **Bits:** A PDU da Camada Física (os dados convertidos para o meio físico).

> **O Conceito dos "Três Endereços" (Three Addresses):**
> A comunicação Cliente-Servidor exige 3 níveis de endereçamento:
> * **Physical address (L2):** Endereço MAC para comunicação na rede local (LAN).
> * **Network host address (L3):** Endereço IP para identificar redes e hosts de ponta a ponta.
> * **Protocol address (L4):** Números de Porta para identificar qual aplicação deve lidar com os dados.

---

## 📑 Tactical Field Report: Lab Executions

Vamos mergulhar no passo a passo prático de como estas ferramentas são utilizadas num cenário de resposta a incidentes ou troubleshooting, utilizando a *CyberOps Workstation VM*.

### 🔬 Lab 5.1.5: Tracing a Route (Reconhecimento de Percurso)
**Objetivo:** Mapear os "saltos" (routers) que um pacote faz até um servidor remoto para identificar ISPs e possíveis estrangulamentos ou interceções de tráfego.

**Execução em Campo:**
1.  **Teste de Vida (Ping):** Primeiro, enviamos 4 pacotes ICMP para garantir conectividade básica.
    `[analyst@secOps ~]$ ping -c 4 www.cisco.com`
    *Resultado:* Recebemos respostas do IP `184.24.123.103` (resolvido por DNS para servidores da Akamai). Sem perda de pacotes (0% packet loss).
2.  **Mapeamento da Rota (Traceroute):** Para ver o que acontece *entre* o nosso host e o servidor, utilizamos o `traceroute`, que explora o campo TTL (Time to Live) dos pacotes.
    `[analyst@secOps ~]$ traceroute www.cisco.com > cisco-traceroute.txt`
    *Resultado:* Salvamos a saída diretamente num ficheiro utilizando o redirecionamento (`>`). O traceroute listou cada router percorrido.
    * **Salto 1:** `192.168.1.1` (O nosso gateway local).
    * **Salto 2 a 5:** Redes internas do fornecedor de serviços.
    * **Salto 6:** O destino final `184.24.123.103`.

### 🦈 Lab 5.3.7: Introduction to Wireshark (Captura e Análise Profunda)
**Objetivo:** Simular uma infraestrutura de rede complexa utilizando o *Mininet* e usar o Wireshark para dissecar o encapsulamento de PDUs em tempo real.

**Execução em Campo:**
1.  **Construção da Infraestrutura Virtual:** Lançamos um script Python poderoso que cria, dentro do próprio Linux, Routers (R1), Switches (S1) e múltiplos Hosts (H1 a H4).
    `[analyst@secOps ~]$ sudo ~/lab.support.files/scripts/cyberops_topo.py`
2.  **Recolha de Inteligência Local:** Abrimos terminais nos hosts (`xterm H1`, `xterm H2`) e utilizamos `ip address` para anotar os IPs e Endereços MAC de cada interface virtual.
3.  **A Captura (Sniffing):** No host H1, lançamos o Wireshark em background (`wireshark &`), selecionamos a interface `H1-eth0` e disparamos um tráfego de controlo contra o H2:
    `[root@secOps analyst]# ping -c 5 10.0.0.12`
4.  **A Análise da Camada 2 (LAN):** Paramos o Wireshark e aplicamos o filtro `icmp`. Ao clicar no pacote de "Echo (ping) request", exploramos o painel intermediário.
    * *Descoberta Analítica:* O "Ethernet II header" mostrou que o Endereço MAC de Origem era perfeitamente igual ao do H1, e o Destino era o MAC do H2. A comunicação ocorreu diretamente na camada 2, pois estão na mesma rede (`10.0.0.0/24`).
5.  **O Comportamento de Roteamento (Remote LAN):** Fizemos um ping do H1 para o H4 (`172.16.0.40`), que está do outro lado do router R1.
    * *Descoberta Analítica Vital (CyberOps):* Ao analisar esta captura, o IP de Destino continuava a ser o do H4 (`172.16.0.40`). Porém, o **Endereço MAC de Destino não era o do H4**, mas sim o endereço MAC da interface `R1-eth1` do Router. Isto prova na prática a regra de ouro: *MACs operam apenas localmente; pacotes externos são enviados para o endereço físico do gateway padrão.*
