# 📁 Module 03: Windows Operating System & Host-Based Analysis

> [!NOTE]
> **Resumo Executivo:** Este módulo mapeia a arquitetura interna do SO Windows, vulnerabilidades estruturais e monitoramento avançado. O foco tático é capacitar o analista (Blue Team) a identificar anomalias, auditar logs e realizar o *hardening* do endpoint, cobrindo 100% dos requisitos do Domínio 3.0 do exame CBROPS 200-201.

---

## 🏛️ Windows Internals (A Arquitetura Central)



### 1. Modos de Execução e Memória
* **User Mode (Ring 3):** Onde rodam as aplicações comuns. O acesso ao hardware é restrito.
* **Kernel Mode (Ring 0):** Possui acesso total ao hardware. Se um driver falha aqui, o sistema colapsa (BSOD). Malwares avançados (Rootkits) buscam este nível para obter invisibilidade.
* **Virtual Address Space:** Cada processo no Windows recebe seu próprio espaço de endereço virtual. Isso significa que o Windows cria um conjunto de endereços de memória virtuais que mapeiam para a memória física que aquele processo tem permissão para usar. Isso isola os processos, impedindo que um programa acesse a memória do outro.

### 2. A Tríade de Execução
* **Processos:** Um contêiner de recursos (ex: `chrome.exe`). Cada processo tem um PID único.
* **Threads:** A unidade básica de execução dentro de um processo.
* **Handles:** Um ponteiro que permite que um processo acesse um recurso do sistema de forma controlada (um arquivo, uma porta, etc.).

### 3. NTFS e Ocultação de Malware
O NTFS possui o **ADS (Alternate Data Streams)**. O ADS permite anexar fluxos de dados ocultos a um arquivo legítimo sem alterar o tamanho visível do arquivo principal. Adversários usam isso para esconder malwares dentro de arquivos de texto (`arquivo.txt:malware.exe`).

---

## 🛡️ Defesa de Endpoint e Hardening

A Cisco cobra o entendimento das estratégias de defesa focadas no host.

### 1. Abordagens de Proteção
* **Agent-based (Com Agente):** Requer a instalação de um software (agente) diretamente no Windows (ex: Antivírus, Cisco AMP). Vantagem: Coleta dados em tempo real e inspeciona processos locais profundamente. Desvantagem: Consome recursos do host.
* **Agentless (Sem Agente):** A proteção é feita pela rede ou hipervisor, sem instalar nada na máquina. Vantagem: Menor custo de manutenção e zero impacto na performance do host. Desvantagem: Menos visibilidade de processos internos.

### 2. Controle de Aplicações
* **Blacklisting:** Bloqueia apenas o que é sabidamente ruim (ex: hashes de malwares conhecidos). Se a ameaça for um *Zero-Day*, ela passará.
* **Whitelisting:** Abordagem "Zero Trust". Bloqueia tudo por padrão e permite rodar apenas o que o administrador aprovar explicitamente. É muito mais seguro.

### 3. Systems-Based Sandboxing
Ferramentas de *Sandboxing* (caixa de areia) criam um ambiente virtual altamente isolado onde arquivos suspeitos podem ser abertos (detonação de malware) de forma segura, sem risco de infectar o sistema operacional real.

---

## 🔍 O Arsenal de Auditoria: Registro e Eventos



* **Windows Registry:** O banco de dados de configuração. A chave `HKEY_LOCAL_MACHINE (HKLM)` afeta o sistema e todos os usuários. A chave `HKEY_CURRENT_USER (HKCU)` afeta apenas o usuário logado. Malwares alteram as subchaves `\CurrentVersion\Run` para persistência.
* **Event Viewer (IDs que caem na prova):**
  * `Event ID 4624`: Logon com sucesso.
  * `Event ID 4625`: Falha de logon (Força Bruta).
  * `Event ID 4688`: Um novo processo foi criado (Vital para rastrear malwares sendo iniciados).
  * `Event ID 1102`: O log de auditoria foi limpo (Sinal clássico de atacante tentando apagar seus rastros).

---

## 📑 Tactical Field Report: Lab Executions

* **[Lab - Identify Running Processes]:** Uso do comando `netstat -abno` para listar conexões TCP, suas portas, e o executável (com PID) atrelado a elas.
* **[Lab - Sysinternals Suite]:** Uso do *Process Explorer* para validar assinaturas digitais de imagens do Windows, identificando malwares camuflados de `svchost.exe`.
