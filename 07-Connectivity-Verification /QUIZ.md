# 🧠 Simulado Definitivo: Module 07 (Connectivity Verification)

Este simulado foca nos mecanismos do ICMP, resolução de vizinhos e ferramentas vitais de diagnóstico, alinhado aos cenários que você encontrará na certificação **Cisco CBROPS 200-201**.

---

### 🌐 Domínio 1: Protocolo IP e Decisões de Roteamento (L3)

**1. Uma das características operacionais do protocolo IP é ser "Connectionless" (Sem conexão). Qual afirmação descreve corretamente essa característica em relação à transmissão de dados?**
a) O IP assegura que os pacotes cheguem na mesma ordem em que foram enviados.
b) O IP exige uma troca inicial de mensagens de controle (Handshake) antes de enviar o payload.
c) O IP envia pacotes ao destinatário sem notificá-lo previamente, assim como enviar uma carta tradicional pelo correio.
d) O IP retransmite automaticamente qualquer pacote que não receba um aviso de recebimento.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) O IP envia pacotes ao destinatário sem notificá-lo previamente, assim como enviar uma carta tradicional pelo correio.
**Explicação:** Ser "Connectionless" significa que não há criação de um canal dedicado de ponta a ponta antes da transmissão. O remetente apenas injeta o pacote na rede. Quem garante ordem e retransmissões (Handshake) é o TCP, não o IP.
</details>

<br>

**2. O protocolo IP opera sob o princípio de "Best Effort" (Melhor Esforço). No contexto da Camada de Rede (L3), o que isso significa na prática?**
a) O protocolo tenta enviar os dados pelo meio mais rápido disponível (fibra óptica em vez de cobre).
b) O IP não garante que todos os pacotes enviados serão recebidos; ele não possui rastreamento de entrega ou recuperação.
c) O IP calculará a rota de menor custo matemático em cada roteador antes de encaminhar o tráfego.
d) O IP ajustará automaticamente o tamanho do cabeçalho para evitar a fragmentação.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) O IP não garante que todos os pacotes enviados serão recebidos; ele não possui rastreamento de entrega ou recuperação.
**Explicação:** "Best Effort" é sinônimo de "não confiável" no jargão de redes. O IP faz o possível para encaminhar o pacote, mas não fornece aviso de recebimento. Se houver congestionamento, pacotes podem ser descartados sem aviso.
</details>

<br>

**3. A característica do IPv4 e IPv6 de ser "Media Independent" (Independente do Meio) significa que o pacote IP:**
a) É imune a interferências eletromagnéticas (EMI) geradas pelo cabeamento.
b) Pode conter qualquer tipo de dados de aplicação, como HTTP, FTP ou SMTP.
c) Não sofre modificações em sua estrutura lógica interna, quer viaje por um cabo de cobre, fibra óptica ou sinal Wi-Fi.
d) Ajusta seu tamanho de MTU de forma autônoma para evitar fragmentação no caminho.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Não sofre modificações em sua estrutura lógica interna, quer viaje por um cabo de cobre, fibra óptica ou sinal Wi-Fi.
**Explicação:** A Camada de Rede (IP) opera em nível lógico e não se "importa" com as leis da física da Camada 1. O pacote IP permanece idêntico durante toda a viagem; apenas o quadro Ethernet (L2) muda de tecnologia a cada salto.
</details>

<br>

**4. Um desenvolvedor utiliza o endereço IP `127.0.0.1` no seu código fonte. Ao gerar pacotes com este endereço de destino, o que acontece ao fluxo de rede do computador?**
a) O pacote é roteado para a internet, mas bloqueado no ISP do provedor.
b) O pacote desce a pilha TCP/IP até a placa de rede e volta para o próprio sistema operativo, sem nunca entrar no cabo de rede físico.
c) O pacote é transmitido via cabo e retorna ao PC pelo switch local.
d) O pacote dispara um Broadcast de descoberta para todos os hosts da mesma sub-rede.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) O pacote desce a pilha TCP/IP até a placa de rede e volta para o próprio sistema operativo, sem nunca entrar no cabo de rede físico.
**Explicação:** Os endereços do bloco `127.0.0.0/8` (ou `::1` em IPv6) são interfaces de Loopback. Servem para testes internos e garantem que a arquitetura de rede do sistema operativo local está funcional.
</details>

<br>

**5. Um Host final executa uma operação matemática de *Logical AND* entre o IP de destino e a sua própria Máscara de Sub-rede antes de enviar o tráfego. Se o resultado revelar que o destino NÃO está na rede local, para onde o Host enviará o quadro (Frame) na Camada 2?**
a) Para o endereço MAC de Loopback (127.0.0.1).
b) Para o endereço MAC de Broadcast (`FF:FF:FF:FF:FF:FF`).
c) Diretamente para o endereço MAC do dispositivo de destino usando ARP.
d) Para o endereço MAC do seu Default Gateway (Roteador Padrão).

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) Para o endereço MAC do seu Default Gateway (Roteador Padrão).

**Explicação:** Quando o cálculo AND indica um "Remote Host" (outra rede), o computador confia no seu roteador (Default Gateway) para encontrar o caminho, endereçando o MAC do quadro para a porta local do roteador.
</details>

<br>

---

### 📦 Domínio 2: Cabeçalhos IPv4 e Campos de Controle

**6. Durante uma investigação no Wireshark, um analista observa um tráfego de rede e inspeciona o cabeçalho IPv4. O campo "Protocol" possui o valor decimal `6`. Qual protocolo da camada superior está contido no payload deste pacote IP?**
a) ICMP
b) UDP
c) TCP
d) IPv6

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) TCP
**Explicação:** O campo Protocol (8 bits) informa ao roteador e ao receptor quem deve tratar os dados. `6` é TCP, `17` é UDP e `1` é ICMP.
</details>

<br>

**7. Qual campo dentro do cabeçalho de um pacote IPv4 sofre decrementação (redução) obrigatória toda vez que o pacote é processado e repassado por um roteador de Camada 3?**
a) Header Checksum
b) Differentiated Services (DS)
c) Fragment Offset
d) Time to Live (TTL)

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) Time to Live (TTL)

**Explicação:** O TTL é o mecanismo anti-loop da internet. Cada roteador subtrai 1. Se chegar a 0, o pacote é destruído e um erro ICMP "Time Exceeded" é enviado. O *Header Checksum* também é modificado porque precisa de ser recalcular após a alteração do TTL.
</details>

<br>

**8. Qual campo do pacote IPv4 substituiu o antigo *Type of Service (ToS)* e é hoje utilizado ativamente para a priorização de pacotes (Quality of Service - QoS) durante congestionamentos?**
a) DiffServ (Differentiated Services)
b) IHL (Internet Header Length)
c) Header Checksum
d) ECN (Explicit Congestion Notification)

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** a) DiffServ (Differentiated Services)
**Explicação:** O campo DS (8 bits) contém o DSCP para classificar o tráfego (garantindo que pacotes de VoIP não fiquem presos atrás de downloads pesados) e o ECN para notificar sobre congestionamentos iminentes.
</details>

<br>

---

### 🔗 Domínio 3: Subcamadas Ethernet e Endereçamento (L2)

**9. A Camada de Enlace de Dados (Layer 2) sob o padrão IEEE 802 é dividida em duas subcamadas distintas. Qual delas atua como a "ponte de software" que comunica diretamente com os protocolos de Camada 3 (IPv4/IPv6)?**
a) MAC (Media Access Control)
b) LLC (Logical Link Control)
c) FCS (Frame Check Sequence)
d) CSMA/CD

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) LLC (Logical Link Control)
**Explicação:** A subcamada LLC (802.2) identifica qual protocolo de rede está a ser usado e faz a ponte lógica com o sistema operativo. A subcamada inferior, MAC (802.3), lida fisicamente com a placa de rede e a formatação do meio físico.
</details>

<br>

**10. O endereço MAC é o identificador físico de um dispositivo. Qual alternativa descreve com precisão a estrutura e o formato padrão de um MAC Address Ethernet?**
a) Um valor binário de 32 bits, expresso em formato decimal pontuado.
b) Um valor binário de 64 bits, expresso em oito grupos hexadecimais.
c) Um valor binário de 48 bits, expresso por 12 dígitos hexadecimais.
d) Um valor alfanumérico de 128 bits atribuído pelo ISP.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Um valor binário de 48 bits, expresso por 12 dígitos hexadecimais.
**Explicação:** Os endereços MAC (ex: `00:1A:2B:3C:4D:5E`) têm 48 bits de comprimento. Para leitura humana, os bits são agrupados e convertidos em 12 caracteres hexadecimais.
</details>

<br>

**11. No cabeçalho de um quadro Ethernet, o campo `Type / Length` (EtherType) é crucial para o desencapsulamento. Se este campo apresentar o valor hexadecimal `0x86DD`, o que o sistema receptor espera encontrar no payload?**
a) Um pacote IPv4.
b) Um pacote IPv6.
c) Uma solicitação ARP (Address Resolution Protocol).
d) Uma mensagem de erro ICMP.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Um pacote IPv6.
**Explicação:** O EtherType é como uma etiqueta de correio. `0x0800` sinaliza que dentro do envelope há um pacote IPv4, `0x0806` sinaliza ARP, e `0x86DD` sinaliza IPv6.
</details>

<br>

---

### 🛡️ Domínio 4: O Quadro Ethernet (Frame) e Integridade

**12. Num analisador de rede, um analista depara-se com um quadro Ethernet cujo tamanho total (do MAC de destino até ao FCS) é de apenas 52 bytes. Como o hardware receptor tratará este quadro?**
a) Solicitará ao switch que adicione 12 bytes de Padding.
b) Tratá-lo-á como um "Runt Frame" (ou Fragmento de Colisão) e descartá-lo-á automaticamente.
c) Processá-lo-á normalmente se for um pacote ICMP.
d) Repassá-lo-á para o Default Gateway para análise.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Tratá-lo-á como um "Runt Frame" (ou Fragmento de Colisão) e descartá-lo-á automaticamente.

**Explicação:** O limite mínimo inegociável da Ethernet é 64 bytes. Menos do que isso é fisicamente impossível num frame válido, pelo que as placas de rede descartam silenciosamente como lixo/colisão.
</details>

<br>

**13. Qual componente de um quadro Ethernet não contém dados úteis, mas tem a função crítica de sincronizar os relógios físicos dos emissores e recetores avisando que um novo quadro está a chegar?**
a) FCS (Frame Check Sequence)
b) Type / Length
c) Preamble e Start Frame Delimiter (SFD)
d) Endereço MAC de Broadcast

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** c) Preamble e Start Frame Delimiter (SFD)
**Explicação:** São os primeiros 8 bytes (7 de Preamble + 1 de SFD) transmitidos. Atuam como um alarme que estabiliza o pulso elétrico na placa de rede recetora antes da leitura do MAC de Destino.
</details>

<br>

**14. Para que um quadro alcance os 64 bytes exigidos, o campo "Data" deve ter no mínimo 46 bytes. Se o Pacote IP encapsulado tiver apenas 20 bytes, qual ação é executada pela Camada de Enlace (MAC)?**
a) A Camada de Enlace bloqueia o pacote e pede mais dados à Aplicação.
b) O quadro é transmitido incompleto e remontado mais tarde.
c) O switch converte o quadro num "Jumbo Frame".
d) Injetam-se bits sem significado (Padding) no final do payload até atingir os 46 bytes mínimos de dados.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** d) Injetam-se bits sem significado (Padding) no final do payload até atingir os 46 bytes mínimos de dados.
**Explicação:** O *Padding* é um "enchimento" artificial adicionado aos pacotes pequenos. Sem ele, pacotes muito pequenos não ativariam corretamente a detecção de colisões (CSMA/CD) em redes locais físicas.
</details>

<br>

**15. Qual é a responsabilidade do Frame Check Sequence (FCS) presente no final de cada quadro Ethernet (Trailer)?**
a) Executar criptografia para ocultar os dados em redes Wi-Fi.
b) Utilizar um cálculo de Redundância Cíclica (CRC) sobre todo o quadro para garantir que os bits transmitidos não foram corrompidos física ou magneticamente no caminho.
c) Notificar o PC emissor sobre perda de pacotes.
d) Auditar exclusivamente os cabeçalhos IPv4 e TCP do payload.

<details>
<summary><b>✅ Ver Resposta e Explicação</b></summary>

**Resposta Correta:** b) Utilizar um cálculo de Redundância Cíclica (CRC) sobre todo o quadro para garantir que os bits transmitidos não foram corrompidos física ou magneticamente no caminho.
**Explicação:** O FCS garante a integridade nó-a-nó. O emissor faz a conta matemática (CRC) e envia o resultado no FCS. O receptor faz a mesma conta; se não bater, o cabo ou o switch corromperam o dado, e o quadro é descartado.
</details>

<br>

