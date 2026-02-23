# 🛡️ LEVEL 3: THE WINDOWS FORTRESS (SYSTEM HARDENING)

![CISCO](https://img.shields.io/badge/CISCO-NETACAD-orange) ![STATUS](https://img.shields.io/badge/STATUS-COMPLETED-green) ![FOCUS](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue)

## 📊 PROGRESSO DA MISSÃO

* **Módulo 3.1: Windows History** — Status: 100% Concluído
* **Módulo 3.2: Windows Architecture and Operations** — Status: 100% Concluído
* **Módulo 3.3: Windows Configuration and Monitoring** — Status: 100% Concluído
* **Módulo 3.4: Windows Security** — Status: 100% Concluído

---

## ⚔️ SKILL TREE (HABILIDADES DESBLOQUEADAS)

### 3.1. EVOLUÇÃO E FUNDAMENTOS DO SO
* **Histórico e Vulnerabilidades:** Compreensão da evolução do MS-DOS para a arquitetura NT. Análise de como a herança de sistemas legados e a complexidade da GUI introduzem vetores de ataque e vulnerabilidades de dia zero.

### 3.2. ARQUITETURA E OPERAÇÕES INTERNAS (THE CORE)
* **Modos de Execução (Kernel vs. User):** Estudo da separação de privilégios onde o Kernel Mode possui acesso total ao hardware e a HAL isola o software das complexidades do hardware.
* **Sistemas de Arquivos e ADS:** Exploração do NTFS e a técnica de **Alternate Data Streams (ADS)**, utilizada para ocultar arquivos ou metadados sem alterar o tamanho visível do arquivo.
* **Workflow de Sistema:** Análise detalhada das etapas de Boot (BIOS/UEFI), Startup (carregamento de drivers/serviços) e Shutdown seguro.
* **Internals (Processos e Memória):** Diferenciação técnica entre Processos, Threads e Handles.
* **Windows Registry:** Investigação das 5 Hives do Registro para identificar persistência de malware.



### 3.3. CONFIGURAÇÃO E MONITORAMENTO PROATIVO
* **Gestão de Identidades:** Administração de usuários locais e de domínio sob o princípio do privilégio mínimo.
* **CLI & PowerShell:** Automação de tarefas de segurança e uso do `net command` para gerenciar sessões e recursos.
* **Monitoramento de Recursos:** Uso do Task Manager e Resource Monitor para análise de processos ativos (PIDs).

### 3.4. DEFESA ATIVA E SEGURANÇA (HARDENING)
* **Auditoria de Rede:** Uso do `netstat` para mapear conexões e detectar atividade de Comando e Controle (C2).
* **Análise Forense de Logs:** Investigação de eventos críticos no Event Viewer para rastreamento de intrusões.
* **Hardening:** Configuração de Local Security Policies e defesa nativa via Windows Defender e Firewall.

---

## 🧪 LABS PRÁTICOS (FIELD REPORTS)

* **LAB 3.1.4 - Identify Running Processes:** Uso de ferramentas como o TCP/UDP Endpoint Viewer para identificar conexões ativas e localizar arquivos de sistema como `lsass.exe`.
* **LAB 3.2.11 - Internals Investigation:** Exploração de processos, threads e handles com Process Explorer, além da manipulação de chaves do Registro (EULA) para entender persistência.
* **LAB 3.3.10 - User Management:** Criação e auditoria de contas locais, validando o isolamento de perfis e privilégios administrativos.
* **LAB 3.3.11 - PowerShell Automation:** Execução de auditorias de rede com `netstat -abno` e automação de limpeza de recursos.
* **LAB 3.3.12 - Task Manager Ops:** Gerenciamento de processos em background e análise detalhada de performance de hardware.
* **LAB 3.3.13 - Resource & Service Management:** Criação de Data Collector Sets no Performance Monitor e auditoria de serviços (Event ID 7040).

---

### 🛠️ Toolset Aplicado
* PowerShell & Windows CLI
* Regedit (Registry Editor)
* Event Viewer (Security Logs)
* Local Security Policy Editor
* Microsoft Resource Monitor & Performance Monitor
* Sysinternals Suite (Process Explorer, TCPView)

---

*Documentação mantida por **Ícaro de Souza Mariano** | Especialista em Formação*
