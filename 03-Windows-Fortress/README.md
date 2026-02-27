# 📁 Module 03: Windows Operating System & Host-Based Analysis

> [!NOTE]
> **Resumo Executivo:** Este módulo mapeia a arquitetura interna do SO Windows, vulnerabilidades estruturais e monitoramento avançado. O foco tático é capacitar o analista (Blue Team) a identificar anomalias, auditar logs e realizar o *hardening* do endpoint, cobrindo 100% dos requisitos do Domínio 3.0 do exame CBROPS 200-201.

---

## 🏛️ Windows Internals (A Arquitetura Central)

### 1. Modos de Execução e Memória
* **User Mode (Ring 3):** Onde correm as aplicações comuns. O acesso ao hardware é restrito.
* **Kernel Mode (Ring 0):** Possui acesso total ao hardware. Se um driver falha aqui, o sistema colapsa (BSOD). Malwares avançados (Rootkits) procuram este nível para obter invisibilidade.
* **Virtual Address Space:** Cada processo no Windows recebe o seu próprio espaço de endereço virtual. O Windows cria um conjunto de endereços de memória virtuais que mapeiam para a memória física, isolando os processos.

### 2. A Tríade de Execução
* **Processos:** Um contentor de recursos (ex: `chrome.exe`). Cada processo tem um PID único.
* **Threads:** A unidade básica de execução dentro de um processo.
* **Handles:** Um ponteiro que permite que um processo aceda a um recurso do sistema de forma controlada (um ficheiro, uma porta, etc.).

---

## 💀 Anatomia da Evasão: Case Study "Alternate Data Streams (ADS)"

O sistema de ficheiros NTFS possui o **ADS (Alternate Data Streams)**, originalmente criado para compatibilidade com sistemas antigos da Apple. No entanto, é amplamente abusado por adversários para evasão de defesas. O ADS permite anexar fluxos de dados ocultos a um ficheiro legítimo sem alterar o tamanho visível no Windows Explorer.

### 🧪 Análise Prática (Simulação de Ameaça)
O teste prático de ofuscação que realizei demonstrou como dados críticos e binários podem desaparecer da vista de um utilizador comum e até de soluções antivírus baseadas em assinaturas estáticas.

* **Fase 1: Ocultação de Texto (Exfiltração/Persistência):** Criação de um fluxo de dados oculto contendo a string `SENHA_ULTRA_SECRETA_123` dentro de um ficheiro de texto inofensivo.
  * *Comando de Execução:* `echo "SENHA_ULTRA_SECRETA_123" > relatorio.txt:secreto.txt`
* **Fase 2: Ocultação de Binário Malicioso:**
  Ocultação de um payload simulado (`TROJAN_V8.exe`) atrás de um documento comum.
  * *Comando de Execução:* `type TROJAN_V8.exe > relatorio.pdf:trojan.exe`

### 🛡️ Táticas de Detenção e Limitações (Blue Team)
O ADS não é autónomo. O fluxo oculto não se executa sozinho; necessita de um gatilho externo (uma "Logic Bomb", um script PowerShell, ou chamadas via WMI/WMIC) para extrair e executar o binário escondido.

**Como o SOC deteta e erradica a ameaça?**
1. **CLI Clássica:** O comando `dir` normal não mostra o ficheiro. É obrigatório utilizar `dir /r` no prompt de comando para listar os fluxos anexados.
2. **PowerShell Avançado:** O cmdlet `Get-Item -Stream * relatorio.txt` revela todos os fluxos de dados (streams) associados ao ficheiro.
3. **Sysinternals (O Padrão Ouro):** A ferramenta `streams.exe` (da suite Sysinternals da Microsoft) permite não só detetar, mas também apagar os fluxos maliciosos em massa numa diretoria, sem destruir o ficheiro original (`streams -d relatorio.txt`).

> [!WARNING]
> **Vulnerabilidade Arquitetural:** O ADS é uma funcionalidade exclusiva do NTFS. Se o atacante tentar exfiltrar o ficheiro para uma pen USB formatada em FAT32 ou transferi-lo via rede (HTTP/FTP para um servidor Linux), o fluxo oculto (e o malware) perde-se. É uma técnica estritamente de *permanência local*.

---

## 🛡️ Defesa de Endpoint e Hardening

A Cisco exige a compreensão das estratégias de defesa focadas no host.

### 1. Abordagens de Proteção
* **Agent-based (Com Agente):** Requer a instalação de um software diretamente no Windows (ex: Antivírus, Cisco Secure Endpoint). Coleta dados em tempo real, mas consome recursos da máquina local.
* **Agentless (Sem Agente):** A proteção é feita pela rede ou hipervisor. Tem menor custo de manutenção e impacto zero na performance do endpoint, mas menor visibilidade de processos internos.

### 2. Controlo de Aplicações
* **Blacklisting:** Bloqueia o que é sabidamente mau (ex: lista de hashes de malwares). Falha redondamente contra *Zero-Days*.
* **Whitelisting:** Abordagem "Zero Trust". Bloqueia tudo por defeito e permite correr apenas o explicitamente aprovado pelo administrador de sistemas.

### 3. Systems-Based Sandboxing
Ferramentas de *Sandboxing* criam um ambiente virtual altamente isolado onde ficheiros suspeitos (como aquele `relatorio.pdf:trojan.exe`) podem ser abertos (detonação de malware) de forma segura, sem risco de infetar o sistema operativo real e permitindo a recolha de *Indicadores de Comprometimento (IoCs)*.

---

## 🔍 O Arsenal de Auditoria: Registo e Eventos

* **Windows Registry (Registo do Windows):** O banco de dados de configuração. A chave `HKEY_LOCAL_MACHINE (HKLM)` afeta o sistema e todos os utilizadores. Malwares alteram subchaves como `\CurrentVersion\Run` para persistência.
* **Event Viewer (IDs Críticos para o Exame e para o SOC):**
  * `Event ID 4624`: Logon com sucesso.
  * `Event ID 4625`: Falha de logon (Múltiplas tentativas indicam Força Bruta / Password Spraying).
  * `Event ID 4688`: Um novo processo foi criado (Vital para rastrear execuções originadas de scripts que chamam um ficheiro oculto em ADS).
  * `Event ID 1102`: O log de auditoria foi limpo (Sinal clássico de encobrimento de rastos após a invasão).

---

## 📑 Tactical Field Report: Lab Executions

* **[Lab - Identify Running Processes]:** Uso do comando `netstat -abno` para listar ligações TCP ativas, as suas portas, e o executável (com PID) atrelado a elas.
* **[Lab - Sysinternals Suite]:** Uso do *Process Explorer* para validar assinaturas digitais de imagens do Windows, identificando malwares camuflados sob o nome de processos legítimos do sistema (como `svchost.exe`).
