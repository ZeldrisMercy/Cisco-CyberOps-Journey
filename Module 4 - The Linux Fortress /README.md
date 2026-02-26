# 🛡️ LEVEL 4: THE LINUX FORTRESS (KALI & CYBEROPS ESSENTIALS)

![CISCO](https://img.shields.io/badge/CISCO-NETACAD-orange) ![STATUS](https://img.shields.io/badge/STATUS-COMPLETED-green) ![FOCUS](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue)

## 📊 PROGRESSO DA MISSÃO

* **Módulo 4.1: Linux Basics** — Status: 100% Concluído
* **Módulo 4.2: Working in the Linux Shell** — Status: 100% Concluído 💻
* **Módulo 4.3: Linux Servers and Clients** — Status: 100% Concluído 🛡️
* **Módulo 4.4: Basic Server Administration** — Status: 100% Concluído ⚙️
* **Módulo 4.5: The Linux File System** — Status: 100% Concluído 📂
* **Módulo 4.6: Working with the Linux GUI** — Status: 100% Concluído 🖥️
* **Módulo 4.7: Working on a Linux Host** — Status: 100% Concluído ⚔️

---

## ⚔️ SKILL TREE: ANÁLISE PROFUNDA E ARQUITETURA DE SISTEMA

### 💻 4.2. WORKING IN THE LINUX SHELL (CORE CLI)
* **Shell & Terminal Emulator:** Domínio do interpretador de comandos e uso das páginas de manual (`man`) para explorar a documentação embutida e opções de ferramentas.
* **Navegação Absoluta e Relativa:** Manipulação de caminhos no sistema, onde o diretório atual é representado por `.` e o diretório pai por `..`.
* **Operadores de Redirecionamento:** Uso de `>` para sobrescrever saídas em arquivos e `>>` para anexar (append) dados sem alterar o conteúdo original.
* **Arquivos Ocultos (Dot-files):** Identificação de arquivos que começam com um `.` (ponto), fundamentais para configurações de ambiente como o `.bashrc`.
* **Text Editors (CLI & GUI):** Operação de editores gráficos como SciTE e maestria em editores de terminal como `nano` e `vi/vim` para administração remota via SSH.

### 🛡️ 4.3. LINUX SERVERS AND CLIENTS
* **Daemons & Processos:** Entendimento de que servidores são programas em background aguardando requisições, com auditoria de hierarquia via `ps -ejH`.
* **Mapeamento de Sockets de Rede:** Uso do `netstat -tunap` para correlacionar portas abertas (listening) com Process IDs (PIDs) para identificar serviços ativos.
* **Auditoria Ativa com Telnet:** Uso tático do Telnet para testar disponibilidade de portas TCP e realizar banner grabbing (extração de versão de serviços).

### ⚙️ 4.4. BASIC SERVER ADMINISTRATION
* **Gestão de Configurações (`/etc` vs `/home`):** Separação de escopo onde configurações de usuário ficam na home e configurações globais de serviços residem em `/etc/`.
* **Análise de Logs Clássicos (`/var/log`):** Investigação forense de arquivos como `/var/log/messages` e monitoramento em tempo real com `tail -f`.
* **Ecossistema Systemd & Journalctl:** Uso do `journalctl` para filtrar eventos por boot (`-b`) ou por unidade de serviço específica (`-u`).

### 📂 4.5. THE LINUX FILE SYSTEM
* **Mounting & Block Devices:** Processo de vincular partições físicas (como `/dev/sda1`) a diretórios lógicos (pontos de montagem) para torná-las acessíveis.
* **Sistema de Permissões (Octal & Simbólico):** Controle granular via `chmod` e `chown`, utilizando lógica binária para definir leitura, escrita e execução.
* **Links (Simbólicos vs Hard):** Diferença entre Symbolic Links (atalhos de caminho) e Hard Links (ponteiros diretos para o Inode/conteúdo físico).

### 🖥️ 4.6. WORKING WITH THE LINUX GUI
* **X Window System:** Compreensão da infraestrutura básica que fornece as capacidades fundamentais para a interface gráfica no Linux.
* **Linux Desktop Environments (DE):** Gestão e operação de ambientes gráficos (como GNOME ou XFCE) para facilitar a administração visual de ferramentas de segurança.

### ⚔️ 4.7. WORKING ON A LINUX HOST
* **Application Management:** Instalação e execução de aplicações, garantindo que o sistema permaneça atualizado com os últimos patches de segurança.
* **Processos e Forks:** Monitoramento de processos e compreensão do mecanismo de "forking", onde um processo cria uma cópia de si mesmo para realizar tarefas paralelas.
* **Rootkit Check & Malware Defense:** Utilização de ferramentas de auditoria para detectar malwares de persistência profunda que tentam ocultar sua presença do sistema.
* **Advanced Command Piping:** Maestria no encadeamento de comandos complexos para filtragem de dados e automação de triagem em investigações.

---

## 🎒 ARSENAL DE COMANDOS (CHEAT SHEET)

* **`netstat -tunap`**: Lista conexões TCP/UDP numéricas, sockets em escuta e o PID/Nome do programa responsável pela conexão.
* **`ps -ejH`**: Exibe a árvore de processos completa para visualizar a hierarquia e processos filhos.
* **`chmod 665 <arquivo>`**: Define permissões: Dono (RW-), Grupo (RW-) e Outros (R-X).
* **`chown <user>:<group> <arquivo>`**: Altera o proprietário e o grupo de um arquivo simultaneamente.
* **`tail -f <arquivo_de_log>`**: Segue o final de um arquivo de log em tempo real, exibindo novas entradas conforme ocorrem.
* **`journalctl -u <serviço>`**: Filtra logs do sistema para exibir apenas eventos de um serviço específico.
* **`mount <dispositivo> <ponto_de_montagem>`**: Monta um dispositivo de bloco em um diretório específico.
* **`ln -s <alvo> <link>`**: Cria um link simbólico (atalho) para um arquivo ou diretório.

---

*Documentação mantida por **Ícaro de Souza Mariano** | Analista de Segurança em Formação*
