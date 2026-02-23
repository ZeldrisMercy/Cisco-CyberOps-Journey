# 🛡️ Cisco CyberOps Associate: Journey

![Cisco](https://img.shields.io/badge/CISCO-044342?style=for-the-badge&logo=cisco&logoColor=white)
![Netacad](https://img.shields.io/badge/NETACAD-00BCEB?style=for-the-badge&logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-COMPLETED-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue?style=for-the-badge)

## 📁 Module 03: Windows Operating System

> [!NOTE]
> **Resumo Executivo:** Este módulo consolida o domínio técnico sobre a arquitetura do sistema operacional Windows, cobrindo desde a evolução histórica e vulnerabilidades estruturais até o monitoramento avançado de processos, rede e recursos. O foco foi capacitar o analista na identificação de anomalias e no endurecimento (hardening) do ambiente operacional.

---

## 📑 Tactical Field Report: Lab Executions

### 🔍 Identificação de Processos Ativos
**Referência:** *3.1.4 Class Activity - Identify Running Processes*

Monitoramento de conexões de rede e endpoints de software.

* **Endpoints de Rede:** Uso do TCP/UDP Endpoint Viewer (Sysinternals) para listar processos que possuem conexões ativas.
* **Processos de Sistema:** Identificação e localização de processos críticos como `lsass.exe` e `services.exe`.
* **Análise de Comportamento:** Observação da criação de novos endpoints ao iniciar navegadores (Microsoft Edge) e monitoramento de estados como LISTENING e ESTABLISHED.

### 🛡️ Investigação de Arquitetura e Registro
**Referência:** *3.2.11 Lab - Exploring Processes, Threads, Handles, and Windows Registry*

Exploração profunda dos componentes internos e base de dados de configuração.

* **Hierarquia de Execução:** Uso do Process Explorer para analisar a relação entre Processos, Threads e Handles.
* **Segurança de Processos:** Integração com VirusTotal para verificar a assinatura e integridade de arquivos do sistema.
* **Forense de Registro:** Manipulação de chaves HKEY_CURRENT_USER para entender como o sistema operacional processa aceites de licença (EULA) e configurações de persistência.

### 👤 Gerenciamento de Contas de Usuário
**Referência:** *3.3.10 Lab - Create User Accounts*

Implementação de políticas de acesso e isolamento de perfis.

* **Controle de Acesso:** Criação de contas de usuário locais e gerenciamento de grupos administrativos via Computer Management.
* **Isolamento NTFS:** Auditoria de permissões em diretórios de usuários para garantir que perfis padrão não acessem dados de administradores.

### 💻 Automação via PowerShell
**Referência:** *3.3.11 Lab - Using Windows PowerShell*

Utilização de shell avançado para coleta de dados e automação de tarefas.

* **Auditoria de Conexões:** Uso do comando `netstat -abno` para correlacionar portas abertas diretamente com executáveis e PIDs.
* **Cmdlets de Sistema:** Exploração de comandos como `Get-ChildItem` e `Clear-RecycleBin` para manutenção e investigação rápida via CLI.

### 📊 Monitoramento via Task Manager
**Referência:** *3.3.12 Lab - Windows Task Manager*

Gestão operacional de aplicações, serviços e performance de hardware.

* **Gestão de Apps:** Monitoramento de categorias de processos (Apps, Background, Windows processes) e finalização forçada de tarefas.
* **Performance Intel:** Análise de utilização de CPU, Memória, Disco e Ethernet em tempo real.
* **Resource Monitoring:** Uso do Resource Monitor para identificar threads ativos e tempo de resposta de escrita em disco.

### 📈 Gestão de Recursos e Serviços
**Referência:** *3.3.13 Lab - Monitor and Manage System Resources in Windows*

Auditoria de serviços e criação de logs de desempenho.

* **Controle de Serviços:** Início e interrupção de serviços como "Routing and Remote Access" e observação de mudanças em adaptadores de rede.
* **Data Collector Sets:** Criação de logs manuais no Performance Monitor para capturar dados de performance (CSV) para análise posterior.
* **Event Logging:** Investigação de logs de sistema (Event ID 7040) no Event Viewer para rastrear mudanças de configuração.

---

### 🔬 Tactical Insights & Aprendizado Crítico

* **Visibilidade Holística:** O uso conjunto de CLI, Sysinternals e Ferramentas Administrativas fornece ao Blue Team a visibilidade necessária para detectar desde malwares simples até ameaças persistentes avançadas.
* **Hardening Proativo:** A desativação de serviços desnecessários e o monitoramento rigoroso do registro são passos fundamentais para reduzir a superfície de ataque no Windows.
* **Cultura de Auditoria:** O entendimento de Event IDs e logs de performance permite a reconstrução de incidentes de forma precisa durante uma resposta a intrusão.

---
**Analista Responsável:** Ícaro de Souza Mariano  
**Data do Relatório:** 23/02/2026
