# 🐍 Python SOC Automations & Active Response

> **Missão:** Construir o próprio arsenal. Este diretório contém ferramentas desenvolvidas em Python para automatizar tarefas críticas de um Centro de Operações de Segurança (SOC), desde a inteligência de ameaças global até a resposta ativa contra intrusões (IPS).

A abordagem aqui une **Host-Based Analysis** (análise interna) com **Threat Intelligence** (análise externa), criando uma camada de defesa proativa.

---

## 🛠️ O Arsenal (Ferramentas de Defesa)

### 1. CyberOps Threat Intelligence (`soc_threat_intel.py`) 🚀 **NEW**

**Descrição:**  
O **"olho externo" do SOC**. Este script atua como um conector entre o tráfego de rede e bases globais de reputação de IPs.

**Features Principais:**

- **Integração AbuseIPDB:** Consulta em tempo real o score de risco e país de origem de IPs suspeitos.
- **Gateway Integration:** Envia automaticamente ameaças confirmadas para o **Java-Sec-API** via requisições REST (JSON).
- **Notificação em Tempo Real:** Dispara alertas via Telegram quando IPs de alto risco são detectados.

**Módulos Core:**  
`requests`, `python-dotenv`

---

### 2. Integrity Scanner Pro (`hash_checker.py`) v3.0

**Descrição:**  
Ferramenta forense para garantir a **Integridade** de evidências e binários.

Utiliza leitura em blocos (`8192 bytes`) para máxima eficiência no processamento de arquivos grandes.

**Features Principais:**

- Geração simultânea de hashes **MD5**
- Geração de hashes **SHA-1**
- Geração de hashes **SHA-256**
- Comparação direta com hashes oficiais para validação de integridade

**Módulos Core:**  
`hashlib`, `os`

---

### 3. SOC IPS Unit - Advanced (`soc_ips_blocker.py`)

**Descrição:**  
Sistema de **Resposta Ativa (Active Response)**.

O script analisa logs de autenticação para identificar padrões de **ataques de força bruta** e aplica bloqueios automáticos no firewall do sistema.

Dependendo do sistema operacional, ele utiliza:

- `iptables` (Linux)
- `netsh` (Windows)

**Módulos Core:**  
`re`, `subprocess`, `json`, `collections.Counter`

---

### 4. SSH Log Parser & Blocker (`log_parser_ssh.py`)

**Descrição:**  
Ferramenta focada em **auditoria e análise de logs SSH**.

Inclui um sistema de **Whitelist interativo** que impede o bloqueio acidental de administradores legítimos.

Ideal para ambientes de laboratório ou servidores expostos à internet.

**Módulos Core:**  
`logging`, `platform`

---

## 🚀 Como Executar no Laboratório

### Pré-requisitos

- **Python 3.10 ou superior**
- Dependências instaladas via `pip`

`pip install requests python-dotenv`

---

### 1️⃣ Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto contendo as seguintes variáveis:

`ABUSEIPDB_API_KEY=your_api_key`  
`TELEGRAM_TOKEN=your_bot_token`  
`TELEGRAM_CHAT_ID=your_chat_id`

---

### 2️⃣ Executar o Módulo de Threat Intelligence

`python soc_threat_intel.py`

Este módulo consulta bases externas de reputação e envia alertas em tempo real.

---

### 3️⃣ Executar o IPS (Requer privilégios de Administrador)

`python soc_ips_blocker.py`

O script analisará logs de autenticação e bloqueará automaticamente IPs maliciosos detectados.

---

## ⚠️ Aviso de Operação

A opção **"Módulo Real"** presente nos scripts de IPS altera diretamente as regras do **Firewall do sistema operacional**.

Para testes em laboratório ou desenvolvimento, recomenda-se utilizar o:

**Modo de Simulação**

Esse modo permite validar a lógica de detecção e resposta **sem modificar regras reais do firewall**.
