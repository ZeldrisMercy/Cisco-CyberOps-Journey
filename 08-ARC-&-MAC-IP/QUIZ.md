# 🧠 Simulado Interativo: Módulo 08 - ARP & Relação MAC/IP

Este simulado foca-se na compreensão do **protocolo ARP**, funcionamento da **comunicação em redes locais**, estrutura de **quadros Ethernet**, e relação entre **endereços MAC e IP**, conforme os objetivos do exame **Cisco CBROPS 200-201**.

---

## 📚 Conteúdos Abordados

- Funcionamento do protocolo ARP  
- Descoberta de MAC a partir de IP  
- Comunicação dentro e fora da sub-rede  
- Estrutura de quadros Ethernet  
- Broadcast e Unicast na rede  
- Cache ARP e seu funcionamento  
- Ataques ARP Spoofing  
- Campos do quadro Ethernet  
- Análise de pacotes com Wireshark  

---

# 🌐 Domínio 1: Comunicação em Redes Locais (ARP)

**1. Quando um dispositivo precisa enviar dados para um destino que está na mesma sub-rede IPv4, como ele descobre o endereço MAC de destino?**

a) Consulta o servidor DNS  
b) Envia o pacote ao gateway  
c) Verifica a tabela de roteamento  
d) Consulta o cache ARP ou envia um ARP Request  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) Consulta o cache ARP ou envia um ARP Request

**Explicação:**  
Para comunicação dentro da mesma rede local, o dispositivo precisa descobrir qual **MAC corresponde ao IP de destino**.

Ele faz isso através do **ARP (Address Resolution Protocol)**:

1. Primeiro verifica se o IP já está no **cache ARP**.  
2. Caso não esteja, envia um **ARP Request em broadcast** para descobrir o MAC correspondente.

</details>

<br>

---

**2. Qual é o endereço MAC de destino utilizado em um ARP Request?**

a) MAC do servidor DHCP  
b) FF:FF:FF:FF:FF:FF  
c) 00:00:00:00:00:00  
d) MAC do gateway  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) FF:FF:FF:FF:FF:FF

**Explicação:**  
O ARP Request precisa alcançar **todos os dispositivos da rede local**.

Por isso ele utiliza um endereço **broadcast Ethernet**, representado por:

FF:FF:FF:FF:FF:FF

Todos os hosts recebem a mensagem, mas apenas o que possui o IP solicitado responde.

</details>

<br>

---

**3. Qual protocolo está identificado pelo valor hexadecimal 0x0806 no campo Type do quadro Ethernet?**

a) IPv4  
b) ARP  
c) IPv6  
d) ICMP  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) ARP

**Explicação:**  
O campo **EtherType** no quadro Ethernet identifica qual protocolo está encapsulado.

Alguns valores comuns:

- **0x0800 → IPv4**  
- **0x0806 → ARP**  
- **0x86DD → IPv6**

</details>

<br>

---

**4. Um host precisa enviar dados para o endereço IP 8.8.8.8. Qual será o MAC destino no quadro Ethernet inicial?**

a) MAC do servidor Google  
b) Broadcast  
c) MAC do Default Gateway  
d) MAC do ISP  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) MAC do Default Gateway

**Explicação:**  
Quando o destino está **fora da rede local**, o host não envia diretamente ao destino final.

Em vez disso:

1. O host envia o quadro ao **roteador (gateway)**.
2. O roteador encaminha o pacote para a rede externa.

</details>

<br>

---

# 🧩 Domínio 2: Segurança e Ataques Relacionados ao ARP

**5. Um atacante envia respostas ARP falsas afirmando que o gateway pertence ao seu MAC. Qual ataque é esse?**

a) MAC Flooding  
b) ARP Spoofing  
c) DHCP Starvation  
d) DNS Poisoning  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) ARP Spoofing

**Explicação:**  
No **ARP Spoofing**, o atacante envia **respostas ARP falsas** para manipular a tabela ARP das vítimas.

Isso permite:

- interceptar tráfego (Man-in-the-Middle)  
- modificar pacotes  
- capturar credenciais  

</details>

<br>

---

# 🔍 Domínio 3: Tabelas ARP e Ferramentas

**6. Qual comando mostra a tabela ARP de um sistema?**

a) ipconfig  
b) netstat  
c) arp -a  
d) nslookup  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) arp -a

**Explicação:**  
O comando:

arp -a

mostra o **cache ARP**, que contém associações entre:

IP → MAC

Isso ajuda a diagnosticar problemas de rede.

</details>

<br>

---

**7. Qual parte do endereço MAC identifica o fabricante da placa de rede?**

a) Últimos 24 bits  
b) Campo Type  
c) Primeiros 24 bits (OUI)  
d) Preâmbulo  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Primeiros 24 bits (OUI)

**Explicação:**  
O endereço MAC possui 48 bits.

Estrutura:

- **Primeiros 24 bits → OUI (fabricante)**  
- **Últimos 24 bits → Identificador único do dispositivo**

</details>

<br>

---

**8. Por que entradas ARP possuem tempo de expiração?**

a) Porque IP muda a cada ping  
b) Para renovar DHCP  
c) Porque tabelas ocupam muito espaço  
d) Para manter informações atualizadas  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) Para manter informações atualizadas

**Explicação:**  
Entradas ARP expiram para evitar inconsistências.

Isso é importante quando:

- dispositivos mudam de IP  
- interfaces são reiniciadas  
- MAC address muda

</details>

<br>

---

# 🧱 Domínio 4: Estrutura do Quadro Ethernet

**9. O que acontece se o FCS de um quadro Ethernet estiver incorreto?**

a) O switch corrige  
b) A NIC descarta o quadro  
c) O roteador corrige  
d) O ARP retransmite  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) A NIC descarta o quadro

**Explicação:**  
O **FCS (Frame Check Sequence)** detecta erros de transmissão.

Se houver inconsistência, a **placa de rede descarta o quadro automaticamente**.

</details>

<br>

---

**10. Qual campo do quadro Ethernet não aparece normalmente no Wireshark?**

a) Source MAC  
b) Type  
c) Preamble  
d) FCS  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Preamble

**Explicação:**  
O **preâmbulo** é tratado diretamente pelo hardware da placa de rede.

Por isso ele geralmente **não aparece em capturas de pacotes**.

</details>

<br>

---

# 🌍 Domínio 5: Protocolos Relacionados

**11. Qual diferença entre ARP e ICMP?**

a) ARP usa UDP  
b) ICMP é roteável entre redes  
c) ARP criptografa dados  
d) São protocolos equivalentes  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) ICMP é roteável entre redes

**Explicação:**  

ARP:
- Funciona apenas dentro da **rede local (LAN)**

ICMP:
- Pode atravessar **roteadores e redes diferentes**

</details>

<br>

---

**12. Qual comando limpa o cache ARP no Windows?**

a) Reiniciar firewall  
b) arp -d *  
c) ping -t  
d) alterar DNS  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) arp -d *

**Explicação:**  
Esse comando remove **todas as entradas do cache ARP**.

Isso força o sistema a reconstruir a tabela ARP.

</details>

<br>

---

# 📡 Domínio 6: Tipos de Comunicação

**13. Qual tipo de comunicação representa um ARP Reply?**

a) Broadcast  
b) Multicast  
c) Unicast  
d) Anycast  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Unicast

**Explicação:**  
Enquanto o **ARP Request é broadcast**, o **ARP Reply é unicast**.

Ou seja, a resposta é enviada **diretamente ao host solicitante**.

</details>

<br>

---

**14. Qual protocolo pode gerar flooding natural em redes grandes?**

a) HTTP  
b) ARP  
c) OSPF  
d) SMTP  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) ARP

**Explicação:**  
ARP usa **broadcast na rede local**.

Em redes grandes isso pode gerar **muito tráfego de broadcast**, causando flooding.

</details>

<br>

---

# 🔬 Domínio 7: Análise de Pacotes

**15. O filtro "arp or icmp" no Wireshark mostra o que?**

a) Erros L2 e L3  
b) Tráfego de roteamento  
c) Pacotes ARP e ICMP  
d) Todo tráfego TCP/IP  

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Pacotes ARP e ICMP

**Explicação:**  
O filtro mostra apenas dois tipos de pacotes:

- mensagens **ARP (resolução de endereço)**  
- mensagens **ICMP (como ping)**

Isso facilita analisar **descoberta de rede e conectividade**.

</details>

---

