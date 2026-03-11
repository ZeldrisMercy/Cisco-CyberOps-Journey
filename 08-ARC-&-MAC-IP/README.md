# 📁 Module 08: Address Resolution Protocol (ARP) & MAC/IP

> [!NOTE]
> **Resumo Executivo:** Este módulo explora como dispositivos conseguem entregar pacotes dentro de uma rede local utilizando dois tipos de endereçamento fundamentais: **endereços IP (lógicos)** e **endereços MAC (físicos)**.  
> O protocolo **ARP (Address Resolution Protocol)** atua como a ponte que conecta esses dois mundos.  
> Sem ele, os dispositivos saberiam **para qual IP enviar os dados**, mas não saberiam **qual interface física deve receber o quadro Ethernet**.  
> Além do funcionamento normal do ARP, também exploramos suas **limitações de segurança**, como ataques de **ARP Spoofing**, além da análise prática de quadros Ethernet e tráfego ARP utilizando **Wireshark**.

---

## 🧭 8.1 MAC and IP: A Dupla Dinâmica do Roteamento

Na comunicação em rede, cada dispositivo possui **dois identificadores essenciais**:

| Tipo de Endereço | Camada | Função |
|------------------|-------|-------|
| **IP Address** | Camada 3 (Rede) | Identifica o dispositivo na rede lógica |
| **MAC Address** | Camada 2 (Enlace) | Identifica fisicamente a interface de rede |

Uma analogia comum:

- **IP Address:** como o CEP de uma casa
- **MAC Address:** como a pessoa que recebe a encomenda na porta

O endereço IP permite **roteamento entre redes**, enquanto o endereço MAC permite **entrega dentro da rede local (LAN)**.

---

### 8.1.1 Destination on Same Network (Destino na Mesma Rede)

Quando dois dispositivos estão **na mesma sub-rede**, a comunicação acontece diretamente entre eles.

#### Processo

1. O host verifica se o **IP destino pertence à mesma sub-rede**.
2. Caso pertença, ele precisa descobrir o **MAC Address correspondente ao IP destino**.
3. Para isso, utiliza **ARP Request**.

Depois que o MAC é descoberto:

- O pacote IP é encapsulado dentro de um **quadro Ethernet**
- O quadro é enviado diretamente ao destino
- Nenhum roteador participa da comunicação

---

### 8.1.2 Destination on Remote Network (Destino em Rede Remota)

Quando o IP de destino pertence **a outra rede**, o host precisa enviar o pacote para o **Default Gateway**.

Nesse caso:

| Campo | Valor |
|------|------|
| **IP destino** | permanece o IP do servidor final |
| **MAC destino** | passa a ser o MAC do roteador |

Isso acontece porque o roteador é responsável por **encaminhar o pacote até a rede correta**.

#### Regra fundamental do roteamento

- O **IP permanece constante de ponta a ponta**
- O **MAC muda a cada salto (hop)**

---

## 🔎 8.2 ARP: O Protocolo de Resolução de Endereços

O **ARP (Address Resolution Protocol)** resolve um problema fundamental:

> Como descobrir o endereço MAC de um dispositivo sabendo apenas seu IP?

Ele atua exclusivamente dentro da **rede local (LAN)**.

---

### 8.2.1 & 8.2.2 ARP Overview and Functions

O ARP possui duas funções principais:

#### 1. Resolver IP → MAC

Quando um host precisa enviar dados para outro dispositivo da mesma rede, ele precisa descobrir o MAC correspondente ao IP destino.

#### 2. Manter a ARP Table

Os resultados são armazenados em cache na memória RAM.

Exemplo de entrada ARP:

```
192.168.1.7 → AA:BB:CC:DD:EE:FF
```

Isso evita que novas requisições ARP sejam enviadas constantemente.

---

### O Processo de Comunicação ARP

#### ARP Request (Broadcast)

Quando o MAC destino não está no cache, o host envia um broadcast perguntando:

```
Quem possui o IP 192.168.1.7 ?
```

O endereço MAC de destino do quadro será:

```
FF:FF:FF:FF:FF:FF
```

Esse endereço representa **broadcast Ethernet**, ou seja, todos os dispositivos da rede recebem o quadro.

---

#### ARP Reply (Unicast)

Somente o dispositivo que possui aquele IP responde:

```
Eu sou 192.168.1.7
Meu MAC é AA:BB:CC:DD:EE:FF
```

Essa resposta é enviada diretamente ao solicitante.

---

### 8.2.6 & 8.2.7 ARP Tables e Remoção de Entradas

As entradas da tabela ARP **não são permanentes**.

Elas possuem um **tempo de expiração**, normalmente entre:

```
2 a 20 minutos
```

Isso evita problemas caso:

- dispositivos sejam removidos da rede
- placas de rede sejam trocadas
- endereços IP mudem

---

### Comandos úteis

Visualizar tabela ARP:

```
arp -a
```

Remover entrada ARP:

```
arp -d <endereço IP>
```

Exemplo:

```
arp -d 192.168.1.7
```

---

## ⚠️ 8.3 ARP Issues: Ameaças e Problemas Inerentes

O ARP foi criado quando **segurança de rede ainda não era uma preocupação**.

Ele assume que **todos os dispositivos são confiáveis**, o que cria vulnerabilidades.

---

### 8.3.1 ARP Broadcasts (Overhead de Broadcast)

As requisições ARP são enviadas em **broadcast**, o que significa que **todos os dispositivos da LAN precisam processar o pacote**.

Em redes muito grandes isso pode causar:

- consumo excessivo de CPU
- congestionamento
- degradação de desempenho

Esse fenômeno é chamado de **Broadcast Flooding**.

---

### 8.3.2 ARP Spoofing / ARP Poisoning

Uma das técnicas mais comuns de ataque em redes locais.

#### Funcionamento

O atacante envia uma resposta ARP falsa dizendo:

```
O IP do Gateway agora pertence ao meu MAC
```

Antes do ataque:

```
192.168.1.1 → MAC do roteador
```

Depois do ataque:

```
192.168.1.1 → MAC do atacante
```

---

### Resultado

As vítimas passam a enviar todo o tráfego ao atacante.

Isso permite:

- interceptação de dados
- captura de credenciais
- manipulação de pacotes

Esse tipo de ataque é conhecido como **Man-in-the-Middle (MITM)**.

---

## 📑 Tactical Field Report: Lab Executions (8.2.8)

Neste laboratório utilizamos:

- **CyberOps Workstation VM**
- **Wireshark**
- **Mininet**

para analisar o funcionamento do ARP e dos quadros Ethernet.

---

### 🔬 Parte 1: Estrutura de um Quadro Ethernet II

| Campo | Tamanho | Função |
|------|------|------|
| Preamble | 8 bytes | Sincronização do hardware |
| Destination MAC | 6 bytes | MAC de destino |
| Source MAC | 6 bytes | MAC de origem |
| Type | 2 bytes | Tipo de protocolo |
| Data | 46–1500 bytes | Dados encapsulados |
| FCS | 4 bytes | Verificação de erro |

---

#### Valores comuns do campo Type

```
0x0800 → IPv4
0x0806 → ARP
```

---

### FCS (Frame Check Sequence)

O FCS funciona como um **selo de integridade**.

Se o cálculo do receptor não corresponder ao valor do FCS:

> o quadro é descartado automaticamente.

---

### 🦈 Parte 2: Prova Prática do Roteamento

No Mininet criamos o seguinte ambiente:

```
LAN: 10.0.0.0/24
Hosts: H1 H2 H3
Router: R1
Rede Remota: 172.16.0.0/12
Host remoto: H4
```

---

#### Experimento

No host H3 executamos:

```
arp -d
ping 10.0.0.1
```

---

### Descoberta 1 — Comunicação Local

Ao analisar os quadros capturados:

- MAC origem → H3
- MAC destino → Router

---

### Descoberta 2 — Comunicação Remota

Ao pingar o host remoto:

```
ping 172.16.0.40
```

O Wireshark mostrou que:

```
MAC destino = MAC do Gateway
```

---

### Regra fundamental

> Pacotes destinados a redes externas sempre usam o **MAC do Default Gateway** na camada 2.
