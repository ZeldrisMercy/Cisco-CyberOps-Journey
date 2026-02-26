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
* [cite_start]**Shell & Terminal Emulator:** Domínio do interpretador de comandos[cite: 1772, 1773]. [cite_start]Uso das páginas de manual (`man`) para explorar a documentação embutida do sistema e opções de ferramentas[cite: 1780, 1781, 1782].
* **Navegação Absoluta e Relativa:** Manipulação de caminhos no sistema. [cite_start]Entendimento de que o diretório atual é representado por `.` (dot) e o diretório pai (um nível acima) por `..` (double dot)[cite: 1846, 1847, 1848, 1856, 1870].
* **Operadores de Redirecionamento:** Controle de fluxo de dados no terminal. [cite_start]Uso de `>` para redirecionar e sobrescrever a saída de um comando para um arquivo, e `>>` para adicionar (append) dados ao final de um arquivo sem alterar o conteúdo existente[cite: 1878, 1879, 1906, 1907].
* [cite_start]**Arquivos Ocultos (Dot-files):** Identificação de arquivos que começam com um `.` (ponto), geralmente usados para armazenar configurações de aplicativos e ambiente de usuário na pasta `/home` (ex: `.bashrc`)[cite: 1453, 1542, 1915, 1916].
* [cite_start]**Text Editors (CLI & GUI):** Operação de editores gráficos enxutos como o SciTE e maestria em editores de terminal essenciais para acesso remoto (SSH) como GNU `nano` e `vi/vim`[cite: 1350, 1351, 1393, 1394, 1400].

### 🛡️ 4.3. LINUX SERVERS AND CLIENTS
* [cite_start]**Daemons & Processos:** Compreensão de que servidores são essencialmente programas rodando em background aguardando requisições[cite: 12, 13, 23, 24]. [cite_start]Auditoria da hierarquia de processos utilizando o comando `ps -ejH`[cite: 36, 37].
* [cite_start]**Mapeamento de Sockets de Rede:** Uso avançado do `netstat` (ex: `netstat -tunap`) para correlacionar portas abertas (listening) com seus respectivos Process IDs (PIDs), vital para identificar serviços[cite: 59, 72, 82].
* [cite_start]**Auditoria Ativa com Telnet:** Embora inseguro para administração remota por transmitir dados em texto claro, o Telnet é utilizado taticamente para testar rapidamente a disponibilidade e interagir com serviços TCP rodando em portas específicas (ex: testar a porta 80 para validar um servidor web Nginx)[cite: 104, 105, 106, 108, 109, 114].

### ⚙️ 4.4. BASIC SERVER ADMINISTRATION
* **Gestão de Configurações (`/etc` vs `/home`):** Entendimento da arquitetura de configurações. [cite_start]Arquivos de escopo de usuário ficam ocultos em seus diretórios home (ex: `~/.bashrc`), enquanto configurações de serviços globais do sistema residem no diretório restrito `/etc/`[cite: 1440, 1448, 1547].
* [cite_start]**Análise de Logs Clássicos (`/var/log`):** Investigação de eventos de sistema e serviços[cite: 182, 183]. [cite_start]Dissecação de arquivos como `/var/log/messages` (eventos do kernel/OS) e uso do comando `tail -f` para monitoramento defensivo em tempo real de logs de acesso[cite: 228, 229, 478, 521, 522].
* [cite_start]**Ecossistema Systemd & Journalctl:** Substituindo sistemas *init* mais antigos, o `systemd` gerencia a inicialização e unifica configurações[cite: 627]. [cite_start]O serviço `systemd-journald` coleta os logs em arquivos binários[cite: 629]. [cite_start]O domínio do comando `journalctl` permite filtrar eventos por boot (`-b`) ou focar em serviços específicos (`-u`)[cite: 631, 663, 801].

### 📂 4.5. THE LINUX FILE SYSTEM
* [cite_start]**Mounting & Block Devices:** Todo hardware no Linux é um arquivo (ex: `/dev/sda` para discos)[cite: 962]. [cite_start]A técnica de *mounting* liga fisicamente a partição do dispositivo a um diretório lógico (Mounting Point), tornando o sistema de arquivos acessível ao SO[cite: 935, 936, 937].
* [cite_start]**Sistema de Permissões (Octal & Simbólico):** Controle granular de acesso usando `chmod` e `chown`[cite: 1078, 1111]. [cite_start]Leitura de permissões na notação octal, onde, por exemplo, `665` significa permissão total de leitura/escrita para o Owner (6=110) e Group (6=110), e leitura/execução para Outros (5=101)[cite: 1104, 1105, 1107, 1108, 1109].
* [cite_start]**Links (Simbólicos vs Hard):** Diferenciação arquitetônica onde *Symbolic Links* (`ln -s`) agem como atalhos apontando para o nome/caminho de um arquivo, enquanto *Hard Links* (`ln`) apontam diretamente para o conteúdo físico do arquivo no disco (Inode)[cite: 1279, 1280, 1288].

---

## 🎒 ARSENAL DE COMANDOS (CHEAT SHEET)

* [cite_start]**`netstat -tunap`**: Formata e filtra a saída de conexões ativas na rede[cite: 58, 59]. [cite_start]Lista portas lógicas TCP (`t`) e UDP (`u`), em formato numérico numérico sem resolver DNS (`n`), revelando todos os sockets ativos (`a`) e o Process ID / Nome do Programa (`p`) rodando em cada porta[cite: 59, 68].
* [cite_start]**`ps -ejH`**: Exibe a árvore de processos rodando no background, revelando a hierarquia (processo pai e processo filho) para rastrear o fluxo de execução no sistema[cite: 26, 36, 37].
* [cite_start]**`chmod 665 <arquivo>`**: Altera as permissões de acesso de um arquivo utilizando o formato octal[cite: 1092, 1104]. [cite_start]Concede leitura e escrita para o Dono (6 = 110 em binário), leitura e escrita para o Grupo (6 = 110), e leitura e execução para Outros usuários (5 = 101)[cite: 1105, 1107, 1108, 1109].
* [cite_start]**`chown <user>:<group> <arquivo>`**: Comando utilizado para alterar simultaneamente o Dono (owner) e o Grupo de um arquivo ou diretório[cite: 1111, 1126].
* **`tail -f <arquivo_de_log>`**: Ferramenta indispensável para analistas. [cite_start]Exibe o final de um arquivo (como o `access.log`) e o parâmetro `-f` (follow) mantém o comando rodando em tempo real, monitorando e exibindo novas entradas no log instantaneamente[cite: 484, 521, 522].
* [cite_start]**`journalctl -u <serviço>`**: Consulta e filtra logs gerados pelo moderno `systemd-journald`, isolando apenas os eventos relacionados a um serviço específico (ex: `nginx.service`)[cite: 629, 631, 801, 802].
* [cite_start]**`mount <dispositivo> <ponto_de_montagem>`**: Torna um sistema de arquivos acessível ao SO, ligando uma partição física (como `/dev/sdb1`) a um diretório vazio criado para este fim (como `~/second_drive/`)[cite: 935, 936, 1017, 1018].
* **`ln -s <alvo> <link>`**: Cria um "Link Simbólico". [cite_start]Age exatamente como um atalho do Windows, apontando para o caminho/nome de um arquivo original[cite: 1278, 1280, 1288].

---

## 🧪 TACTICAL FIELD REPORTS (LABS)

* **LAB 4.2.6 - Working with Text Files in the CLI**
  * [cite_start]*Missão:* Operar editores de texto (SciTE e nano) e manipular configurações essenciais[cite: 1336, 1350, 1400]. [cite_start]Foco prático em alterar o comportamento visual do terminal (`.bashrc`) e reconfigurar a porta e diretório alvo de um servidor web (`custom_server.conf`)[cite: 1529, 1584, 1634, 1730, 1732].
* **LAB 4.2.7 - Getting Familiar with the Linux Shell**
  * [cite_start]*Missão:* Manipulação avançada do file system via CLI[cite: 1765]. [cite_start]Execução tática de criação de diretórios (`mkdir`), cópias (`cp`), movimentações (`mv`) e deleção recursiva (`rm -r`)[cite: 1796, 1938, 1971, 1984]. [cite_start]O laboratório também aprofunda o uso de operadores de redirecionamento (`>` e `>>`) para salvar dados diretamente no terminal[cite: 1878, 1879, 1906, 1907].
* **LAB 4.3.4 - Linux Servers**
  * [cite_start]*Missão:* Identificar serviços rodando e monitorar comunicações de rede usando a linha de comando[cite: 5, 51]. [cite_start]Auditoria de processos ativos via `ps` em conjunto com a varredura local de conexões do `netstat`, culminando na interação manual com servidores web utilizando conexões `telnet`[cite: 26, 51, 86, 114].
* **LAB 4.4.4 - Locating Log Files**
  * [cite_start]*Missão:* Forense de rastros no sistema[cite: 174]. [cite_start]Investigação proativa de eventos no Apache e registros de Kernel (`/var/log/messages`)[cite: 189, 228]. [cite_start]Evolução de ferramentas passivas como `cat` e `more` para monitoramento constante com `tail -f`, até a maestria em consultas avançadas na arquitetura `systemd` via `journalctl`[cite: 231, 478, 627, 631].
* **LAB 4.5.4 - Navigating the Linux Filesystem and Permission Settings**
  * [cite_start]*Missão:* Domínio de infraestrutura de armazenamento e Hardening de privilégios[cite: 921]. [cite_start]O laboratório aborda desde o rastreamento de block devices (`lsblk`) e montagem manual de discos, até a aplicação de `chmod`/`chown` para restrição de leitura[cite: 938, 997, 1078, 1111]. [cite_start]Também engloba a criação e distinção prática entre links simbólicos (`ln -s`) e físicos (`ln`)[cite: 1280, 1288].

---

*Documentação mantida por **Ícaro de Souza Mariano** | Analista de Segurança em Formação*
