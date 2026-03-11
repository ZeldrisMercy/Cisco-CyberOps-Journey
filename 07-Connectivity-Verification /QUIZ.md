# 🧠 Simulado Definitivo: Module 07 (Connectivity Verification)

Este simulado foca nos mecanismos do ICMP, resolução de vizinhos e ferramentas vitais de diagnóstico, alinhado aos cenários que você encontrará na certificação **Cisco CBROPS 200-201**.

---

### 📡 Domínio 1: O Protocolo ICMP e Mensagens de Diagnóstico

**1. No modelo TCP/IP, protocolos como TCP e UDP transportam dados de aplicações. Qual é a função central do protocolo ICMP (Internet Control Message Protocol) na Camada de Rede?**
a) Estabelecer canais seguros de comunicação encriptada entre roteadores de borda.
b) Realizar a tradução de endereços IP privados para endereços IP públicos roteáveis.
c) Fornecer mensagens de diagnóstico, testes de conectividade e relatar erros de roteamento.
d) Garantir a entrega confiável e sequencial de pacotes entre o remetente e o destinatário.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Fornecer mensagens de diagnóstico, testes de conectividade e relatar erros de roteamento.
**Explicação:** O ICMP atua como o protocolo "mensageiro" do IP. Ele não carrega dados de utilizador, mas reporta problemas (como destinos inalcançáveis) e permite diagnósticos (como o Ping).
</details>

<br>

**2. Durante um ataque de negação de serviço ou um loop de roteamento, pacotes podem ficar presos na rede. O que acontece quando o campo TTL (IPv4) ou Hop Limit (IPv6) chega a zero num roteador?**
a) O roteador recarrega o TTL para 255 e reencaminha o pacote.
b) O roteador encapsula o pacote num quadro Ethernet de broadcast.
c) O roteador descarta o pacote e envia uma mensagem ICMP "Time Exceeded" ao remetente.
d) O roteador envia uma mensagem de "Echo Reply" para o destino final.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) O roteador descarta o pacote e envia uma mensagem ICMP "Time Exceeded" ao remetente.
**Explicação:** Este mecanismo anti-loop destrói o pacote expirado e utiliza o ICMP para avisar a máquina de origem que o tráfego se perdeu no caminho.
</details>

<br>

**3. No protocolo ICMPv4, como a estrutura do cabeçalho distingue exatamente o propósito de uma mensagem de controle (por exemplo, diferenciar entre um simples ping e um aviso de rota inalcançável)?**
a) Através da variação de bits na subcamada LLC.
b) Pelos campos "Type" e "Code" no cabeçalho ICMP.
c) Lendo e processando dados armazenados no campo TTL estendido.
d) Avaliando a porta lógica de origem usada pelo UDP.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Pelos campos "Type" e "Code" no cabeçalho ICMP.
**Explicação:** O "Type" define a classe do evento (ex: Tipo 8 = Echo Request, Tipo 3 = Destination Unreachable) e o "Code" especifica o motivo exato dentro dessa classe.
</details>

<br>

**4. Num contexto de SOC, a equipe detecta a geração de mensagens ICMP "Redirect". Qual é o motivo para um roteador enviar essa mensagem a uma máquina corporativa?**
a) O roteador informa à máquina que existe um caminho melhor (outro roteador) na mesma rede local para alcançar o destino desejado.
b) O servidor detectou anomalias no tráfego HTTPS e está forçando o cliente a reconectar.
c) A interface física do switch foi desativada e o tráfego deve fluir pelo circuito de backup.
d) A máquina alcançou o seu limite de banda de Quality of Service (QoS).

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** a) O roteador informa à máquina que existe um caminho melhor (outro roteador) na mesma rede local para alcançar o destino desejado.
**Explicação:** O ICMP Redirect otimiza o roteamento avisando o host que ele enviou o pacote para o gateway errado, quando havia um atalho mais eficiente no mesmo segmento LAN.
</details>

<br>

---

### 🌍 Domínio 2: O Poder do ICMPv6 e Neighbor Discovery (NDP)

**5. Uma rede corporativa migrou para o protocolo IPv6. Como o IPv6 resolve a ausência do protocolo ARP (usado no IPv4) para a resolução de endereços MAC na rede local?**
a) Através do uso extensivo de pacotes de Broadcast em Nível 2.
b) Utilizando o Neighbor Discovery Protocol (NDP), com mensagens NS (Neighbor Solicitation) e NA (Neighbor Advertisement).
c) Consultando um servidor DNS centralizado na rede corporativa.
d) Aplicando um cálculo matemático fixo nos últimos 64 bits do endereço IPv6.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Utilizando o Neighbor Discovery Protocol (NDP), com mensagens NS (Neighbor Solicitation) e NA (Neighbor Advertisement). 
**Explicação:** O Host A envia um NS em multicast perguntando "Quem tem este IPv6?", e o alvo responde diretamente com um NA fornecendo o seu MAC Address.
</details>

<br>

**6. Num ambiente com SLAAC, um host IPv6 recém-conectado precisa descobrir o prefixo da rede para se autoconfigurar. Qual par de mensagens ICMPv6 realiza este processo?**
a) Echo Request e Echo Reply.
b) Neighbor Solicitation (NS) e Neighbor Advertisement (NA).
c) Router Solicitation (RS) e Router Advertisement (RA).
d) Destination Unreachable e Time Exceeded.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Router Solicitation (RS) e Router Advertisement (RA).
**Explicação:** O host emite um RS perguntando pelas configurações da rede. Os roteadores locais respondem com um RA, entregando o prefixo da sub-rede para que a máquina crie o seu próprio IP.
</details>

<br>

**7. O Duplicate Address Detection (DAD) previne conflitos de IP no IPv6. Como um dispositivo verifica se o IP que deseja usar está livre na rede?**
a) Envia um Echo Request para o endereço de broadcast da rede.
b) Pergunta ao servidor DHCPv6 central se o IP está em lease.
c) Envia uma mensagem NS direcionada ao próprio endereço IP que deseja assumir e aguarda para ver se alguém responde.
d) Executa um ARP reverso no switch local.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Envia uma mensagem NS direcionada ao próprio endereço IP que deseja assumir e aguarda para ver se alguém responde.
**Explicação:** Se houver um NA de resposta, significa que outro host já possui esse IP. Se houver silêncio, o IP é único e seguro para ser utilizado.
</details>

<br>

**8. Qual tipo de endereço IPv6 possui escopo focado apenas na rede local (mesmo link), é essencial para o descobrimento de vizinhos (NDP), não é roteável para a internet e tipicamente começa com `fe80::`?**
a) Global Unicast
b) Link-Local
c) Unique Local
d) Loopback

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Link-Local
**Explicação:** Todo o tráfego de controle local do IPv6 (incluindo a comunicação com o Gateway Padrão em ambientes SLAAC) ocorre utilizando endereços Link-Local.
</details>

<br>

**9. Por que um ataque clássico de amplificação como o "Smurf", que causa negação de serviço, não é viável em infraestruturas puramente IPv6?**
a) O IPv6 descarta nativamente pacotes ICMP não criptografados pelo IPsec.
b) A arquitetura do protocolo IPv6 eliminou o uso de endereços de broadcast, impossibilitando a amplificação de respostas em massa.
c) O tráfego IPv6 possui verificações matemáticas inquebráveis baseadas no MAC.
d) Os pacotes ICMPv6 não contêm mais o campo equivalente ao TTL.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) A arquitetura do protocolo IPv6 eliminou o uso de endereços de broadcast, impossibilitando a amplificação de respostas em massa.
**Explicação:** O Smurf falsificava o IP de origem e disparava pings para o endereço de broadcast IPv4, forçando todos os hosts a responderem ao alvo. O IPv6 substituiu o broadcast pelo multicast, mitigando essa técnica.
</details>

<br>

---

### 🛠️ Domínio 3: Utilitários de Teste e Troubleshooting (Ping e Traceroute)

**10. Uma estação falha ao se conectar à internet. O analista executa o comando `ping 127.0.0.1` (ou `ping ::1`) e o teste funciona. O que isto valida isoladamente?**
a) Que o cabo de rede está conectado ao switch físico.
b) Que a pilha TCP/IP interna e os drivers de rede do próprio computador estão operacionais.
c) Que a resolução de nomes (DNS) está a funcionar corretamente.
d) Que o roteador da rede local está alcançável.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Que a pilha TCP/IP interna e os drivers de rede do próprio computador estão operacionais.
**Explicação:** O endereço de Loopback nunca sai da placa de rede para o cabo físico. Este ping confirma apenas que a infraestrutura lógica do sistema operativo está saudável.
</details>

<br>

**11. Enquanto o ping testa a conectividade, o utilitário Traceroute mapeia os saltos até ao destino. Qual técnica o Traceroute utiliza para forçar os roteadores intermediários a revelarem a sua identidade?**
a) Envia mensagens NS (Neighbor Solicitation) em cada salto físico da rede.
b) Altera a porta de origem do UDP a cada pacote enviado.
c) Inicia o campo TTL (ou Hop Limit) em 1 e incrementa-o sequencialmente, forçando os roteadores a responderem com erros "Time Exceeded".
d) Inunda a rede com requisições ARP corrompidas.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Inicia o campo TTL (ou Hop Limit) em 1 e incrementa-o sequencialmente, forçando os roteadores a responderem com erros "Time Exceeded".
**Explicação:** O roteador 1 recebe o pacote com TTL=1, descarta e responde. O Traceroute regista. Depois envia com TTL=2, o roteador 2 descarta e responde. O processo repete-se até o destino ser alcançado.
</details>

<br>

**12. Ao analisar um tráfego de "Echo Request" entre duas máquinas IPv4, o analista verifica os tipos de mensagem ICMP no Wireshark. Quais são os valores de "Type" padrão para o Ping no IPv4?**
a) Type 3 para a solicitação e Type 4 para a resposta.
b) Type 8 para a solicitação (Request) e Type 0 para a resposta (Reply).
c) Type 133 para a solicitação e Type 134 para a resposta.
d) Type 128 para a solicitação e Type 129 para a resposta.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Type 8 para a solicitação (Request) e Type 0 para a resposta (Reply).
**Explicação:** No protocolo ICMPv4, o Ping inicia a sondagem com o Tipo 8, e a máquina de destino responde com o Tipo 0. (Nota: 128 e 129 são os equivalentes no ICMPv6).
</details>

<br>

---

### 📑 Domínio 4: Operações Práticas e Dual-Stack

**13. Num contexto de infraestrutura moderna abordada no CBROPS, o que caracteriza uma rede "Dual-Stack" (Pilha Dupla)?**
a) A utilização de dois firewalls de perímetro em modo Ativo-Passivo.
b) O encapsulamento de pacotes IPv4 inteiros dentro de túneis IPv6.
c) A segmentação física entre tráfego de dados e tráfego de telefonia (VLANs).
d) A presença nativa e simultânea dos protocolos IPv4 e IPv6 ativados nas mesmas interfaces e equipamentos.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) A presença nativa e simultânea dos protocolos IPv4 e IPv6 ativados nas mesmas interfaces e equipamentos.
**Explicação:** No modo Dual-Stack, os equipamentos têm endereços IPv4 e IPv6 atribuídos simultaneamente, processando e roteando o tráfego de ambos os protocolos lado a lado de forma independente.
</details>

<br>

**14. Um pacote destinado a um IP público chega ao roteador corporativo. O roteador verifica a tabela, não encontra rota explícita e não possui Gateway Padrão. Qual é a reação correta do equipamento?**
a) Encaminhar o pacote em broadcast por todas as portas.
b) Reter o pacote na memória RAM aguardando uma rota OSPF.
c) Destruir o pacote e enviar um erro ICMP "Destination Unreachable" à máquina emissora.
d) Descartar o pacote silenciosamente sem avisar a origem.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Destruir o pacote e enviar um erro ICMP "Destination Unreachable" à máquina emissora.
**Explicação:** Sem rota e sem gateway de último recurso, a Camada 3 decreta falha imediata e notifica a origem para que não mantenha a conexão pendente.
</details>

<br>

**15. Em redes configuradas exclusivamente com SLAAC (sem DHCPv6), o host depende da mensagem Router Advertisement (RA) do roteador para descobrir o seu Gateway Padrão. Geralmente, qual endereço o roteador fornece como Gateway nessa mensagem?**
a) O seu próprio endereço Link-Local (fe80::).
b) O seu endereço Global Unicast (IP público).
c) O endereço de Loopback encapsulado (::1).
d) O endereço MAC de broadcast.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** a) O seu próprio endereço Link-Local (fe80::).
**Explicação:** Para garantir máxima estabilidade no acesso dentro da rede local, o SLAAC instrui os hosts a utilizarem o endereço não-roteável (Link-Local) do roteador como o seu portal de saída.
</details>

<br>
