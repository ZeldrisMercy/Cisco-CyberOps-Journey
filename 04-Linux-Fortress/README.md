# 📁 Module 04: Linux Operating System & Host-Based Analysis

> [!NOTE]
> **Resumo Executivo:** Este módulo estabelece o domínio operacional sobre o sistema Linux, com ênfase em distribuições voltadas para segurança corporativa. O foco é capacitar o analista na navegação avançada via CLI, matemática de permissões, administração de daemons, manipulação forense de logs e gestão de identidades, cobrindo 100% da infraestrutura do exame CBROPS 200-201.

---

## 🏛️ Filosofia e Arquitetura Linux

Para operar defesas no Linux, duas regras de ouro devem ser internalizadas: **1. Tudo é um arquivo** (até teclados e conexões de rede são representados em `/dev` ou `/proc`); **2. Programas pequenos fazem apenas uma coisa bem feita** (e se conectam via *Pipes* `|`).

### 1. A Hierarquia do Sistema de Arquivos (FHS)
* `/etc`: O cérebro das configurações globais (ex: `nginx.conf`, `sshd_config`).
* `/var/log`: A casa dos logs e auditorias.
* `/bin` e `/sbin`: Binários essenciais. O `/sbin` contém ferramentas exclusivas para o usuário `root`.
* `/home`: Onde residem os arquivos de usuários comuns e configurações de ambiente (como o `.bashrc`).
* `/tmp`: Arquivos temporários. **Atenção (SOC):** Malwares frequentemente são baixados para cá porque qualquer usuário tem permissão de escrita.

### 2. Gestão de Identidades e Privilégios
O controle de acesso no Linux depende de como o sistema armazena as credenciais:
* `/etc/passwd`: Lista todos os usuários, seus IDs (UID), IDs de grupo (GID) e o shell padrão (ex: `/bin/bash`). **Qualquer um pode ler este arquivo.**
* `/etc/shadow`: Onde os **hashes** das senhas são guardados. **Apenas o root pode ler.** O vazamento deste arquivo permite ataques offline de quebra de senhas (ex: usando John the Ripper ou Hashcat).
* `sudo` vs. `su`: O comando `su root` troca de usuário exigindo a senha do root. O `sudo` executa um comando com privilégios elevados usando a senha do *próprio usuário*, deixando um rastro de auditoria perfeito no `/var/log/auth.log`.

### 3. Matemática de Permissões
As permissões são lidas como **R**ead (4), **W**rite (2) e e**X**ecute (1).
* **Exemplo:** `chmod 750 script.sh`
  * 7 (4+2+1) = O Dono (Owner) pode Ler, Gravar e Executar.
  * 5 (4+1) = O Grupo (Group) pode Ler e Executar.
  * 0 = Outros (Others) não têm acesso algum.
* O comando `chown root:admin arquivo.txt` transfere a posse do arquivo para o root e para o grupo admin.

---

## ⚙️ Gestão de Serviços (Systemd) e Troubleshooting

Adversários tentam instalar serviços maliciosos ou derrubar serviços de defesa (como EDRs e firewalls locais).

### 1. Controlando Daemons com `systemctl`
Sistemas modernos abandonaram o antigo *init* em favor do *systemd*.
* `systemctl status ssh`: Verifica se o servidor SSH está rodando.
* `systemctl start / stop ssh`: Inicia ou para o serviço imediatamente.
* `systemctl enable / disable ssh`: **Crucial para persistência.** Define se o serviço deve iniciar automaticamente junto com o boot do sistema.

### 2. Canivete Suíço de Rede
* `ip addr` ou `ip a`: Substitui o obsoleto `ifconfig` para verificar IPs e interfaces físicas/virtuais.
* `dig dominio.com` ou `nslookup`: Ferramentas vitais para investigar problemas de resolução DNS ou mapear a infraestrutura de um domínio suspeito.
* `curl -v http://site.com`: Faz uma requisição web crua. Excelente para testar se um servidor web está respondendo ou para baixar *payloads* em ambientes controlados.

---

## 🛡️ O Arsenal de Auditoria e Resposta (CLI)

### 1. Gerenciamento de Processos
O Linux usa um processo de clonagem chamado **Forking**, onde um processo "Pai" cria processos "Filhos".
* `ps -ejH` ou `ps -elf`: Lista a árvore de processos mostrando quem executou o quê.
* `netstat -tunap` ou `ss -tunap`: Caça conexões **T**CP/**U**DP em formato **N**umérico, mostrando todas (**A**) as portas e o **P**ID/Programa atrelado a elas.

### 2. Pipeline de Análise de Logs (A Abordagem DevSecOps)
Diferente do Event Viewer do Windows, os logs no Linux são textos puros. O analista não usa o mouse; ele usa processamento de texto avançado:
* `grep "Failed password" /var/log/auth.log`: Filtra apenas as linhas de falha de login.
* `awk '{print $11}'`: Pega o resultado do `grep` e extrai apenas a 11ª coluna (onde o IP do atacante costuma ficar).
* `sort | uniq -c`: Organiza e conta quantas vezes cada IP tentou invadir o sistema.

> **Exemplo Prático de Triage:** > `cat /var/log/auth.log | grep "Failed" | awk '{print $11}' | sort | uniq -c`
> *Este comando de uma linha revela exatamente quais IPs estão fazendo força bruta e com qual frequência.*

---

## 📑 Tactical Field Report: Lab Executions

* **[Lab - Working in the Linux Shell]:** Domínio de operadores de redirecionamento (`>` sobrescreve o arquivo; `>>` adiciona ao final, vital para preservar logs).
* **[Lab - Linux Servers and Clients]:** Auditoria ativa com o `Telnet` para testar disponibilidade de portas e realizar *Banner Grabbing* (extração de versões de serviços em portas abertas).
* **[Lab - File System & Rootkits]:** Busca de malwares de persistência profunda (Rootkits) que modificam binários do Kernel para esconder processos da saída nativa do comando `ps`.
