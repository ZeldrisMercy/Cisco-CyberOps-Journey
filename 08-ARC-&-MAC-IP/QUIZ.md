# 🧠 Simulado Definitivo: Module 08 (ARP & MAC/IP)

Este simulado contém **15 questões de nível de certificação**, focadas nos objetivos do exame **Cisco CBROPS 200-201**.



**1. Quando um dispositivo precisa enviar dados para um destino que está na mesma sub-rede IPv4, como ele descobre o endereço MAC de destino?**

- [ ] A) Consulta o servidor DNS
- [ ] B) Envia o pacote ao gateway
- [ ] C) Verifica a tabela de roteamento
- [ ] D) Consulta o cache ARP ou envia um ARP Request

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: D**

Explicação:  
Para comunicação local o dispositivo utiliza ARP para mapear o IP destino ao endereço MAC correspondente.

</details>

<br>



**2. Qual é o endereço MAC de destino utilizado em um ARP Request?**

- [ ] A) MAC do servidor DHCP
- [ ] B) FF:FF:FF:FF:FF:FF
- [ ] C) 00:00:00:00:00:00
- [ ] D) MAC do gateway

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
ARP Requests são enviados em broadcast para todos os dispositivos da rede.

</details>

<br>



**3. Qual protocolo está identificado pelo valor hexadecimal 0x0806 no campo Type do quadro Ethernet?**

- [ ] A) IPv4
- [ ] B) ARP
- [ ] C) IPv6
- [ ] D) ICMP

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
O valor 0x0806 identifica pacotes ARP encapsulados em quadros Ethernet.

</details>

<br>



**4. Um host precisa enviar dados para o endereço IP 8.8.8.8. Qual será o MAC destino no quadro Ethernet inicial?**

- [ ] A) MAC do servidor Google
- [ ] B) Broadcast
- [ ] C) MAC do Default Gateway
- [ ] D) MAC do ISP

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
Quando o destino está em outra rede, o host envia o quadro ao roteador local.

</details>

<br>



**5. Um atacante envia respostas ARP falsas afirmando que o gateway pertence ao seu MAC. Qual ataque é esse?**

- [ ] A) MAC Flooding
- [ ] B) ARP Spoofing
- [ ] C) DHCP Starvation
- [ ] D) DNS Poisoning

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
O ARP Spoofing altera as tabelas ARP das vítimas permitindo interceptação de tráfego.

</details>

<br>



**6. Qual comando mostra a tabela ARP de um sistema?**

- [ ] A) ipconfig
- [ ] B) netstat
- [ ] C) arp -a
- [ ] D) nslookup

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
O comando arp -a exibe o cache ARP armazenado no sistema.

</details>

<br>



**7. Qual parte do endereço MAC identifica o fabricante da placa de rede?**

- [ ] A) Últimos 24 bits
- [ ] B) Campo Type
- [ ] C) Primeiros 24 bits (OUI)
- [ ] D) Preâmbulo

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
O OUI (Organizationally Unique Identifier) identifica o fabricante do hardware.

</details>

<br>



**8. Por que entradas ARP possuem tempo de expiração?**

- [ ] A) Porque IP muda a cada ping
- [ ] B) Para renovar DHCP
- [ ] C) Porque tabelas ocupam muito espaço
- [ ] D) Para manter informações atualizadas

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: D**

Explicação:  
Entradas expiradas evitam inconsistências caso dispositivos mudem de IP ou MAC.

</details>

<br>



**9. O que acontece se o FCS de um quadro Ethernet estiver incorreto?**

- [ ] A) O switch corrige
- [ ] B) A NIC descarta o quadro
- [ ] C) O roteador corrige
- [ ] D) O ARP retransmite

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
Erro no FCS indica corrupção durante transmissão.

</details>

<br>



**10. Qual campo do quadro Ethernet não aparece normalmente no Wireshark?**

- [ ] A) Source MAC
- [ ] B) Type
- [ ] C) Preamble
- [ ] D) FCS

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
O preâmbulo é tratado pelo hardware da placa de rede.

</details>

<br>



**11. Qual diferença entre ARP e ICMP?**

- [ ] A) ARP usa UDP
- [ ] B) ICMP é roteável entre redes
- [ ] C) ARP criptografa dados
- [ ] D) São protocolos equivalentes

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
ARP funciona apenas na LAN, enquanto ICMP pode atravessar roteadores.

</details>

<br>



**12. Qual comando limpa o cache ARP no Windows?**

- [ ] A) Reiniciar firewall
- [ ] B) arp -d *
- [ ] C) ping -t
- [ ] D) alterar DNS

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
Esse comando remove todas as entradas ARP.

</details>

<br>



**13. Qual tipo de comunicação representa um ARP Reply?**

- [ ] A) Broadcast
- [ ] B) Multicast
- [ ] C) Unicast
- [ ] D) Anycast

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
A resposta ARP é enviada diretamente ao solicitante.

</details>

<br>



**14. Qual protocolo pode gerar flooding natural em redes grandes?**

- [ ] A) HTTP
- [ ] B) ARP
- [ ] C) OSPF
- [ ] D) SMTP

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: B**

Explicação:  
ARP utiliza broadcast, o que pode gerar tráfego excessivo.

</details>

<br>



**15. O filtro "arp or icmp" no Wireshark mostra o que?**

- [ ] A) Erros L2 e L3
- [ ] B) Tráfego de roteamento
- [ ] C) Pacotes ARP e ICMP
- [ ] D) Todo tráfego TCP/IP

<details>
<summary><b>✅ Ver Gabarito</b></summary>

**Resposta correta: C**

Explicação:  
O filtro mostra apenas pacotes de descoberta ARP e mensagens ICMP.

</details>
