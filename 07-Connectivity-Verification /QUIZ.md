# 🧠 Simulado Definitivo: Module 07 (Connectivity Verification)

Este simulado foca nos mecanismos do ICMP, resolução de vizinhos e ferramentas vitais de diagnóstico, alinhado aos cenários que você encontrará na certificação **Cisco CBROPS 200-201**.

---

**1. Em redes IPv4, o ARP é utilizado para resolver endereços IP em endereços MAC físicos. Como o IPv6 não suporta broadcasts e não utiliza o ARP, qual mensagem do ICMPv6 cumpre exatamente o papel de um "ARP Request"?**
- [ ] A) Router Solicitation (RS)
- [ ] B) Neighbor Solicitation (NS)
- [ ] C) Neighbor Advertisement (NA)
- [ ] D) Router Advertisement (RA)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A mensagem Neighbor Solicitation (NS) é enviada por um dispositivo que conhece o IPv6 do alvo, mas precisa descobrir o MAC address associado, funcionando da mesma forma que o ARP Request no IPv4.
</details>
<br>

**2. Um analista está diagnosticando um servidor recém-conectado a uma rede IPv6 SLAAC. Antes do servidor atribuir a si mesmo um endereço IPv6 Unicast Global, ele executa o mecanismo DAD (Duplicate Address Detection). Como o DAD verifica se o IP já está em uso?**
- [ ] A) O servidor envia um ping (Echo Request) para o servidor DHCPv6.
- [ ] B) O servidor envia uma mensagem Neighbor Solicitation (NS) contendo o seu próprio endereço IPv6 pretendido como alvo. Se receber um Neighbor Advertisement (NA), significa que o endereço é duplicado e já está em uso.
- [ ] C) O servidor consulta a tabela de roteamento interna do Roteador Padrão (Default Gateway).
- [ ] D) O servidor tenta acessar um DNS reverso; se falhar, o IP é seguro.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O processo DAD (Duplicate Address Detection) envia uma mensagem NS para o endereço que o host quer utilizar. Se outro equipamento na rede já possuir esse endereço IP, ele responderá imediatamente com um NA, alertando sobre a duplicidade.
</details>
<br>

**3. Uma tática comum de Troubleshooting operacional, conforme visto no módulo de conectividade, é realizar um ping no endereço "Loopback". Qual é o endereço IP de loopback padrão para as pilhas IPv4 e IPv6, respectivamente, e o que este teste verifica?**
- [ ] A) 10.0.0.1 e fe80::1 / Verifica o Gateway Padrão.
- [ ] B) 127.0.0.1 e ::1 / Verifica se o hardware da placa de rede e a pilha TCP/IP interna estão funcionando corretamente no próprio host.
- [ ] C) 0.0.0.0 e ::0 / Verifica a rota padrão da rede externa.
- [ ] D) 255.255.255.255 e FF02::1 / Verifica todos os hosts na rede local.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O ping para a interface de loopback (127.0.0.1 em IPv4 e ::1 em IPv6) não sai fisicamente da máquina. Ele apenas sobe e desce a pilha de protocolos TCP/IP do sistema operacional para garantir que os drivers e configurações lógicas vitais não estejam corrompidos.
</details>
<br>

**4. Em um ambiente IPv6, qual dispositivo gera mensagens Router Advertisement (RA) a cada 200 segundos e qual a sua principal função em uma rede SLAAC?**
- [ ] A) Switches L2; para evitar loops de rede.
- [ ] B) Servidores DNS; para fornecer resolução de nomes.
- [ ] C) Roteadores IPv6; para fornecer o prefixo de rede e permitir que os hosts configurem automaticamente os seus endereços IP e gateway.
- [ ] D) Firewalls; para transmitir a lista de Controle de Acesso (ACL) atualizada.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> As mensagens RA são fundamentais para o IPv6 SLAAC (Stateless Address Autoconfiguration). Os roteadores enviam RAs periodicamente ou em resposta a um RS, fornecendo aos hosts a estrutura da rede para que eles próprios gerem seus IPs e configurem a saída da rede.
</details>
<br>

**5. Um pacote ICMP atinge um roteador, mas o valor do campo TTL (no IPv4) ou do campo Hop Limit (no IPv6) chega a zero antes de o pacote alcançar seu destino final. O que o roteador fará em seguida?**
- [ ] A) O roteador repassa o pacote para o próximo salto e alerta o administrador via SNMP.
- [ ] B) O roteador descarta o pacote e envia uma mensagem ICMP "Time Exceeded" de volta à origem.
- [ ] C) O roteador encapsula o pacote em um frame Ethernet de Broadcast L2.
- [ ] D) O roteador recarrega o TTL para 255 e redireciona o tráfego.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O campo TTL/Hop Limit serve especificamente para evitar que pacotes fiquem em loop infinito na internet. Quando atinge 0, o pacote é morto, e a origem é notificada via mensagem ICMP "Time Exceeded" — este é o exato mecanismo que faz o utilitário Traceroute funcionar.
</details>
<br>

**6. Durante o Lab 7.2.8 (Verify IPv4 and IPv6 Addressing), qual comando é executado no terminal do Windows para traçar a rota (saltos de roteamento) de um pacote IP do host local até o servidor remoto?**
- [ ] A) `traceroute`
- [ ] B) `tracert`
- [ ] C) `ping -t`
- [ ] D) `ipconfig /trace`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Em sistemas operacionais Microsoft Windows (como os PCs do Packet Tracer lab), o utilitário de linha de comando para rastreamento de rota é chamado `tracert`. Em Linux, macOS e dispositivos Cisco, utiliza-se `traceroute`.
</details>
<br>

**7. O que caracteriza uma infraestrutura de rede que opera em modo "Dual-Stack" (Pilha Dupla)?**
- [ ] A) Uma rede que utiliza simultaneamente topologias em estrela e em anel para redundância de cabo físico.
- [ ] B) Dispositivos e interfaces de rede que executam e suportam os protocolos IPv4 e IPv6 simultaneamente.
- [ ] C) Uma configuração de Firewall onde as regras de Inbound e Outbound são empilhadas juntas.
- [ ] D) O uso de TCP e UDP no mesmo número de porta de uma aplicação.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Dual-Stack é a estratégia de transição primária para a internet moderna. Significa que os roteadores, switches e sistemas operacionais lidam tanto com tráfego IPv4 quanto IPv6 nativamente nas mesmas interfaces físicas, sem precisar de tradutores (como NAT64).
</details>
<br>

**8. Após enviar um ICMPv6 Neighbor Solicitation (NS), um PC aguarda uma mensagem NA (Neighbor Advertisement) de volta. Qual informação crucial a mensagem NA de resposta carregará?**
- [ ] A) A porta lógica do serviço solicitado.
- [ ] B) A máscara de sub-rede do servidor DHCP.
- [ ] C) O endereço MAC Ethernet do dispositivo alvo.
- [ ] D) A chave pública de encriptação TLS do roteador.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> A mensagem NA (Neighbor Advertisement) tem a função análoga ao "ARP Reply". Ela declara ao dispositivo que solicitou o contato: "Eu sou o dono deste IPv6, e o meu Endereço Físico (MAC) de Camada 2 para envio do frame é este".
</details>
<br>

**9. Quando um host IPv6 acaba de inicializar e não quer esperar pelo ciclo de 200 segundos do roteador para obter sua configuração de rede, qual mensagem do protocolo Neighbor Discovery ele dispara ativamente?**
- [ ] A) Neighbor Advertisement (NA)
- [ ] B) Router Solicitation (RS)
- [ ] C) Echo Request
- [ ] D) DHCP Request

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O host em boot gera um endereço Link-Local provisório e dispara um ICMPv6 Router Solicitation (RS) para o endereço multicast de roteadores, efetivamente pedindo à rede: "Por favor, algum Roteador ativo envie-me uma mensagem de Router Advertisement (RA) agora".
</details>
<br>

**10. Se você for encarregado de validar a configuração de endereçamento no Prompt de Comando do Windows (Lab 7.2.8), quais os dois comandos corretos para exibir todos os detalhes do adaptador físico, listando o IPv4 e depois listando a configuração do IPv6?**
- [ ] A) `ifconfig` e `ifconfig -v6`
- [ ] B) `netstat -nr` e `show ipv6 route`
- [ ] C) `ipconfig /all` e `ipv6config /all`
- [ ] D) `ip address` e `ipv6 address`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Em ambientes Microsoft Windows, `ipconfig /all` é usado para o detalhamento completo do adaptador, incluindo IPv4 e MAC. A variante específica para focar em atribuições IPv6 é `ipv6config /all` no simulador. Em sistemas Linux (incluindo o CyberOps VM), o padrão atual seria `ip address`.
</details>
<br>

**11. Qual é a principal diferença conceitual entre uma mensagem de erro ICMP "Destination Unreachable" e uma mensagem "Time Exceeded"?**
- [ ] A) "Unreachable" indica que o cabo de rede está fisicamente desconectado, "Time Exceeded" indica erro de DNS.
- [ ] B) "Unreachable" ocorre quando a rota para a rede alvo não existe na tabela de roteamento (o pacote não pode ser entregue), enquanto "Time Exceeded" ocorre quando o pacote fica preso em um loop e o TTL zera.
- [ ] C) Ambas são enviadas apenas pelo host de destino para recusar conexões.
- [ ] D) Nenhuma diferença, são sinônimos e usadas aleatoriamente dependendo do fabricante do roteador.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> "Destination Unreachable" é uma falha de entrega por falta de conhecimento do caminho (o roteador não sabe para onde mandar) ou por proibição administrativa (Firewall negou). "Time Exceeded" ocorre por expiração do limite de saltos (Hop Limit/TTL) durante o trânsito.
</details>
<br>

**12. Em qual camada do Modelo OSI o ICMP (Internet Control Message Protocol) opera?**
- [ ] A) Camada 2 - Enlace de Dados
- [ ] B) Camada 3 - Rede
- [ ] C) Camada 4 - Transporte
- [ ] D) Camada 7 - Aplicação

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O ICMP é um protocolo da Camada 3 (Rede). Apesar de seu payload muitas vezes testar as camadas inferiores, o cabeçalho ICMP é encapsulado diretamente logo após o cabeçalho IPv4 ou IPv6 (sem usar números de porta L4 de TCP ou UDP).
</details>
<br>

**13. No mecanismo IPv6 SLAAC, como um host normal configura o seu próprio campo "Gateway Padrão" ao receber uma mensagem RA (Router Advertisement)?**
- [ ] A) Faz uma solicitação extra ao servidor de DNS pela rota padrão.
- [ ] B) Define a porta lógica do RA como gateway.
- [ ] C) O host extrai o endereço "Link-Local" (fe80::) do roteador emissor (Endereço IP de Origem do pacote RA) e o atribui como o seu Default Gateway.
- [ ] D) Utiliza o Broadcast Mac Address FF:FF:FF:FF:FF:FF.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Diferente do DHCP IPv4 (onde o roteador pode ser um IP distante), o IPv6 usa o próprio endereço de enlace físico do roteador (Link-Local) como portal de saída. O host simplesmente lê quem enviou o RA e confia naquele Link-Local como sendo o gateway correto da LAN.
</details>
<br>

**14. Um analista do SOC pede para que você execute um `ping` focado exclusivamente no IP do "Gateway Padrão". Qual é o objetivo técnico deste teste específico na metodologia de troubleshooting?**
- [ ] A) Testar o DNS global do provedor.
- [ ] B) Confirmar a disponibilidade dos servidores de aplicação do Datacenter em outra cidade.
- [ ] C) Isolar a rede. Se o ping no gateway funciona, significa que a Camada 1, Camada 2, a placa de rede e o cabo local estão saudáveis até a fronteira da LAN; o problema provavelmente está na internet (externo).
- [ ] D) Limpar o cache de ARP da interface.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Pingar o default gateway é o passo vital após pingar o loopback. Se você atinge o gateway, toda a sua estrutura local de switches e cabos físicos está intacta. Qualquer falha após esse ponto é um problema de roteamento externo ou bloqueio de firewall de borda.
</details>
<br>

**15. As mensagens do ICMPv6 Neighbor Discovery não dependem de Broadcasts "barulhentos" como o ARP. Para quais alvos lógicos as mensagens RA e RS são tipicamente endereçadas usando Multicast?**
- [ ] A) RA é enviado para o Multicast "All-IPv6-Devices", e o RS é enviado para o Multicast "All-IPv6-Routers".
- [ ] B) Ambas são enviadas em Unicast exclusivo.
- [ ] C) RS é enviado para o servidor DNS, RA é enviado para o Switch Core.
- [ ] D) RA é enviado apenas para redes de 2.4GHz, RS para 5GHz.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> No ICMPv6, as comunicações de descobrimento são precisas. Quando o roteador envia um RA, ele manda para o grupo Multicast "Todos os nós IPv6" (All-nodes). Quando o Host quer descobrir quem é o roteador e envia um RS, ele poupa os outros PCs da rede direcionando a mensagem ao grupo Multicast "Todos os Roteadores IPv6" (All-routers).
</details>
