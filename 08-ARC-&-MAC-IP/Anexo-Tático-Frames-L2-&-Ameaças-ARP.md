# 🛡️ Anexo Tático: Dissecando Frames L2 e Ameaças ARP

> [!WARNING]
**Atenção Analista:** Compreender a teoria do ARP é apenas o primeiro passo. No dia a dia de um Centro de Operações de Segurança (SOC), você precisará olhar diretamente para os bits e bytes no Wireshark para distinguir tráfego legítimo de um ataque de *Man-in-the-Middle*.

Esta seção aprofunda a análise de cabeçalhos Ethernet e o comportamento de roteamento L2/L3 com base em capturas reais de laboratório.

### 🔬 Anatomia de um Frame Ethernet II (Visão do Analista)

Quando o Wireshark intercepta o tráfego de rede local, ele nos mostra exatamente como os dados da Camada 3 (como pacotes IPv4 ou mensagens ICMP) foram envelopados na Camada 2. Aqui está o que você deve procurar no painel de "Packet Details":

1.  **Preamble (8 Bytes):** Este campo contém bits de sincronização processados diretamente pelo hardware da placa de rede (NIC). O Wireshark não exibe o preâmbulo porque a placa de rede o descarta antes de enviar o frame para o sistema operacional.
2.  **Destination Address (6 Bytes):** O endereço MAC para onde o quadro está indo. Pode ser um Unicast (dispositivo específico) ou um Broadcast (`ff:ff:ff:ff:ff:ff`).
3.  **Source Address (6 Bytes):** O endereço MAC de quem enviou. Os primeiros três bytes (6 dígitos hexadecimais) formam o **OUI (Organizationally Unique Identifier)**, que revela o fabricante da placa de rede.
4.  **Frame Type (2 Bytes):** O campo mais crítico para triagem rápida. Ele diz qual protocolo está encapsulado:
    * `0x0800`: O payload é um pacote **IPv4**.
    * `0x0806`: O payload é uma mensagem **ARP**.
5.  **Data (46 a 1500 Bytes):** A carga útil (PDU da camada superior).
6.  **FCS (4 Bytes):** O *Frame Check Sequence*. Calculado pelo emissor para identificar erros de transmissão. Se o receptor encontrar uma divergência, o pacote é descartado sumariamente pelo hardware.



### 🌐 O Comportamento de Roteamento na Prática (Mininet Lab)

Para provar como o MAC e o IP trabalham juntos, executamos um laboratório isolado usando *Mininet*, onde o Host H3 (`10.0.0.13`) enviou pings para destinos diferentes.

**Cenário 1: Tráfego Local (H3 enviando ping para o Gateway)**
* **Ação:** O H3 (`10.0.0.13`) envia um *Echo Request* para o IP `10.0.0.1` (o Gateway Padrão).
* **Análise Wireshark:** O endereço MAC de destino no frame L2 pertence diretamente à placa de rede do Gateway. A comunicação não sai da LAN.

**Cenário 2: Tráfego Remoto (H3 enviando ping para a rede 172.16.0.0/12)**
* **Ação:** O H3 envia pings para o Host H4, cujo IP é `172.16.0.40`.
* **Análise Wireshark:** Ao inspecionar o pacote capturado, o IP de destino mudou perfeitamente para `172.16.0.40`. **No entanto, o endereço MAC de destino permaneceu o do Gateway R1**.
* **Conclusão Tática:** Endereços MAC são estritamente locais. Quando o tráfego precisa sair da sua sub-rede, o host encapsula o quadro L2 com o MAC do roteador, deixando o endereço IP L3 guiar o pacote pelo resto do caminho na internet.

### 💻 Arsenal de Comandos (Linux / CyberOps CLI)

Durante o laboratório de análise de frames ou em uma resposta a incidentes real, estes comandos de terminal são essenciais para manipular o ambiente L2/L3:

* **Verificar a Tabela de Roteamento:** Descubra quem é o seu Default Gateway.
    `netstat -r`
* **Visualizar a Tabela ARP Atual:** Veja os mapeamentos MAC-IP ativos em cache sem precisar traduzir nomes de host.
    `arp -n`
* **Limpar Entradas do Cache ARP:** Força o sistema operacional a enviar um novo "ARP Request" para a rede.
    `arp -d <endereço IP>`
