# 🛡️ LEVEL 3: THE WINDOWS FORTRESS

![CISCO](https://img.shields.io/badge/CISCO-NETACAD-orange) ![STATUS](https://img.shields.io/badge/STATUS-COMPLETED-green) ![FOCUS](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue)

## 📊 PROGRESSO DA MISSÃO

* **Módulo 3.1: Windows History** — Status: 100% Concluído
* **Módulo 3.2: Windows Architecture and Operations** — Status: 100% Concluído
* **Módulo 3.3: Windows Configuration and Monitoring** — Status: 100% Concluído
* **Módulo 3.4: Windows Security** — Status: 100% Concluído

---

## ⚔️ SKILL TREE (HABILIDADES DESBLOQUEADAS)

### 3.1. EVOLUÇÃO E FUNDAMENTOS DO SO
* **Histórico e Vulnerabilidades:** Compreensão da evolução do MS-DOS para a arquitetura NT. Análise de como a herança de sistemas legados e a complexidade da GUI (Interface Gráfica) introduzem vetores de ataque e vulnerabilidades de dia zero.

### 3.2. ARQUITETURA E OPERAÇÕES INTERNAS (THE CORE)
* **Modos de Execução (Kernel vs. User):** Estudo da separação de privilégios onde o Kernel Mode possui acesso total ao hardware e a HAL (Hardware Abstraction Layer) isola o software das complexidades do hardware.
* **Sistemas de Arquivos e ADS:** Exploração do NTFS e a técnica de **Alternate Data Streams (ADS)**, utilizada por atacantes para ocultar arquivos maliciosos ou metadados dentro de arquivos legítimos sem alterar seu tamanho visível.
* **Workflow de Sistema:** Análise detalhada das etapas de Boot (BIOS/UEFI), Startup (carregamento de drivers e serviços) e Shutdown seguro do sistema.
* **Internals (Processos e Memória):** Diferenciação técnica entre Processos (instâncias de programas), Threads (unidades de execução) e Handles (referências a recursos do sistema).
* **Windows Registry:** Investigação das 5 Hives principais do Registro para identificar persistência de malware e configurações críticas do sistema.



### 3.3. CONFIGURAÇÃO E MONITORAMENTO PROATIVO
* **Gestão de Identidades:** Administração de usuários locais e de domínio, com foco no princípio do privilégio mínimo (Least Privilege) e uso do "Run as Administrator".
* **CLI & PowerShell:** Automação de tarefas de segurança e coleta de dados via terminal, utilizando o `net command` para gerenciar recursos de rede e sessões de usuário.
* **Instrumentação (WMI):** Uso do Windows Management Instrumentation para monitorar o estado do sistema e gerenciar componentes remotamente.
* **Monitoramento de Recursos:** Utilização estratégica do Task Manager e Resource Monitor para correlacionar picos de CPU/Memória com processos específicos (PIDs).

### 3.4. DEFESA ATIVA E SEGURANÇA (HARDENING)
* **Auditoria de Rede:** Aplicação do comando `netstat` para mapear portas abertas e conexões estabelecidas, essencial para detectar conexões de Comando e Controle (C2).
* **Análise Forense de Logs:** Investigação de eventos críticos no Event Viewer (Ex: Event ID 4624 para logons), permitindo o rastreamento de atividades suspeitas no sistema.
* **Hardening e Políticas:** Configuração de Local Security Policies para endurecimento da estação de trabalho e gestão rigorosa do Windows Update.
* **Defesa Nativa:** Configuração e monitoramento do Windows Defender Antivírus e do Firewall com segurança avançada para filtragem de tráfego.

---

## 🧪 LABS PRÁTICOS (FIELD REPORTS)

* **LAB 3.2.11:** Investigação profunda de processos ativos e manipulação de chaves no Registro do Windows.
* **LAB 3.3.10:** Criação e auditoria de contas de usuários locais via linha de comando.
* **LAB 3.3.11:** Automação de coleta de informações do sistema utilizando scripts em PowerShell.
* **LAB 3.3.13:** Gestão e monitoramento de recursos para identificação de gargalos e processos zumbis.

---

### 🛠️ Toolset Aplicado
* PowerShell & Windows CLI
* Regedit (Registry Editor)
* Event Viewer (Security Logs)
* Local Security Policy Editor
* Microsoft Resource Monitor
