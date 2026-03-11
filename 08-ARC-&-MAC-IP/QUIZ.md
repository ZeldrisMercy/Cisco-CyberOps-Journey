# 🧠 Simulado Definitivo: Module 08 (ARP & MAC/IP)
Este simulado contém 15 questões de nível de certificação, focadas nos objetivos oficiais do exame **Cisco CBROPS 200-201**. Ele testa a sua capacidade de compreender o funcionamento do protocolo ARP, a relação entre endereços MAC e IP, o comportamento de quadros Ethernet e a análise de tráfego em cenários reais de rede e segurança.

---

### 🌐 Domínio 1: ARP e Descoberta de Endereços



**1. Quando um dispositivo precisa enviar dados para um destino que está na mesma sub-rede IPv4, como ele descobre o endereço MAC de destino?**
- [ ] A) Consulta o servidor DNS
- [ ] B) Envia o pacote ao gateway
- [ ] C) Verifica a tabela de roteamento
- [ ] D) Consulta o cache ARP ou envia um ARP Request

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> Para comunicação local o dispositivo utiliza o protocolo <b>ARP (Address Resolution Protocol)</b> para mapear um endereço IP ao endereço MAC correspondente. Primeiro verifica o cache ARP; se não encontrar, envia um <b>ARP Request em broadcast</b>.
</details>
<br>

**2. Qual é o endereço MAC de destino utilizado em um ARP Request?**
- [ ] A) MAC do servidor DHCP
- [ ] B) FF:FF:FF:FF:FF:FF
- [ ] C) 00:00:00:00:00:00
- [ ] D) MAC do gateway

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> ARP Requests são enviados em <b>broadcast na camada 2</b>. O endereço MAC FF:FF:FF:FF:FF:FF indica que todos os dispositivos no segmento de rede local devem receber o quadro.
</details>
<br>

**3. Qual protocolo está identificado pelo valor hexadecimal 0x0806 no campo Type do quadro Ethernet?**
- [ ] A) IPv4
- [ ] B) ARP
- [ ] C) IPv6
- [ ] D) ICMP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O campo <b>EtherType</b> do quadro Ethernet identifica qual protocolo está encapsulado. O valor hexadecimal <b>0x0806</b> indica que o quadro transporta uma mensagem ARP.
</details>
<br>

**4. Um host precisa enviar dados para o endereço IP 8.8.8.8. Qual será o MAC destino no quadro Ethernet inicial?**
- [ ] A) MAC do servidor Google
- [ ] B) Broadcast
- [ ] C) MAC do Default Gateway
- [ ] D) MAC do ISP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Quando o destino está fora da rede local, o host envia o pacote ao <b>Default Gateway</b>. Assim, o quadro Ethernet utiliza o MAC do roteador local como destino inicial.
</details>
<br>

---

### 🛡️ Domínio 2: Segurança e Manipulação do ARP



**5. Um atacante envia respostas ARP falsas afirmando que o gateway pertence ao seu MAC. Qual ataque é esse?**
- [ ] A) MAC Flooding
- [ ] B) ARP Spoofing
- [ ] C) DHCP Starvation
- [ ] D) DNS Poisoning

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O <b>ARP Spoofing</b> ocorre quando um atacante envia respostas ARP falsas para alterar o cache ARP das vítimas. Isso permite ataques como <b>Man-in-the-Middle</b>, interceptação de tráfego e roubo de credenciais.
</details>
<br>

---

### 🔍 Domínio 3: Tabelas ARP e Estrutura de Endereços



**6. Qual comando mostra a tabela ARP de um sistema?**
- [ ] A) ipconfig
- [ ] B) netstat
- [ ] C) arp -a
- [ ] D) nslookup

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O comando <b>arp -a</b> mostra o cache ARP armazenado no sistema, exibindo o mapeamento entre endereços IP e endereços MAC conhecidos.
</details>
<br>

**7. Qual parte do endereço MAC identifica o fabricante da placa de rede?**
- [ ] A) Últimos 24 bits
- [ ] B) Campo Type
- [ ] C) Primeiros 24 bits (OUI)
- [ ] D) Preâmbulo

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>OUI (Organizationally Unique Identifier)</b> corresponde aos primeiros 24 bits do endereço MAC e identifica o fabricante do hardware de rede.
</details>
<br>

**8. Por que entradas ARP possuem tempo de expiração?**
- [ ] A) Porque IP muda a cada ping
- [ ] B) Para renovar DHCP
- [ ] C) Porque tabelas ocupam muito espaço
- [ ] D) Para manter informações atualizadas

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> Entradas ARP possuem tempo de expiração para evitar inconsistências caso dispositivos mudem de IP ou MAC, garantindo que a tabela ARP permaneça atualizada.
</details>
<br>

---

### 🧱 Domínio 4: Quadros Ethernet e Integridade de Dados



**9. O que acontece se o FCS de um quadro Ethernet estiver incorreto?**
- [ ] A) O switch corrige
- [ ] B) A NIC descarta o quadro
- [ ] C) O roteador corrige
- [ ] D) O ARP retransmite

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O campo <b>Frame Check Sequence (FCS)</b> permite detectar erros de transmissão. Se o valor calculado não corresponder ao recebido, a placa de rede descarta o quadro.
</details>
<br>

**10. Qual campo do quadro Ethernet não aparece normalmente no Wireshark?**
- [ ] A) Source MAC
- [ ] B) Type
- [ ] C) Preamble
- [ ] D) FCS

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>preamble</b> é utilizado para sincronização no nível físico e normalmente é processado pelo hardware da NIC, não aparecendo nas capturas do Wireshark.
</details>
<br>

---

### 🔗 Domínio 5: Protocolos e Comunicação na Rede



**11. Qual diferença entre ARP e ICMP?**
- [ ] A) ARP usa UDP
- [ ] B) ICMP é roteável entre redes
- [ ] C) ARP criptografa dados
- [ ] D) São protocolos equivalentes

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O ARP opera apenas dentro da rede local (LAN), enquanto o <b>ICMP</b> pode atravessar roteadores e redes diferentes, sendo usado para diagnósticos como o comando <b>ping</b>.
</details>
<br>

**12. Qual comando limpa o cache ARP no Windows?**
- [ ] A) Reiniciar firewall
- [ ] B) arp -d *
- [ ] C) ping -t
- [ ] D) alterar DNS

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O comando <b>arp -d *</b> remove todas as entradas do cache ARP, forçando o sistema a descobrir novamente os endereços MAC necessários.
</details>
<br>

---

### 📡 Domínio 6: Tipos de Comunicação em Rede



**13. Qual tipo de comunicação representa um ARP Reply?**
- [ ] A) Broadcast
- [ ] B) Multicast
- [ ] C) Unicast
- [ ] D) Anycast

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Enquanto o <b>ARP Request</b> é enviado em broadcast, o <b>ARP Reply</b> é enviado diretamente ao host que fez a solicitação, caracterizando comunicação <b>unicast</b>.
</details>
<br>

**14. Qual protocolo pode gerar flooding natural em redes grandes?**
- [ ] A) HTTP
- [ ] B) ARP
- [ ] C) OSPF
- [ ] D) SMTP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Como o ARP utiliza broadcast para descobrir endereços MAC, redes grandes podem gerar grande volume de tráfego ARP, causando <b>ARP flooding</b>.
</details>
<br>

---

### 🦈 Domínio 7: Análise de Tráfego e Wireshark



**15. O filtro "arp or icmp" no Wireshark mostra o que?**
- [ ] A) Erros L2 e L3
- [ ] B) Tráfego de roteamento
- [ ] C) Pacotes ARP e ICMP
- [ ] D) Todo tráfego TCP/IP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O filtro <b>arp or icmp</b> exibe apenas pacotes ARP (descoberta de MAC) e ICMP (mensagens de diagnóstico como ping), facilitando a análise de conectividade e descoberta de rede.
</details>
