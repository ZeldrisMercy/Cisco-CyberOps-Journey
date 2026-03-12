# 📁 Module 10: Network Application Services & NAT

> [!NOTE]
> **Resumo Executivo:** Este módulo explora os serviços essenciais que fazem a internet e as redes corporativas funcionarem de forma invisível para o usuário final. 
> Da automação de IPs via **DHCP**, passando pela resolução de nomes via **DNS**, até a economia de endereços utilizando **NAT/PAT**. 
> Além da infraestrutura básica, detalhamos os protocolos de aplicação da camada 7, como transferência de arquivos (**FTP, TFTP, SMB**), correio eletrônico (**SMTP, POP3, IMAP**) e navegação Web (**HTTP/HTTPS e HTTP/2**), culminando na análise de como esse tráfego se apresenta em investigações forenses via Wireshark.

---

## 🏗️ 10.1 DHCP: Configuração Dinâmica de Hosts

O **DHCP (Dynamic Host Configuration Protocol)** é vital para redes escaláveis, automatizando a entrega de endereços IPv4, máscaras, gateways e servidores DNS.

### O Processo DORA
A comunicação ocorre em quatro etapas principais entre cliente e servidor:

1. **DHCPDISCOVER (Broadcast):** O cliente "grita" na rede procurando um servidor DHCP.
2. **DHCPOFFER (Unicast):** O servidor responde oferecendo um IP disponível.
3. **DHCPREQUEST (Broadcast):** O cliente solicita formalmente o IP oferecido.
4. **DHCPACK (Unicast):** O servidor confirma o aluguel (lease) do IP para o cliente.

*Nota:* O formato da mensagem DHCP inclui o *OP Code*, *Hardware Type*, endereços de IP do cliente (CIADDR), do seu novo IP (YIADDR), endereço do servidor (SIADDR) e do Gateway (GIADDR).

---

## 🌐 10.2 DNS: O Catálogo da Internet

O **DNS (Domain Name System)** resolve nomes de domínio amigáveis (FQDNs, como `www.cisco.com`) em endereços IP (numéricos) que os roteadores entendem.

### 10.2.2 Hierarquia de Domínios
O DNS usa um modelo de árvore invertida:
* **Root Level:** O topo da hierarquia (representado por um ponto `.`).
* **Top-Level Domain (TLD):** Como `.com`, `.net`, `.edu`, `.br`.
* **Second-Level Domain:** O nome da empresa/organização (ex: `cisco.com`).

### 10.2.5 & 10.2.6 Extensões: DDNS e WHOIS
* **DDNS (Dynamic DNS):** Atualiza os servidores DNS em tempo real quando um provedor muda o IP público do cliente dinamicamente.
* **WHOIS:** Protocolo baseado em TCP para descobrir donos de domínios, essencial para investigações de CyberOps (identificar origens de ataques).

---

## 🛡️ 10.3 NAT e PAT: Tradução e Economia de IPs

Devido ao esgotamento do IPv4, o **NAT (Network Address Translation)** permite que redes inteiras operem sob um único IP público.

### 10.3.1 Espaço de Endereço Privado (RFC 1918)
Estes IPs são descartados pelos roteadores da internet pública e só funcionam em LANs:

| Classe | Faixa RFC 1918 | Prefixo |
|--------|----------------|---------|
| **A** | 10.0.0.0 a 10.255.255.255 | `/8` |
| **B** | 172.16.0.0 a 172.31.255.255 | `/12` |
| **C** | 192.168.0.0 a 192.168.255.255 | `/16` |

### 10.3.4 PAT (Port Address Translation)
Também conhecido como *NAT Overload*, é o recurso usado em roteadores domésticos e corporativos. Ele mapeia **vários IPs privados para um único IP público**, utilizando **números de portas de origem** para rastrear qual dispositivo interno fez a requisição.

---

## 📁 10.4 Serviços de Arquivos: FTP, TFTP e SMB

| Protocolo | Descrição | Portas e Características |
|-----------|-----------|--------------------------|
| **FTP** | File Transfer Protocol | Requer duas conexões TCP: Porta **21 (Controle)** e Porta **20 (Dados)**. Tráfego em texto claro (inseguro). |
| **TFTP** | Trivial File Transfer Protocol | Usa **UDP (porta 69)**. Sem conexão, baixa sobrecarga. |
| **SMB** | Server Message Block | Protocolo cliente/servidor focado em compartilhar arquivos, impressoras e portas seriais (muito comum em redes Windows). |

---

## ✉️ 10.5 Protocolos de Email

O tráfego de email não vai direto de cliente para cliente, mas através de servidores:

* **SMTP (Simple Mail Transfer Protocol - Porta 25):** Usado para **ENVIAR** o e-mail do cliente para o servidor, ou entre servidores.
* **POP3 (Porta 110):** Usado para **RECEBER**. Ele baixa a mensagem e *deleta* a cópia do servidor (ruim para backup centralizado).
* **IMAP:** Usado para **RECEBER**. Sincroniza e *mantém* as mensagens no servidor, ideal para múltiplos dispositivos.

---

## 🕸️ 10.6 Tráfego Web: HTTP, HTTP/2 e HTTPS

### HTTP (Hypertext Transfer Protocol)
* **Status Codes Comuns:** `1xx` (Informational), `2xx` (Success, ex: 200 OK), `3xx` (Redirection), `4xx` (Client Error, ex: 404 Not Found), `5xx` (Server Error).
* **Métodos:** `GET` (solicita dados), `POST` (envia dados para processamento), `PUT` (faz upload), `DELETE` (exclui recurso).
* **Estrutura da URL:** Scheme/Protocol, Domain, Port, Path, Query, Fragment.

### HTTP/2 (Evolução)
Traz melhorias vitais de desempenho: Multiplexação (vários fluxos na mesma sessão TCP), Server Push, formato Binário (em vez de texto L1.1) e Compressão de Cabeçalhos.

### HTTPS (Secure)
Opera via porta TCP 443. Os dados do HTTP são encapsulados e criptografados pelo protocolo **TLS/SSL**. Em análise de pacotes, os dados HTTP somem e viram "*Application Data*".

---

## 📑 Tactical Field Report: Lab Executions (Wireshark)

Nos laboratórios de análise, constatamos que:
* **DNS usa UDP (porta 53):** Um datagrama pequeno de até 512 bytes minimiza o overhead de conexão. A requisição vai para a porta destino 53, e a resposta volta para a porta de origem aleatória criada pelo cliente.
* **TFTP usa UDP (porta 69):** O cabeçalho UDP tem apenas 8 bytes (Source Port, Dest Port, Length, Checksum).
* **HTTP via TCP:** Vemos os comandos `GET` e `POST` em texto claro. No painel detalhado (HTML Form URL Encoded), é possível capturar credenciais se não houver criptografia.
* **HTTPS via TCP:** A negociação de *handshake* revela o TLSv1.2. Após isso, toda a conversa vira carga útil criptografada (*Encrypted Application Data*), frustrando a interceptação em texto claro.
