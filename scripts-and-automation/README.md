# 🐍 Automação e Threat Intelligence (DevSec)

> **Missão:** Um analista de SOC de elite não se limita a operar *dashboards* construídos por terceiros; ele desenvolve as suas próprias ferramentas para acelerar a Resposta a Incidentes (IR) e proteger contra Riscos Digitais.

Esta secção do repositório materializa a união entre a engenharia de software e a cibersegurança. Aqui arquivo os *scripts* e ferramentas de linha de comandos (CLI) desenvolvidos para automatizar tarefas de segurança e testar os meus conhecimentos.

---

## 🛠️ O Arsenal (Ferramentas Desenvolvidas)

### 1. CyberOps CLI Quizzer (`cyberops_quizzer.py`)
Porquê utilizar aplicações genéricas de *flashcards* quando podes construir o teu próprio motor de estudo? 
* **Descrição:** Um *script* em Python desenvolvido do zero para testar os conhecimentos da certificação Cisco CBROPS. Ele consome uma base de dados JSON (`questoes_cbrops.json`), apresenta as questões de forma interativa no terminal, contabiliza a pontuação em tempo real e utiliza códigos de cor ANSI para *feedback* visual imediato.
* **Competências Demonstradas:** Manipulação de ficheiros JSON, interfaces de linha de comandos (CLI), lógica de programação e estudo ativo.

### 2. SSH Log Parser & Threat Intel (`log_parser_ssh.py`) 
* **Descrição:** Um *script* para dissecar ficheiros `/var/log/auth.log` de servidores Linux. O objetivo é identificar endereços IP com múltiplas falhas de autenticação (Força Bruta) e isolá-los automaticamente num relatório.
* **Competências Demonstradas:** Expressões Regulares (Regex), manipulação de *strings*, análise forense e automação de SOC (Tier 1).

### 3. API Hash Checker (`vt_hash_checker.py`) - *Em Breve*
* **Descrição:** Ferramenta que consome a API pública do VirusTotal para verificar automaticamente se uma lista de *hashes* (MD5/SHA-256) extraídos de um incidente corresponde a malwares conhecidos.
* **Competências Demonstradas:** Integração de APIs REST, pedidos HTTP (Requests) e Threat Intelligence.

---

## 🚀 Como testar o CyberOps Quizzer na tua máquina

1. Certifica-te de que tens o Python 3 instalado.
2. Clona este repositório.
3. Navega até esta pasta: `cd scripts-and-automation`
4. Executa o simulador: `python3 cyberops_quizzer.py`
