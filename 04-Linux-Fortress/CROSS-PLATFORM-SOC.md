# ⚖️ Estratégia Multiplataforma: Windows vs. Linux

> [!IMPORTANT]
> **Visão Tática (Blue Team):** O verdadeiro diferencial de um analista de SOC moderno é a capacidade de transitar fluidamente entre ecossistemas híbridos. Esta seção sintetiza as diferenças fundamentais de arquitetura, segurança e administração exploradas nos Módulos 3 e 4.

## 🏛️ Comparativo de Arquitetura e Defesa


Abaixo, o contraste de como cada sistema operacional aborda os mesmos desafios de segurança de endpoint:

| Característica Operacional | 🛡️ Windows (Module 03) | ⚔️ Linux (Module 04) |
| :--- | :--- | :--- |
| **Arquitetura de Configuração** | Baseada no **Registro (Hives)**. Centralizada e hierárquica (HKLM, HKCU). | Baseada em **Arquivos de Texto** planos (geralmente no `/etc`). Descentralizada. |
| **Interface Primária** | Orientada a **GUI** (Event Viewer, Task Manager) e ferramentas administrativas (PowerShell/WMI). | Orientada a **CLI** nativa (Bash, Nano, Grep) e encadeamento via Pipes (`|`). |
| **Gestão e Isolamento de Processos** | Foco em Processos, Threads e **Handles** (ponteiros de acesso a recursos e memória). | Foco em Processos e **Forking** (processo pai clonando processos filhos). |
| **Visibilidade de Conexões (Rede)** | Uso de Sysinternals (**TCPView**) e do comando nativo `netstat -abno`. | Uso intensivo de **`netstat -tunap`**, utilitário `ss` e auditoria ativa via Telnet/Curl. |
| **Motor de Auditoria (Logs)** | **Event Viewer** (Monitoramento via Event IDs específicos, ex: 4624, 4688). | **Syslog** (arquivos estáticos em `/var/log/`) e o daemon moderno **Journalctl** (`systemd`). |
| **Controle de Acesso e Permissões** | **NTFS** (Permissões cumulativas, listas de herança e Grupos de Domínio). | Permissões estritas em Octal (**rwx**) e gestão direta de propriedade e Inodes. |

## 🔬 Conclusão Estratégica para Resposta a Incidentes

A abordagem de caça a ameaças (Threat Hunting) muda drasticamente dependendo do host sob investigação:

* **Windows Insights:** O adversário foca em ocultação e abuso de recursos legítimos (Living off the Land). Ele usará Alternate Data Streams (ADS) para esconder arquivos, tentará injetar código no `lsass.exe` para roubar credenciais na memória e usará scripts PowerShell para evitar tocar no disco rígido. A defesa exige monitoramento afiado das chaves de Registro (busca por persistência) e o uso contínuo da suíte Sysinternals para auditar assinaturas digitais de processos.
* **Linux Insights:** A filosofia de que "tudo é um arquivo" permite que a equipe de defesa automatize e escale investigações de forma impressionante. O adversário tentará modificar binários essenciais instalando Rootkits, procurará alterar o `/etc/shadow` ou garantirá persistência alterando o `.bashrc` ou os serviços via `systemd`. A defesa exige domínio absoluto de expressões regulares e ferramentas de texto (`grep`, `awk`, `sed`) para extrair Indicadores de Comprometimento (IoCs) de gigantescos arquivos de texto plano de forma cirúrgica.
