# 🌐 Module 6: Ethernet and Internet Protocol (IP)

## 1. The Network Layer (Layer 3)
A Camada de Rede (Layer 3 do modelo OSI) é responsável por rotear pacotes entre diferentes redes. Os dois principais protocolos desta camada são o **IPv4** e o **IPv6**. 


O protocolo IP possui três características fundamentais que você deve memorizar:
1. **Connectionless (Sem conexão):** O IP não estabelece uma conexão dedicada antes de enviar os dados. 
   * *Analogia:* É como colocar uma carta na caixa de correio. Você não avisa o destinatário que a carta está chegando e não sabe se ele está em casa para recebê-la. 2. **Best Effort (Melhor esforço / Não confiável):** O IP não garante a entrega dos pacotes. Se um pacote for perdido ou corrompido no caminho, o IP não tenta reenviá-lo. (Quem faz a checagem e reenvio é o TCP, na Camada 4).
3. **Media Independent (Independente do meio):** O IP não se importa se os dados estão viajando por cabos de cobre, fibra óptica ou ondas de rádio (Wi-Fi). Ele opera da mesma forma.

---

## 2. IP Packet Encapsulation & Headers
Quando os dados descem da Camada de Transporte (Segmento), a Camada de Rede adiciona seu próprio cabeçalho (IP Header), transformando o PDU em um **Pacote IP (IP Packet)**.


### Principais Campos do Cabeçalho IPv4:
* **Version:** Identifica se é IPv4 (0100) ou IPv6.
* **Differentiated Services (DS / DiffServ):** Usado para determinar a prioridade do pacote (QoS - Quality of Service).
* **Time to Live (TTL):** Evita loops infinitos na rede. É diminuído em 1 a cada roteador (hop) que o pacote passa. Se chegar a 0, o pacote é descartado e uma mensagem *ICMP Time Exceeded* é enviada à origem. (No IPv6, este campo foi renomeado para **Hop Limit**).
* **Protocol:** Identifica qual protocolo da camada superior está no payload (Ex: 1 para ICMP, 6 para TCP, 17 para UDP).
* **Source / Destination IP Address:** Os endereços lógicos de origem e destino (32 bits no IPv4).

---

## 3. Host Routing Decisions
Antes de um computador enviar um pacote, ele usa a operação matemática **Logical AND** (comparando o IP de destino com sua própria Máscara de Sub-rede) para decidir para onde enviar o pacote:

1. **Itself (Loopback):** `127.0.0.1` (IPv4) ou `::1` (IPv6). O pacote não sai da máquina. Usado para testar a própria placa de rede (TCP/IP stack).
2. **Local Host:** O destino está na mesma rede. O pacote é enviado diretamente para o MAC Address do dispositivo via Switch.
3. **Remote Host:** O destino está em outra rede (a matemática do AND não bateu). O pacote é enviado para o **Default Gateway** (o Roteador), que cuidará do roteamento.

---

## 4. IP Addressing & Subnetting Basics

### Private IPv4 Addresses (RFC 1918)
Endereços que não podem ser roteados na internet pública. São usados internamente em residências e empresas.
* **Classe A:** `10.0.0.0` a `10.255.255.255`
* **Classe B:** `172.16.0.0` a `172.31.255.255` *(Atenção à pegadinha do 31!)*
* **Classe C:** `192.168.0.0` a `192.168.255.255`

### Subnet Host Calculation
Fórmula para descobrir IPs utilizáveis em uma sub-rede: **2^h - 2** (onde *h* é o número de bits de host/zeros restantes).
* Exemplo (/26): Sobram 6 bits de host. 2^6 - 2 = **62 Hosts utilizáveis**.

---

## 5. IPv6 Fundamentals
Endereços de 128 bits escritos em formato Hexadecimal. A estrutura padrão divide o endereço no meio: 64 bits para o **Network Prefix** e 64 bits para o **Interface ID** (Host).

### Regras de Compressão:
1. **Omit Leading Zeros:** Você pode ocultar os zeros à esquerda de qualquer bloco (hexteto). Ex: `0db8` vira `db8`. `0000` vira `0`.
2. **Double Colon (::):** Substitui uma sequência contínua de blocos compostos apenas por zeros. **Só pode ser usado UMA vez por endereço.**

### IPv4-Mapped IPv6 Addresses
Forma de representar um IPv4 em uma rede IPv6.
Exemplo (`10.0.0.15`):
* **Híbrido:** `::ffff:10.0.0.15`
* **Hexadecimal Puro:** `::ffff:0a00:000f`

---

## 6. Ethernet (Layer 2 - Data Link)
A tecnologia Ethernet opera nas Camadas 1 (Física) e 2 (Enlace de Dados) do modelo OSI. A Camada de Enlace é dividida em duas subcamadas:
* **LLC (Logical Link Control - 802.2):** Comunica-se com o software (Camada de Rede / IP).
* **MAC (Media Access Control - 802.3):** Comunica-se com o hardware e controla o acesso físico ao meio.

### MAC Address Format
Endereço físico gravado na placa de rede. 
* Tem **48 bits** de tamanho.
* É representado por **12 dígitos Hexadecimais** (Ex: `00-D0-D3-BE-79-75`).

---

## 7. The Ethernet Frame
O PDU da Camada 2 é o **Frame (Quadro)**. O tamanho de um frame Ethernet deve ser de no **mínimo 64 bytes** e no **máximo 1518 bytes**.
* **Runt Frame / Collision Fragment:** Qualquer frame menor que 64 bytes. É descartado automaticamente.
* **Jumbo Frame:** Frames maiores que 1500 bytes de payload (suportados por conexões Gigabit).


### Campos do Frame Ethernet:
1. **Preamble & SFD:** (8 bytes) Usado para sincronização. "Acorda" os receptores avisando que um frame está chegando. *(Não entra na conta do tamanho do frame).*
2. **Destination MAC:** (6 bytes) O MAC de quem vai receber. Pode ser Unicast, Multicast ou Broadcast.
3. **Source MAC:** (6 bytes) O MAC de quem está enviando. (Sempre Unicast).
4. **Type / Length:** (2 bytes) Identifica o protocolo da camada superior (Ex: `0x800` para IPv4, `0x86DD` para IPv6).
5. **Data:** (46 - 1500 bytes) O payload, geralmente o Pacote IP. Se for muito pequeno, um "Padding" (preenchimento) é adicionado para atingir o mínimo de 64 bytes.
6. **FCS (Frame Check Sequence):** (4 bytes) Usa CRC (Cyclic Redundancy Check) para verificar se o frame foi corrompido durante a viagem. Se o cálculo do destino for diferente da origem, o frame é destruído.
