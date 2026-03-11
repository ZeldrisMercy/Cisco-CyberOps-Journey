# 📁 Module 07: Connectivity Verification

> [!NOTE]
> **Resumo Executivo:** Este módulo explora as ferramentas e protocolos essenciais que os analistas de segurança usam para testar, rastrear e solucionar problemas de conectividade em redes IP. O grande foco é a transição das mensagens ICMPv4 clássicas para o ecossistema robusto do ICMPv6, incluindo a Descoberta de Vizinhos (Neighbor Discovery - ND) e a Autoconfiguração (SLAAC). O domínio deste módulo é vital para diagnosticar ataques de negação de serviço e spoofing no exame CBROPS 200-201.

---

## 📡 1. O Protocolo ICMP (Internet Control Message Protocol)

O ICMP é o protocolo "mensageiro" da Camada de Rede (L3). Diferente do TCP ou UDP que transportam dados de aplicações, o ICMP transporta informações de diagnóstico e erros de roteamento.

### Mensagens ICMP Comuns (v4 e v6)
* **Host Confirmation:** Mensagens de *Echo Request* (Solicitação) e *Echo Reply* (Resposta) são usadas pelo comando `ping` para confirmar se um host está vivo.
* **Destination or Service Unreachable:** Um roteador ou host avisa que o pacote não pode ser entregue (ex: rota inexistente ou porta bloqueada por firewall).
* **Time Exceeded:** Um roteador avisa que o pacote expirou. No IPv4, isso ocorre quando o campo TTL (Time to Live) chega a 0; no IPv6, quando o Hop Limit chega a 0.

---

## 🌍 2. O Poder do ICMPv6 (Neighbor Discovery Protocol - NDP)

O IPv6 não utiliza broadcasts e não possui o protocolo ARP (Address Resolution Protocol). Em vez disso, ele incorpora essas funções de forma mais segura e eficiente dentro do ICMPv6 através do Neighbor Discovery (ND).


### A. Mensagens entre Roteador e Dispositivo (RS e RA)
Usadas para roteamento dinâmico e SLAAC (Stateless Address Autoconfiguration):
* **Router Solicitation (RS):** Quando um host IPv6 inicializa, ele envia uma mensagem RS em multicast solicitando informações da rede local ("Acabei de iniciar, enviem-me um RA").
* **Router Advertisement (RA):** Os roteadores enviam RAs periodicamente (ex: a cada 200 segundos) ou em resposta a um RS. O RA contém o prefixo da rede, tamanho do prefixo, DNS, e permite que o host configure seu Gateway Padrão usando o endereço *Link-Local* do roteador.

### B. Mensagens entre Dispositivos (NS e NA)
Substituem o ARP do IPv4 para descobrir endereços MAC (Resolução de Endereços):
* **Neighbor Solicitation (NS):** Se o Host A conhece o IPv6 do Host B, mas não seu MAC, ele envia um NS ("Eu sei seu IP, qual é o seu MAC?").
* **Neighbor Advertisement (NA):** O alvo responde com sua identidade ("Aqui está meu endereço MAC").

### C. DAD (Duplicate Address Detection)
Para evitar conflitos de IP, quando um dispositivo IPv6 gera seu próprio endereço (SLAAC ou Link-Local), ele deve testar se o endereço é único.
* O dispositivo envia uma mensagem NS direcionada **ao próprio IP que deseja usar**.
* Se ninguém responder com um NA após um tempo, o endereço é único e seguro para uso.

---

## 🛠️ 3. Utilitários de Teste: Ping e Traceroute

A base do Troubleshooting operacional.

* **Ping (Test Connectivity):** Testa a conectividade de ponta a ponta medindo o tempo de resposta.
    * *Ping ao Loopback (127.0.0.1 ou ::1):* Testa se a própria pilha TCP/IP do computador está funcionando.
    * *Ping ao Gateway Padrão:* Testa a comunicação até o roteador local, isolando problemas na LAN.
* **Traceroute (Test the Path):** Identifica a rota exata (saltos/hops) que o pacote faz até o destino. No Windows, o comando é `tracert`; no Linux/Cisco, é `traceroute`.

---

## 📑 Tactical Field Report: Lab Executions

### 🔬 Lab 7.2.8: Packet Tracer - Verify IPv4 and IPv6 Addressing
**Objetivo:** Validar uma infraestrutura *Dual-Stack* (rodando IPv4 e IPv6 simultaneamente) auditando IPs, testando rotas e mapeando o tráfego inter-redes.

**Execução em Campo:**
1.  **Auditoria Lógica L3:** Nos terminais (PC1 e PC2), executamos `ipconfig /all` e `ipv6config /all` para documentar os endereços Unicast Globais e Link-Local (fe80::) atribuídos pela rede.
2.  **Verificação de Conectividade Base:** Lançamos comandos `ping` diretos do PC1 para o IPv4 (10.10.1.20) e IPv6 (2001:db8:1:4::a) do PC2 para provar a coexistência do *Dual-Stack* sem interferência.
3.  **Mapeamento de Vetor (Tracert):** Lançamos `tracert 10.10.1.20` e `tracert 2001:db8:1:4::a`. Observamos como os pacotes IPv4 cruzavam as interfaces `10.10.x.x` dos Roteadores R1, R2 e R3, enquanto o mesmo comando IPv6 traçava perfeitamente o caminho através dos IPs `2001:db8:...` nas mesmas interfaces físicas, comprovando o roteamento independente para cada protocolo.
