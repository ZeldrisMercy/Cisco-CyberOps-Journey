## 📁 Module 04: Linux Operating System

> [!NOTE]
> **Resumo Executivo:** Este módulo estabelece o domínio operacional sobre o sistema Linux, com ênfase em distribuições voltadas para segurança (CyberOps Workstation/Arch Linux). [cite_start]O foco foi capacitar o analista na navegação via CLI, administração de serviços, manipulação de sistemas de arquivos, permissões granulares e o uso forense de logs e ferramentas de detecção de rootkits[cite: 619, 628, 921, 1772].

---

## 📑 Tactical Field Report: Lab Executions

### ⌨️ Operações de Texto e Configuração
**Referência:** *4.2.6 Lab - Working with Text Files in the CLI*

Domínio de editores e customização do ambiente operacional.

* [cite_start]**Editores de Texto:** Uso de editores gráficos como o SciTE e de linha de comando como o GNU nano para manipulação de arquivos de sistema[cite: 1350, 1400].
* [cite_start]**Customização de Shell:** Edição do arquivo oculto `.bashrc` para modificar variáveis de ambiente e a estrutura visual do prompt (PS1)[cite: 1530, 1538, 1584].
* [cite_start]**Ajuste de Serviços:** Reconfiguração do servidor web Nginx através de arquivos de configuração customizados, alterando portas de escuta (ex: TCP 8080) e diretórios raiz[cite: 1730, 1732, 1733].

### 🐚 Fundamentos e Gestão via Shell
**Referência:** *4.2.7 Lab - Getting Familiar with the Linux Shell*

Gerenciamento de arquivos, pastas e fluxos de dados via terminal.

* [cite_start]**Manipulação de Diretórios:** Uso de `mkdir`, `cd` e `ls -la` para criar, navegar em estruturas complexas e identificar arquivos ocultos (dot-files)[cite: 1796, 1813, 1914, 1928].
* [cite_start]**Fluxo de Dados:** Aplicação de operadores de redirecionamento (`>` e `>>`) para extrair saídas de comandos e gerar relatórios em arquivos de texto[cite: 1878, 1886, 1906].
* [cite_start]**Manutenção de Arquivos:** Execução de operações de cópia (`cp`), movimentação (`mv`) e deleção recursiva (`rm -r`) para organização e limpeza do ambiente[cite: 1938, 1971, 1985].

### 🕵️ Monitoramento de Servidores e Processos
**Referência:** *4.3.4 Lab - Linux Servers*

Identificação de serviços ativos e análise de sockets de rede.

* [cite_start]**Auditoria de Processos:** Uso de `ps -elf` e `ps -ejH` para mapear a hierarquia de execução e identificar daemons rodando em background[cite: 26, 37, 49].
* [cite_start]**Análise de Rede:** Utilização do `netstat -tunap` para correlacionar portas abertas (Listening) com seus respectivos Process IDs (PIDs)[cite: 59, 72, 82].
* [cite_start]**Banner Grabbing:** Uso do Telnet para conectar em portas específicas (como 80 ou 22) para testar a disponibilidade e extrair informações de versão de serviços[cite: 106, 114, 148, 155].

### 📂 Investigação Forense de Logs
**Referência:** *4.4.4 Lab - Locating Log Files*

Rastreamento de eventos e monitoramento de atividades em tempo real.

* [cite_start]**Análise de Mensagens:** Investigação do arquivo `/var/log/messages` para identificar eventos críticos de kernel e hardware[cite: 227, 229, 273].
* [cite_start]**Logs de Aplicação:** Dissecação de logs de acesso do Nginx para rastrear conexões de clientes e erros de requisição[cite: 444, 487, 606].
* [cite_start]**Monitoramento Ativo:** Uso de `tail -f` para seguir entradas de log instantaneamente e `journalctl` para consultas avançadas e filtragem de logs do sistema[cite: 521, 631, 632, 827].

### 🛡️ Arquitetura de Arquivos e Permissões
**Referência:** *4.5.4 Lab - Navigating the Linux Filesystem and Permission Settings*

Hardening de privilégios e gestão de dispositivos de bloco.

* [cite_start]**Gestão de Montagem:** Identificação de dispositivos via `lsblk` e montagem manual de partições físicas em pontos de montagem lógicos[cite: 934, 938, 1017].
* [cite_start]**Controle de Acesso:** Alteração granular de permissões via `chmod` (formato octal) e transferência de propriedade de arquivos com `chown`[cite: 1078, 1104, 1111].
* [cite_start]**Links de Sistema:** Criação e teste de Symbolic Links (`ln -s`) e Hard Links, compreendendo o impacto de alterações estruturais nos arquivos originais[cite: 1202, 1279, 1288, 1323].

---

### 🔬 Tactical Insights & Aprendizado Crítico

* [cite_start]**O Poder da CLI:** No Linux, a linha de comando é a ferramenta definitiva para administração remota via SSH, permitindo o gerenciamento eficiente de servidores que não possuem interface gráfica[cite: 1394, 1397, 1400, 1773].
* [cite_start]**Visibilidade de Logs:** O diretório `/var/log` e utilitários como `journalctl` são essenciais para investigações, pois permitem a correlação precisa de timestamps entre diferentes fontes de eventos[cite: 225, 631, 910, 913].
* [cite_start]**Segurança de Host:** O controle rigoroso de permissões (`rwx`) e ownership é a primeira linha de defesa contra movimentações laterais e acesso não autorizado a dados sensíveis[cite: 1048, 1049, 1326].

---
**Analista Responsável:** Ícaro de Souza Mariano  
**Data do Relatório:** 26/02/2026
