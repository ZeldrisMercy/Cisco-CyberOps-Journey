# 🐍 Python SOC Automations & Active Response

> **Missão:** Construir o próprio arsenal. Este diretório contém ferramentas desenvolvidas em Python para automatizar tarefas críticas de um Centro de Operações de Segurança (SOC), desde a verificação de integridade de arquivos até a resposta ativa contra intrusões (IPS).

A abordagem aqui é "Host-Based Analysis", operando diretamente nos logs do sistema e manipulando regras de firewall em tempo real.

---

## 🛠️ O Arsenal (Ferramentas de Defesa)

### 1. Integrity Scanner Pro (`hash_checker.py`) v3.0
* **Descrição:** Ferramenta forense para garantir a **Integridade** de evidências e binários. Utiliza leitura de arquivos em blocos de memória (`8192 bytes`), o que a torna extremamente eficiente para escanear arquivos pesados sem sobrecarregar a RAM.
* **Features Principais:**
  * Gera simultaneamente hashes MD5, SHA-1 e SHA-256.
  * **Modo Forense (Lote):** Varredura completa de diretórios iterando sobre todos os arquivos.
  * **Verificação de Adulteração:** Permite colar um hash oficial para comparação direta e validação de integridade.
* **Módulos Core:** `hashlib`, `os`.

### 2. SOC IPS Unit - Advanced (`soc_ips_blocker.py`)
* **Descrição:** Um sistema de Resposta Ativa (Active Response) com interface tática para terminal. O script disseca logs de autenticação para identificar ataques de Força Bruta e aplica bloqueios de rede.
* **Features Principais:**
  * **Regex Engine:** Extrai IPs maliciosos diretamente de strings de erro de senha (`Failed password for...`).
  * **Cross-Platform:** Executa bloqueios reais no firewall do Linux (`iptables`) ou Windows (`netsh`).
  * **Forense Automatizada:** No modo real, gera automaticamente um relatório tático em formato `.json` contendo a data, o IP atacante e o número de tentativas, preservando a cadeia de custódia.
  * **Modo de Simulação:** Permite testar a lógica e o parser sem alterar as regras reais do sistema.
* **Módulos Core:** `re`, `subprocess`, `json`, `collections.Counter`.

### 3. SSH Log Parser & Blocker (`log_parser_ssh.py`)
* **Descrição:** A versão base e focada em auditoria do bloqueador IPS. Focado na manutenção de logs de segurança e gestão simplificada.
* **Features Principais:**
  * **Sistema de Whitelist Interativo:** Permite adicionar IPs confiáveis (como `127.0.0.1`) em tempo de execução para evitar auto-bloqueio.
  * **Auditoria Contínua:** Utiliza a biblioteca `logging` para gravar silenciosamente todos os bloqueios executados em um arquivo `ips_bloqueados.log`.
* **Módulos Core:** `logging`, `platform`, `subprocess`.

### 4. CyberOps DB Quizzer (`cyberops_quizzer.py`)
* *(Documentação em breve: Simulador de estudos em terminal)*

---

## 🚀 Como Executar no Laboratório

**Pré-requisitos:** Python 3.10+ instalado no sistema host.

1. Clone o repositório e navegue até a pasta: `cd scripts-and-automation`
2. **Para verificação de arquivos:** * `python hash_checker.py` (Arraste o arquivo ou diretório para o terminal quando solicitado).
3. **Para executar o IPS (Requer permissão de Administrador/Sudo no Módulo Real):**
   * Certifique-se de que o arquivo de log `auth_test.log` existe no diretório (crie um com logs de teste para simulação).
   * `python soc_ips_blocker.py`

> ⚠️ **Aviso de Operação:** A opção "Módulo Real" nos scripts de IPS **fará alterações diretas no Firewall do seu Sistema Operacional**. Utilize com cautela e prefira o Módulo de Simulação durante os testes de desenvolvimento.
