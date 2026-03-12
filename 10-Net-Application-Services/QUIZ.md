# 🧠 Simulado Definitivo: Module 10 (Network Services)
Este simulado contém 15 questões de nível de certificação baseadas na infraestrutura de serviços de aplicação, DNS, DHCP, roteamento NAT/PAT e análise de pacotes (Wireshark) exigidos no contexto de redes e operações de segurança cibernética (CyberOps).

---

### 🌐 Domínio 1: Configuração Dinâmica (DHCP)

**1. Durante o processo DORA de alocação de endereço via DHCP, qual mensagem é enviada pelo servidor ao cliente confirmando a concessão final do endereço IP?**
- [ ] A) DHCPDISCOVER
- [ ] B) DHCPOFFER
- [ ] C) DHCPREQUEST
- [ ] D) DHCPACK

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> O processo completo é Discover, Offer, Request e Acknowledge. O <b>DHCPACK</b> é a última mensagem, enviada em unicast pelo servidor, confirmando que o cliente agora tem permissão para usar o IP.
</details>
<br>

**2. Qual campo da estrutura da mensagem DHCP carrega o endereço físico (MAC) da máquina do cliente que está solicitando configuração?**
- [ ] A) SIADDR
- [ ] B) CHADDR
- [ ] C) GIADDR
- [ ] D) YIADDR

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O campo <b>CHADDR</b> (Client Hardware Address) possui 16 bytes e transporta o endereço MAC do cliente para que o servidor possa identificá-lo e direcionar ofertas específicas.
</details>
<br>

---

### 📖 Domínio 2: Resolução de Nomes (DNS)

**3. Para minimizar o tempo e o overhead da rede, as consultas normais de DNS entre um cliente e o resolvedor local utilizam qual protocolo e porta de transporte?**
- [ ] A) TCP, Porta 53
- [ ] B) UDP, Porta 53
- [ ] C) TCP, Porta 80
- [ ] D) UDP, Porta 69

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Para requisições ágeis (menores que 512 bytes), o DNS utiliza o <b>UDP na porta 53</b>. Não requer o <i>three-way handshake</i>, garantindo respostas rápidas para os navegadores.
</details>
<br>

**4. Na estrutura hierárquica do DNS, domínios como ".com", ".net" e ".edu" pertencem a qual camada da árvore?**
- [ ] A) Root Level Domain
- [ ] B) Top-Level Domain (TLD)
- [ ] C) Second-Level Domain
- [ ] D) Subdomain

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Estes são exemplos de <b>Top-Level Domains (TLD)</b>, que vêm logo abaixo do domínio raiz (representado pelo ponto final) na hierarquia do DNS.
</details>
<br>

**5. Qual serviço permite consultar registros públicos para descobrir a organização proprietária de um domínio na internet, o que pode auxiliar investigações de tráfego suspeito?**
- [ ] A) DDNS
- [ ] B) DHCP
- [ ] C) WHOIS
- [ ] D) IMAP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>WHOIS</b> é um protocolo baseado em TCP usado por analistas para encontrar o registrante, datas de criação e provedores de um domínio internet.
</details>
<br>

---

### 🛡️ Domínio 3: NAT e Endereçamento Privado

**6. De acordo com a RFC 1918, qual das seguintes faixas representa o espaço de endereços internos da Classe C, tipicamente visto em redes domésticas?**
- [ ] A) 10.0.0.0 a 10.255.255.255
- [ ] B) 127.0.0.1 a 127.255.255.255
- [ ] C) 172.16.0.0 a 172.31.255.255
- [ ] D) 192.168.0.0 a 192.168.255.255

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> A faixa da <b>Classe C</b> para IPs privados é 192.168.0.0 até 192.168.255.255 (prefixo /16). É amplamente configurada como padrão em roteadores corporativos pequenos e residenciais.
</details>
<br>

**7. O que permite que 30 notebooks em uma empresa acessem a internet simultaneamente utilizando apenas UM endereço IP público fornecido pelo ISP?**
- [ ] A) DHCP Overload
- [ ] B) Port Address Translation (PAT)
- [ ] C) Static NAT
- [ ] D) DNS Recursion

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O <b>PAT</b> (ou NAT Overload) traduz múltiplos IPs privados em um único IP público usando diferentes <b>números de portas TCP/UDP de origem</b> para rastrear as sessões exclusivas.
</details>
<br>

---

### 📁 Domínio 4: Compartilhamento e Transferência

**8. Um analista observa tráfego TCP na porta 21 e nota conexões paralelas abrindo na porta 20. Qual protocolo de aplicação está sendo analisado?**
- [ ] A) TFTP
- [ ] B) SMB
- [ ] C) FTP
- [ ] D) SMTP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O <b>FTP</b> (File Transfer Protocol) usa duas conexões: TCP 21 para o canal de comandos/controle e TCP 20 para a real transferência de dados.
</details>
<br>

**9. Qual protocolo Microsoft é predominantemente usado para compartilhamento de arquivos, diretórios e impressoras numa rede local, atuando como um modelo request-response?**
- [ ] A) IMAP
- [ ] B) SMB
- [ ] C) TFTP
- [ ] D) HTTP/2

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O <b>SMB (Server Message Block)</b> é o protocolo nativo das redes Microsoft para controlar e compartilhar recursos como pastas e impressoras na rede local.
</details>
<br>

---

### ✉️ Domínio 5: Protocolos de Correio Eletrônico

**10. Qual protocolo de e-mail deve ser configurado na aplicação cliente para BAIXAR as mensagens do servidor e, como comportamento padrão, deletá-las logo após o download?**
- [ ] A) SMTP
- [ ] B) POP3
- [ ] C) IMAP
- [ ] D) SNMP

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O <b>POP3</b> (Porta 110) faz o download dos e-mails e os remove do servidor. O IMAP faria a sincronização, mantendo cópias originais intactas.
</details>
<br>

**11. Que protocolo entra em ação quando um usuário clica no botão "Enviar" no seu cliente de e-mail para transferir a mensagem até o Mail Server do seu domínio?**
- [ ] A) SMTP
- [ ] B) IMAP
- [ ] C) POP3
- [ ] D) SMB

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> O <b>SMTP</b> (Simple Mail Transfer Protocol - Porta 25) é o responsável por empurrar (enviar) e-mails do cliente para o servidor, ou transportar a mensagem entre diferentes servidores de correio.
</details>
<br>

---

### 🕸️ Domínio 6: Web e Análise Forense (HTTP/HTTPS)

**12. Em uma requisição HTTP capturada no Wireshark, qual código de status da resposta (Response Status Code) indica "Not Found" (Recurso não encontrado)?**
- [ ] A) 200
- [ ] B) 302
- [ ] C) 403
- [ ] D) 404

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D</b><br>
<i>Explicação:</i> O código <b>404 (Not Found)</b> indica erro do cliente ao solicitar uma URL ou arquivo que não existe no servidor HTTP. O 200 indica Sucesso e o 403 indica Proibido.
</details>
<br>

**13. Comparado ao HTTP 1.1 antigo, o HTTP/2 suporta "Multiplexação". O que isso significa na prática?**
- [ ] A) Ele criptografa o tráfego usando TLS 1.3 nativo.
- [ ] B) Ele permite várias solicitações de arquivos simultaneamente na mesma sessão TCP.
- [ ] C) Ele muda a porta padrão de acesso para 443.
- [ ] D) Ele comprime arquivos de imagem do servidor.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> A <b>Multiplexação</b> no HTTP/2 (via Streams) diminui a latência ao permitir que imagens, HTML e scripts sejam trafegados paralelamente sem precisar abrir e fechar várias sessões TCP.
</details>
<br>

**14. Um analista tenta ler credenciais em um tráfego de login via Wireshark. O tráfego usa protocolo HTTPS na porta 443. O que o analista verá na carga útil da mensagem?**
- [ ] A) HTML Form URL Encoded
- [ ] B) Plaintext GET e POST request
- [ ] C) Encrypted Application Data
- [ ] D) SMB Requests

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O HTTPS utiliza a camada TLS/SSL para proteger os dados da aplicação. O tráfego capturado no Wireshark apresentará o payload como <b>"Encrypted Application Data"</b>, impossibilitando leitura passiva dos pacotes em texto claro.
</details>
<br>

**15. No cabeçalho UDP inspecionado no Wireshark durante um tráfego TFTP, quantos bytes esse protocolo consome apenas em seu Header de transporte, indicando seu baixíssimo overhead?**
- [ ] A) 8 bytes
- [ ] B) 20 bytes
- [ ] C) 32 bytes
- [ ] D) 64 bytes

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> O cabeçalho UDP possui exatamente <b>8 bytes</b> de tamanho, dividido apenas em Porta de Origem, Porta de Destino, Tamanho (Length) e Checksum.
</details>
