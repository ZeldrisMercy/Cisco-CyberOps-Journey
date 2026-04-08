# 📁 Module 11: Network Devices & Wireless Communications

> [!NOTE]
> **Resumo Executivo Expandido:** Este módulo detalha a infraestrutura crítica de redes corporativas. Na seção cabeada, dissecamos a inteligência dos **Switches** (construção da tabela MAC), a prevenção de loops via **STP**, a segmentação via **VLANs** e o roteamento em hardware dos **Multilayer Switches**. Na seção Wireless, exploramos as limitações do meio aéreo, o gerenciamento de colisões via **CSMA/CA**, a estrutura complexa do **Frame 802.11** e o passo a passo da associação de clientes aos Access Points.

---

## 🏗️ 11.1 Dispositivos de Rede, Comutação e Roteamento

A jornada de um dado de ponta a ponta exige equipamentos que tomem decisões precisas em diferentes camadas do Modelo OSI.

### 11.1.5 O Processo de Encaminhamento (End-to-End Forwarding)
A regra fundamental do tráfego roteado (saltos entre redes diferentes):
* **Camada 3 (IP de Origem e Destino):** Permanecem **imutáveis** durante todo o trajeto (exceto se houver NAT). Eles indicam o remetente original e o destinatário final.
* **Camada 2 (MAC de Origem e Destino):** São **descartados e recriados** a cada salto (roteador). O roteador lê o IP destino, consulta sua *Routing Table* e cria um novo Frame L2 endereçado ao MAC do próximo salto.

### 11.1.10 Operação de Switching (A Inteligência da Camada 2)
Diferente de um Hub (que é burro e cego), o Switch aprende a topologia da rede dinamicamente construindo sua **Tabela MAC (ou Tabela CAM)** na memória RAM:
1. **Aprendizado (Learning - Origem):** Quando um frame entra em uma porta, o switch lê o **MAC de Origem**. Se esse MAC não estiver na tabela, ele o adiciona e associa à porta de entrada (com um timer de envelhecimento, geralmente 300 segundos).
2. **Encaminhamento (Forwarding - Destino):** O switch lê o **MAC de Destino**. Se o MAC constar na tabela, ele encaminha o frame *apenas* para a porta específica (Unicast).
3. **Inundação (Flooding - Unknown Unicast):** Se o MAC de destino *não* estiver na tabela (ou se for um Broadcast `FF:FF:FF:FF:FF:FF`), o switch inunda o frame para **todas as portas**, exceto a porta por onde o frame entrou.

### 11.1.12 & 11.1.13 VLANs e STP (Spanning Tree Protocol)
* **VLANs (IEEE 802.1Q):** Segmentação lógica de Broadcast Domains. Um switch físico é dividido em vários switches lógicos. Para pacotes trafegarem entre switches diferentes mantendo a separação, usa-se portas de **Trunk**, onde o switch injeta uma *Tag* de 4 bytes contendo o VLAN ID.
* **STP (IEEE 802.1D):** O protocolo salva-vidas da Camada 2. Ele impede **Broadcast Storms** em redes com loops físicos (cabos redundantes).
  * Os switches trocam mensagens **BPDU**.
  * Elegem um **Root Bridge** (O Rei da rede, com o menor Bridge ID).
  * Calculam o melhor caminho e colocam as portas redundantes em estado de **Blocking** (bloqueio lógico, não passam dados, apenas escutam BPDUs).

### 11.1.14 Multilayer Switching (Switches Layer 3)
Equipamentos com chips dedicados (**ASICs**) que unem a velocidade de switching com a inteligência de roteamento.
* **SVI (Switch Virtual Interface):** O método moderno de roteamento Inter-VLAN. É uma interface lógica (`interface vlan 10`) que atua como Default Gateway ultra-rápido para os dispositivos daquela VLAN.
* **Routed Port:** Uma porta física configurada com `no switchport`, perdendo recursos L2 (como STP e VLAN) para receber um IP direto e ligar o switch ao roteador de borda.

---

## 📡 11.2 Comunicações Sem Fio (Wireless)

Redes locais sem fio (WLANs) operam em um meio não guiado (RF), sendo suscetíveis a interferências e operando nativamente em **Half-Duplex** (não podem transmitir e receber simultaneamente).

### 11.2.4 CSMA/CA (A Prevenção de Colisões)
Ao contrário do Ethernet cabeado (CSMA/CD) que detecta a colisão pelo cabo, o Wi-Fi **evita** a colisão:
1. **Listen:** O cliente ouve o canal.
2. **Backoff Timer:** Se livre, ele aguarda um tempo aleatório para evitar que vários dispositivos falem no mesmo milissegundo.
3. **Transmit:** Envia o dado.
4. **ACK:** Todo frame unicast 802.11 exige um *Acknowledgement* do AP. Se o AP não responder, o cliente assume que houve colisão e retransmite.

### 11.2.3 Estrutura do Frame 802.11
Devido à presença do Access Point como intermediário, o cabeçalho wireless é maior e mais complexo, possuindo até **4 campos de endereço MAC**:
1. `Address 1`: Receiver Address (MAC de quem recebe o rádio - ex: AP).
2. `Address 2`: Transmitter Address (MAC de quem emitiu o rádio - ex: Smartphone).
3. `Address 3`: Destination Address (Destino final na rede cabeada).
4. `Address 4`: Source Address (Usado geralmente em conexões ponta a ponta entre APs, como WDS).

### 11.2.5 & 11.2.6 Descoberta, Associação e Estruturas
A topologia Wi-Fi se divide em:
* **BSS (Basic Service Set):** Uma célula de cobertura com um AP. O identificador único dessa célula é o **BSSID** (o MAC Address físico do rádio do AP).
* **ESS (Extended Service Set):** Múltiplos BSSs interligados pelo mesmo Switch (Distribution System), compartilhando o mesmo SSID para permitir o *Roaming*.

O processo de conexão do cliente possui etapas rígidas:
1. **Discovery (Descoberta):**
   * **Passiva:** O AP faz broadcast da rede enviando quadros **Beacon** (contendo SSID, criptografia, etc.). O cliente escuta.
   * **Ativa:** O cliente envia ativamente um **Probe Request** procurando um SSID específico. O AP responde com um **Probe Response**.
2. **Authentication:** Troca de chaves (Open, WPA2, WPA3).
3. **Association:** O cliente pede para entrar no BSS, e o AP registra o MAC do cliente, liberando o trânsito de dados para a rede cabeada.