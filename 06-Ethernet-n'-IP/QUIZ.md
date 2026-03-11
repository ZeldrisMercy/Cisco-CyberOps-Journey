# 🧠 Simulado Definitivo: Module 06 (Ethernet & IP)

Este simulado contém 15 questões de nível de certificação (CBROPS/CCNA), testando a sua compreensão sobre encapsulamento de Camada 2/Camada 3, campos de cabeçalhos, regras da Ethernet e manipulação de tráfego.

---

**1. Durante uma investigação de segurança, um analista de SOC observa um tráfego de rede incomum. Ao inspecionar o cabeçalho IPv4 dos pacotes capturados, ele nota que o campo "Protocol" possui o valor decimal `6`. Qual protocolo da camada superior está contido no payload deste pacote IP?**
- [ ] A) ICMP
- [ ] B) UDP
- [ ] C) TCP
- [ ] D) IPv6

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O campo Protocol no IPv4 (8 bits) identifica o protocolo transportado. O valor <code>6</code> corresponde ao TCP (Transmission Control Protocol), <code>17</code> corresponde ao UDP e <code>1</code> corresponde ao ICMP.
</details>
<br>

**2. A Camada de Enlace de Dados (Layer 2) sob o padrão IEEE 802 é dividida em duas subcamadas distintas. Qual subcamada atua como a interface baseada em software que se comunica diretamente com o protocolo IPv4 na Camada de Rede?**
- [ ] A) MAC (Media Access Control)
- [ ] B) LLC (Logical Link Control)
- [ ] C) FCS (Frame Check Sequence)
- [ ] D) CSMA/CD

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A subcamada LLC (802.2) faz a ponte entre o software de rede (protocolos IP) e o hardware. A subcamada MAC (802.3) interage fisicamente com a placa de rede (NIC) e o meio físico.
</details>
<br>

**3. Uma das características operacionais do protocolo IP é ser "Connectionless" (Sem conexão). Qual afirmação descreve corretamente essa característica em relação à transmissão de dados?**
- [ ] A) O IP assegura que os pacotes cheguem na mesma ordem em que foram enviados.
- [ ] B) O IP exige uma troca inicial de mensagens de controle (Handshake) antes de enviar o payload.
- [ ] C) O IP envia pacotes ao destinatário sem notificá-lo previamente, assim como enviar uma carta tradicional pelo correio.
- [ ] D) O IP retransmite automaticamente qualquer pacote que não receba um aviso de recebimento.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Ser "Connectionless" significa que não há criação de um canal dedicado antes da transmissão. O remetente apenas injeta o pacote na rede. Quem garante ordem e retransmissões (Handshake) é o TCP, não o IP.
</details>
<br>

**4. Ao analisar um frame Ethernet em um analisador de protocolos (como o Wireshark), um analista percebe que o tamanho total do quadro (do MAC de destino até o FCS) é de apenas 52 bytes. Como o dispositivo receptor em uma rede Ethernet padrão tratará este quadro?**
- [ ] A) Ele solicitará ao switch que adicione 12 bytes de Padding.
- [ ] B) Ele o tratará como um "Runt Frame" ou "Collision Fragment" e o descartará automaticamente.
- [ ] C) Ele processará o quadro normalmente, pois o payload ICMP é pequeno.
- [ ] D) Ele repassará o quadro para o Default Gateway.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O tamanho mínimo absoluto de um frame Ethernet padrão é 64 bytes. Qualquer frame menor que isso é considerado inválido (geralmente resultado de uma colisão de rede) e é destruído silenciosamente pelo hardware receptor.
</details>
<br>

**5. Qual campo dentro do cabeçalho de um pacote IPv4 sofre decrementação (redução) obrigatória toda vez que o pacote é processado e repassado por um roteador de Camada 3?**
- [ ] A) Header Checksum
- [ ] B) Differentiated Services (DS)
- [ ] C) Fragment Offset
- [ ] D) Time to Live (TTL)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> O TTL (Time to Live) é o mecanismo anti-loop da internet. Cada roteador subtrai 1 desse campo. Se o TTL chegar a zero antes de atingir o destino, o pacote é morto e um erro ICMP é gerado. (Vale notar que o Header Checksum também muda, pois deve ser recalculado devido à alteração do TTL).
</details>
<br>

**6. Em um quadro Ethernet, o campo `Type / Length` (também chamado de EtherType) é vital para o desencapsulamento. Se este campo apresentar o valor hexadecimal `0x86DD`, o que o sistema operacional receptor deve esperar encontrar no payload de dados?**
- [ ] A) Um pacote IPv4.
- [ ] B) Um pacote IPv6.
- [ ] C) Uma solicitação ARP (Address Resolution Protocol).
- [ ] D) Uma mensagem de erro ICMP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O EtherType indica a natureza do payload de Camada 3. O valor <code>0x0800</code> sinaliza IPv4, enquanto o valor <code>0x86DD</code> sinaliza IPv6.
</details>
<br>

**7. O endereço MAC é o identificador físico de um dispositivo na rede. Qual alternativa descreve com precisão a estrutura e o formato padrão de um MAC Address Ethernet?**
- [ ] A) Um valor binário de 32 bits, expresso em formato decimal pontuado.
- [ ] B) Um valor binário de 64 bits, expresso em oito grupos hexadecimais.
- [ ] C) Um valor binário de 48 bits, expresso por 12 dígitos hexadecimais.
- [ ] D) Um valor alfanumérico de 128 bits atribuído pelo ISP.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O endereço MAC possui 48 bits. Para ser legível por humanos, esses 48 bits são agrupados de 4 em 4, formando 12 caracteres em base hexadecimal (variando de 0 a 9 e A a F).
</details>
<br>

**8. O protocolo IP opera sob o princípio de "Best Effort" (Melhor Esforço). No contexto da Camada de Rede (L3), o que isso significa na prática?**
- [ ] A) O protocolo tenta enviar os dados pelo meio mais rápido disponível (fibra óptica em vez de cobre).
- [ ] B) O IP não garante que todos os pacotes enviados serão recebidos; ele não possui rastreamento de entrega.
- [ ] C) O IP calculará a rota de menor custo matemático em cada roteador antes de encaminhar o tráfego.
- [ ] D) O IP ajustará automaticamente o tamanho do cabeçalho para evitar a fragmentação.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> "Best Effort" é sinônimo de "não confiável" no jargão de redes. O IP faz o possível para encaminhar o pacote para o próximo roteador, mas não fornece aviso de recebimento ou mecanismos para recuperar pacotes perdidos em trânsito.
</details>
<br>

**9. Um computador final (Host) executa uma operação de *Logical AND* entre o endereço IP de destino e a sua própria Máscara de Sub-rede antes de despachar o tráfego. Se o resultado dessa matemática NÃO coincidir com a sua própria rede local, para onde o Host enviará o pacote na Camada 2?**
- [ ] A) Para o endereço MAC de Loopback (127.0.0.1).
- [ ] B) Para o endereço MAC de Broadcast (`FF:FF:FF:FF:FF:FF`).
- [ ] C) Diretamente para o endereço MAC do dispositivo de destino usando ARP.
- [ ] D) Para o endereço MAC do Default Gateway (Roteador Padrão).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> Quando o AND matemático diz que o destino é um "Remote Host" (está em outra rua/cidade), o PC empacota os dados e envia o frame Ethernet para o roteador local (Default Gateway), que fará o transporte inter-redes.
</details>
<br>

**10. Qual componente de um quadro Ethernet tem a responsabilidade principal de sinalizar aos nós receptores que um novo quadro está prestes a chegar e permitir a sincronização do sinal?**
- [ ] A) FCS (Frame Check Sequence)
- [ ] B) Type / Length
- [ ] C) Preamble e Start Frame Delimiter (SFD)
- [ ] D) Differentiated Services (DS)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O Preâmbulo (7 bytes) seguido do SFD (1 byte) formam uma sequência repetitiva de 1s e 0s que atuam como um "despertador" para os circuitos de hardware das placas de rede se sincronizarem eletricamente antes de ler o MAC de destino.
</details>
<br>

**11. Qual campo do pacote IPv4 substituiu o antigo Type of Service (ToS) e é composto por 8 bits utilizados ativamente hoje em dia para priorização de pacotes (Quality of Service - QoS) durante o congestionamento de rede?**
- [ ] A) DiffServ (Differentiated Services)
- [ ] B) IHL (Internet Header Length)
- [ ] C) Header Checksum
- [ ] D) ECN (Explicit Congestion Notification)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> O campo Differentiated Services (DS ou DiffServ) contém 8 bits: os 6 primeiros são o DSCP (Differentiated Services Code Point) para classificar o tráfego (ex: voz tem alta prioridade), e os 2 últimos são para o ECN.
</details>
<br>

**12. Em um quadro Ethernet válido, o campo "Data" deve ter no mínimo 46 bytes para que o quadro alcance os 64 bytes totais exigidos. Se o Pacote IP gerado pela camada superior tiver apenas 20 bytes de tamanho, qual ação é tomada pela Camada de Enlace?**
- [ ] A) A Camada de Enlace pede à Camada de Transporte que aguarde mais dados da Aplicação.
- [ ] B) O switch preenche o espaço enviando o quadro em formato Jumbo.
- [ ] C) A subcamada MAC injeta bits sem sentido (Padding) até que o campo Data atinja 46 bytes.
- [ ] D) O quadro é transmitido como um "Collision Fragment" e remontado pelo receptor.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O *Padding* (preenchimento) é usado para engordar artificialmente pacotes minúsculos para que o frame atenda à lei da física Ethernet de 64 bytes mínimos, permitindo que a detecção de colisões (CSMA/CD) funcione corretamente em cabos metálicos curtos.
</details>
<br>

**13. Um desenvolvedor utiliza o endereço IP `127.0.0.1` em seu código fonte. Ao gerar pacotes com este endereço de destino, o que acontece no fluxo de rede do computador?**
- [ ] A) O pacote é roteado para a internet, mas bloqueado no ISP do provedor.
- [ ] B) O pacote desce a pilha TCP/IP até a placa de rede e volta para o próprio sistema operacional, sem nunca entrar no cabo de rede físico.
- [ ] C) O pacote é transmitido via cabo e retorna ao PC pelo switch local.
- [ ] D) O pacote dispara um Broadcast de descoberta para todos os hosts da mesma sub-rede.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Os endereços do bloco <code>127.0.0.0/8</code> são interfaces de Loopback (teste). Eles são usados para comunicação Inter-Process Communication (IPC) interna ou para testar se a arquitetura de rede do sistema operacional local está saudável.
</details>
<br>

**14. A característica do IPv4 e IPv6 de ser "Media Independent" significa que o pacote IP:**
- [ ] A) É imune a interferências eletromagnéticas (EMI) geradas pelo cabeamento.
- [ ] B) Pode conter qualquer tipo de dados de aplicação, como HTTP, FTP ou SMTP.
- [ ] C) Não sofre modificações em sua estrutura lógica, não importando se viaja por um cabo de par trançado (Cobre) ou enlace de rádio (Wi-Fi).
- [ ] D) Ajusta seu tamanho de MTU de forma autônoma para evitar fragmentação no caminho.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A Camada de Rede (IP) opera em nível lógico e não se "importa" com as leis da física da Camada 1. O pacote IP é idêntico se você está conectado via cabo de fibra óptica, cabo UTP, serial ou antena Wi-Fi. Apenas o quadro L2 muda de tecnologia.
</details>
<br>

**15. Qual é o papel exclusivo do Frame Check Sequence (FCS) presente na extremidade de encerramento (trailer) de um quadro Ethernet?**
- [ ] A) Executar a criptografia AES no payload do pacote para garantir confidencialidade.
- [ ] B) Usar um cálculo de Redundância Cíclica (CRC) sobre o frame para garantir que os bits transmitidos não foram corrompidos no meio físico.
- [ ] C) Notificar o roteador de origem sobre perda de pacotes para forçar a retransmissão.
- [ ] D) Verificar a integridade exclusiva dos cabeçalhos IPv4 e TCP, ignorando o payload.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O FCS fica na extremidade do quadro e usa o cálculo CRC para garantir a integridade completa dos dados em Nível L2 (Camada Física/Enlace). É uma checagem local nó-a-nó, diferentemente do Header Checksum do IP (L3) ou do checksum do TCP (L4).
</details>
