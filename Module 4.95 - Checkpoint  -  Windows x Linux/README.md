---

## 🏛️ Estratégia Multiplataforma: Windows vs. Linux

Esta seção sintetiza as diferenças fundamentais de segurança e administração exploradas nos Módulos 3 e 4, consolidando o conhecimento necessário para um analista de SOC atuar em ambientes híbridos.

| Característica | 🛡️ Windows (Module 03) | ⚔️ Linux (Module 04) |
| :--- | :--- | :--- |
| **Arquitetura de Configuração** | Baseada em **Registro do Windows** (Hives). | Baseada em **Arquivos de Texto** planos (geralmente em `/etc`). |
| **Interface Primária** | Orientada a **GUI** (Task Manager, Event Viewer). | Orientada a **CLI** (Bash, Nano, Grep, Pipes). |
| **Gestão de Processos** | Foco em Processos, Threads e **Handles**. | Foco em Processos e **Forks** (Parent/Child). |
| **Visibilidade de Rede** | Ferramentas como **TCPView** e Netstat. | Uso intensivo de **Netstat** e auditoria via **Telnet**. |
| **Monitoramento de Eventos** | **Event Viewer** (Logs de Sistema/Segurança). | **Syslog** (`/var/log/`) e **Journalctl** (`systemd`). |
| **Controle de Acesso** | NTFS e Grupos Administrativos locais. | Permissões **rwx** (Octal) e gestão de Inodes. |

### 🔬 Conclusão Tática

O domínio de ambos os sistemas é o diferencial de um especialista em **Blue Team**. Enquanto o Windows exige atenção à integridade do registro e processos camuflados, o Linux demanda maestria na linha de comando e rapidez na análise de logs para detectar movimentações laterais.

* **Windows Insights:** A visibilidade através da suíte Sysinternals é vital para detectar ameaças que tentam se ocultar em processos nativos.
* **Linux Insights:** A filosofia de que "tudo é um arquivo" permite automatizar investigações complexas através do encadeamento (piping) de comandos.

---

**Analista Responsável:** Ícaro de Souza Mariano  
**Status da Certificação:** Em Progresso (CCNA / CyberOps)
