# 🧠 Simulado Definitivo Expandido: Module 11 (Devices & Wireless)
Simulado aprofundado com 15 questões de nível de certificação sobre processos de forwarding, tabelas MAC, Spanning Tree e protocolos 802.11.

---

### 🏗️ Domínio 1: Switching, Roteamento e Processos L2/L3

**1. Durante o "End-to-End Packet Forwarding", quando um pacote atravessa três roteadores diferentes na internet para chegar ao destino, o que acontece com os endereços de Camada 2 (MAC) e Camada 3 (IP)?**
- [ ] A) O MAC de origem não muda, mas o MAC de destino muda a cada salto.
- [ ] B) Ambos MAC e IP são substituídos pelo roteador a cada salto.
- [ ] C) Os endereços IP de origem e destino permanecem inalterados, mas os MACs de origem e destino são recriados a cada salto.
- [ ] D) Os IPs de origem e destino mudam com base na tabela ARP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O endereço IP é lógico e representa o trajeto de ponta a ponta. O endereço MAC é físico e só tem validade no link local. Por isso, a cada roteador (salto), o quadro de Camada 2 é destruído e refeito, enquanto o pacote IP de Camada 3 se mantém intacto.
</details>
<br>

**2. Um switch LAN vazio acabou de ser ligado. O PC-A (MAC AA:AA) envia um frame unicast para o PC-B (MAC BB:BB). O que o switch faz imediatamente ao receber este primeiro frame na Porta 1?**
- [ ] A) Descarta o pacote porque a tabela MAC está vazia.
- [ ] B) Grava o MAC AA:AA na sua Tabela MAC associado à Porta 1, e faz o "flooding" (inundação) do frame para todas as outras portas ativas.
- [ ] C) Grava o MAC BB:BB na sua tabela e envia de volta ao PC-A.
- [ ] D) Envia um ARP Request para descobrir o IP do PC-B.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O switch *aprende* lendo o MAC de Origem (grava o PC-A na porta 1). Como ele ainda não sabe onde está o MAC de Destino (PC-B), ele inunda o quadro para todas as portas, exceto a porta de entrada (Unknown Unicast Flooding).
</details>
<br>

**3. Qual é o propósito da inserção da tag IEEE 802.1Q (de 4 bytes) em um frame Ethernet?**
- [ ] A) Fornecer criptografia de Camada 2 entre switches.
- [ ] B) Identificar a qual VLAN o frame pertence quando ele trafega por uma porta de Trunk interligando dois switches.
- [ ] C) Aumentar o tamanho do MTU para suportar Jumbo Frames.
- [ ] D) Eleger o Root Bridge no Spanning Tree Protocol.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O protocolo 802.1Q insere o VLAN ID no cabeçalho do frame L2. Isso permite que um switch de destino saiba exatamente a qual rede lógica (ex: RH ou TI) aquele pacote pertence após ele atravessar o cabo de tronco (Trunk).
</details>
<br>

**4. Em uma topologia de rede com links físicos redundantes, qual protocolo impede que loops infinitos de Camada 2 (Broadcast Storms) travem a infraestrutura?**
- [ ] A) OSPF
- [ ] B) CSMA/CD
- [ ] C) STP (Spanning Tree Protocol)
- [ ] D) VTP (VLAN Trunking Protocol)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>STP (802.1D)</b> monitora a rede trocando mensagens BPDU. Ao detectar caminhos em anel (loops), ele elege um Root Bridge e coloca as portas redundantes no estado "Blocking", cortando o loop logicamente.
</details>
<br>

**5. Qual é o principal benefício de utilizar um Multilayer Switch (Layer 3) com Switch Virtual Interfaces (SVIs) em vez de um roteador tradicional usando a técnica "Router-on-a-Stick"?**
- [ ] A) Suporte nativo a conexões WAN de fibra ótica de longa distância.
- [ ] B) O Multilayer Switch não precisa de tabelas MAC.
- [ ] C) O roteamento Inter-VLAN ocorre em altíssima velocidade porque é processado por hardware dedicado (ASICs) no "backplane" do switch.
- [ ] D) As SVIs operam na Camada 4, oferecendo firewall stateful nativo.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Os ASICs (Application-Specific Integrated Circuits) no Multilayer Switch permitem que o roteamento de pacotes IP entre VLANs (via SVIs) ocorra na velocidade do cabo, eliminando o gargalo de banda do Router-on-a-stick.
</details>
<br>

**6. Se um administrador de rede digita o comando `no switchport` em uma interface GigabitEthernet de um switch Multicamadas, qual função essa porta assume?**
- [ ] A) Porta de Trunk 802.1Q.
- [ ] B) Routed Port (Porta roteada, puramente Camada 3, capaz de receber um IP direto).
- [ ] C) Porta em estado Blocking pelo STP.
- [ ] D) Access Port isolada em uma Blackhole VLAN.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O comando `no switchport` desativa o processamento de Camada 2 (MAC/VLAN/STP) na interface, transformando-a em uma <b>Routed Port</b>. Ela age exatamente como a porta de um Roteador físico convencional.
</details>
<br>

---

### 📡 Domínio 2: Wireless, Frequências e Operações 802.11

**7. Por que as redes WLAN (Wi-Fi) precisam utilizar o método de acesso CSMA/CA em vez do CSMA/CD utilizado em redes LAN cabeadas?**
- [ ] A) Porque os APs não possuem Tabela MAC.
- [ ] B) Porque as redes wireless não têm suporte a endereçamento IPv4.
- [ ] C) Porque os rádios operam em Half-Duplex e não conseguem transmitir e "escutar" colisões simultaneamente no mesmo canal.
- [ ] D) Porque o CSMA/CA oferece maior velocidade de modulação.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Em RF (Rádio Frequência), o sinal emitido é muito mais forte que o sinal recebido, "cegando" o rádio para escutar colisões simultâneas (Half-duplex). O CSMA/CA (Avoidance) contorna isso ouvindo antes e aguardando um timer aleatório para evitar a colisão prévia.
</details>
<br>

**8. No processo de CSMA/CA, como um cliente sem fio tem a certeza absoluta de que o frame que ele transmitiu não sofreu uma colisão no ar e chegou intacto ao AP?**
- [ ] A) Ele recebe uma mensagem BPDU de volta.
- [ ] B) O Access Point é obrigado a responder com um pacote de ACK (Acknowledgement).
- [ ] C) O cliente escuta o eco do próprio pacote refletido no AP.
- [ ] D) O AP envia um Probe Response.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Todo frame de dados Unicast no padrão 802.11 exige um <b>ACK</b>. Se o emissor não receber o ACK após transmitir, ele assume que houve colisão ou perda de sinal e retransmite o frame.
</details>
<br>

**9. Analisando um frame de rádio 802.11 no Wireshark, um analista nota que o cabeçalho possui até 4 campos de endereços MAC. Qual é a justificativa técnica para essa estrutura?**
- [ ] A) Para armazenar os endereços IPv4 e IPv6 simultaneamente.
- [ ] B) Para suportar a tecnologia MIMO (Múltiplas antenas).
- [ ] C) Para identificar o transmissor de rádio, o receptor de rádio, a origem original dos dados e o destino final na rede infraestruturada (cabo).
- [ ] D) Para mascarar o MAC do cliente contra ataques de sniffing.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Como o AP atua como uma ponte (Bridge) entre o ar e o cabo, o pacote precisa ter o MAC do cliente (Transmitter), o MAC do AP (Receiver), o MAC do destino final na web/cabo (Destination) e, em alguns modos, a origem além do cabo (Source).
</details>
<br>

**10. O que define o BSSID (Basic Service Set Identifier) em uma rede sem fio configurada em modo de Infraestrutura?**
- [ ] A) É o nome legível da rede que aparece no celular (ex: "Rede_Visitantes").
- [ ] B) É o endereço IP do Access Point.
- [ ] C) É o endereço físico (MAC Address) do rádio do Access Point.
- [ ] D) É a senha criptográfica (PSK) usada para acessar o Wi-Fi.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>BSSID</b> é o MAC Address do AP. Ele serve como o identificador único daquela célula específica de rádio. O nome legível que aparece no celular é o <b>SSID</b>.
</details>
<br>

**11. Uma empresa instalou 5 Access Points no mesmo andar, conectados ao mesmo sistema de distribuição e divulgando o mesmo SSID ("Corp_WIFI"). Qual arquitetura sem fio isso representa?**
- [ ] A) Ad-Hoc Mode
- [ ] B) IBSS (Independent Basic Service Set)
- [ ] C) ESS (Extended Service Set)
- [ ] D) Personal Hotspot (Tethering)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Um <b>ESS</b> é criado quando agrupamos múltiplos BSSs (múltiplos APs) através de uma rede cabeada, divulgando o mesmo SSID para permitir que o usuário ande pelo prédio (roaming) sem perder a conexão de rede.
</details>
<br>

**12. Em qual modo de descoberta (Discover Mode) o cliente Wireless, sem conhecer as redes ao redor, envia de forma ativa um frame chamado "Probe Request" procurando por redes disponíveis?**
- [ ] A) Descoberta Passiva (Passive Discover)
- [ ] B) Descoberta Ativa (Active Discover)
- [ ] C) CSMA/CD
- [ ] D) Broadcast Storming

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Na <b>Descoberta Ativa</b>, é o cliente quem toma a iniciativa enviando um Probe Request. O AP escuta esse request e, se for compatível, responde com um Probe Response.
</details>
<br>

**13. Quando você ativa a rede Wi-Fi do seu celular em um aeroporto, ele imediatamente lista diversas redes, como "FREE_AIRPORT_WIFI", sem que seu celular tenha transmitido nada. Qual frame o AP do aeroporto está utilizando para esse anúncio?**
- [ ] A) Probe Request
- [ ] B) Authentication Frame
- [ ] C) Beacon Frame
- [ ] D) Association Request

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Esse é o modo de Descoberta Passiva. O Access Point transmite quadros <b>Beacon</b> periodicamente (geralmente a cada 100ms) anunciando o SSID, velocidades suportadas e requisitos de segurança para todos os ouvintes na área.
</details>
<br>

**14. Quais são as três etapas sequenciais obrigatórias para que um cliente wireless se conecte com sucesso a um Access Point e comece a enviar dados para a rede IP?**
- [ ] A) DHCP, DNS, HTTP
- [ ] B) Descobrir (Discover), Autenticar (Authenticate), Associar (Associate).
- [ ] C) Routing, Switching, Flooding.
- [ ] D) RTS, CTS, ACK.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O cliente deve primeiro <b>descobrir</b> o AP (via Beacon ou Probe), em seguida, deve se <b>autenticar</b> (troca de credenciais 802.11/WPA) e, finalmente, solicitar a <b>associação</b> lógica para que o AP passe a fazer a ponte dos seus dados para o cabo.
</details>
<br>

**15. O que ocorre com os Endereços MAC em uma comunicação Ad-Hoc onde dois notebooks se conectam via Wi-Fi sem a presença de um roteador ou Access Point?**
- [ ] A) O Address 3 é usado como Gateway Padrão.
- [ ] B) O formato de 4 endereços é ignorado e o frame utiliza essencialmente apenas os endereços de Transmissor e Receptor (ponto a ponto).
- [ ] C) O BSSID passa a ser gerado por um servidor DHCP externo.
- [ ] D) A criptografia WPA3 é desativada compulsoriamente.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Em uma rede <b>Ad-Hoc</b> (também chamada de IBSS), não existe um Access Point central fazendo a ponte para uma rede de distribuição (DS). Portanto, a complexidade dos 4 endereços MAC não é necessária, pois a comunicação é estritamente direta entre os dois rádios (Peer-to-Peer).
</details>