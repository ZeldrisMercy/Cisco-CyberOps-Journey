## 🛡️ Anexo Tático: Dissecando Frames L2 e Ameaças ARP

> [!WARNING]
> **Atenção Analista:** Compreender a teoria do ARP é apenas o primeiro passo. No dia a dia de um Centro de Operações de Segurança (SOC), você precisará olhar diretamente para os bits e bytes no Wireshark para distinguir tráfego legítimo de um ataque de *Man-in-the-Middle*.

Esta seção aprofunda a análise de cabeçalhos Ethernet e o comportamento de roteamento L2/L3 com base em capturas reais de laboratório.

---

### 🔬 Anatomia de um Frame Ethernet II (Visão do Analista)

[cite_start]Quando o Wireshark intercepta o tráfego de rede local, ele nos mostra exatamente como os dados da Camada 3 (como pacotes IPv4 ou mensagens ICMP) foram envelopados na Camada 2[cite: 21, 23]. Aqui está o que você deve procurar no painel de "Packet Details":

1.  [cite_start]**Preamble (8 Bytes):** Este campo contém bits de sincronização processados diretamente pelo hardware da placa de rede (NIC)[cite: 95]. [cite_start]**Nota:** O Wireshark *não* exibe o preâmbulo porque a placa de rede o descarta antes de enviar o frame para o sistema operacional[cite: 283].
2.  [cite_start]**Destination Address (6 Bytes):** O endereço MAC para onde o quadro está indo[cite: 100]. [cite_start]Pode ser um Unicast (dispositivo específico) ou um Broadcast (`ff:ff:ff:ff:ff:ff`)[cite: 78, 100].
3.  [cite_start]**Source Address (6 Bytes):** O endereço MAC de quem enviou[cite: 100].
    * [cite_start]*Dica Forense:* Os primeiros três bytes (6 dígitos hexadecimais) formam o **OUI (Organizationally Unique Identifier)**, que revela o fabricante da placa de rede[cite: 100]. [cite_start]Os últimos três bytes são o número de série[cite: 100].
4.  **Frame Type (2 Bytes):** O campo mais crítico para triagem rápida. [cite_start]Ele diz qual protocolo está encapsulado[cite: 100]:
    * [cite_start]`0x0800`: O payload é um pacote **IPv4**[cite: 100].
    * [cite_start]`0x0806`: O payload é uma mensagem **ARP**[cite: 100].
5.  [cite_start]**Data (46 a 1500 Bytes):** A carga útil (PDU da camada superior)[cite: 100].
6.  **FCS (4 Bytes):** O *Frame Check Sequence*. Calculado pelo emissor para identificar erros de transmissão. [cite_start]Se o receptor encontrar uma divergência, o pacote é descartado sumariamente pelo hardware[cite: 100].



---

### 🌐 O Comportamento de Roteamento na Prática (Mininet Lab)

[cite_start]Para provar como o MAC e o IP trabalham juntos, executamos um laboratório isolado usando *Mininet*, onde o Host H3 (`10.0.0.13`) enviou pings para destinos diferentes[cite: 119, 139, 269].

**Cenário 1: Tráfego Local (H3 enviando ping para o Gateway)**
* [cite_start]**Ação:** O H3 (`10.0.0.13`) envia um *Echo Request* para o IP `10.0.0.1` (o Gateway Padrão)[cite: 140, 158].
* [cite_start]**Análise Wireshark:** O endereço MAC de destino no frame L2 pertence diretamente à placa de rede do Gateway[cite: 228]. A comunicação não sai da LAN.

**Cenário 2: Tráfego Remoto (H3 enviando ping para a rede 172.16.0.0/12)**
* [cite_start]**Ação:** O H3 envia pings para o Host H4, cujo IP é `172.16.0.40`[cite: 269].
* [cite_start]**Análise Wireshark:** Ao inspecionar o pacote capturado, o IP de destino mudou perfeitamente para `172.16.0.40`[cite: 280]. [cite_start]**No entanto, o endereço MAC de destino permaneceu o do Gateway R1**[cite: 281].
* **Conclusão Tática:** Endereços MAC são estritamente locais. [cite_start]Quando o tráfego precisa sair da sua sub-rede, o host encapsula o quadro L2 com o MAC do roteador, deixando o endereço IP L3 guiar o pacote pelo resto do caminho na internet[cite: 263, 281].

---

### 🚨 Cenário de Ameaça: ARP Spoofing e Flooding

A confiança inata do ARP o torna vulnerável a falhas de segurança críticas na Camada 2.

1.  **ARP Flooding (Problema de Performance):** Como as requisições ARP são enviadas em Broadcast para toda a mídia local, redes muito grandes e não segmentadas podem sofrer inundações de pacotes, esgotando recursos dos switches e dos hosts.
2.  **ARP Spoofing / Poisoning (Ataque Ativo):**
    * Um atacante (PC C) na mesma rede intercepta uma requisição legítima (Ex: PC A perguntando pelo MAC do Default Gateway `192.168.1.1`).
    * O atacante envia rapidamente um *ARP Reply* falsificado dizendo: *"Eu sou o 192.168.1.1, envie para o meu endereço MAC"*.
    * O PC A atualiza sua tabela ARP confiando cegamente na resposta. A partir desse momento, todo o tráfego destinado à internet passa primeiro pelo computador do atacante, caracterizando um ataque de *Man-in-the-Middle*.



---

### 💻 Arsenal de Comandos (Linux / CyberOps CLI)

Durante o laboratório de análise de frames ou em uma resposta a incidentes real, estes comandos de terminal são essenciais para manipular o ambiente L2/L3:

* **Verificar a Tabela de Roteamento:** Descubra quem é o seu Default Gateway.
    `netstat -r` [cite: 126]
* **Visualizar a Tabela ARP Atual:** Veja os mapeamentos MAC-IP ativos em cache sem precisar traduzir nomes de host (o `-n` mantém os IPs numéricos).
    `arp -n` [cite: 131]
* **Limpar Entradas do Cache ARP:** Força o sistema operacional a enviar um novo "ARP Request" para a rede (útil se você suspeita de envenenamento ARP ou se uma placa de rede foi trocada). Repita até limpar.
    `arp -d <endereço IP>` [cite: 133, 134]
