# 🐍 Automação e Threat Intelligence (DevSec)

> **Missão:** Um analista de SOC de elite não se limita a operar *dashboards* construídos por terceiros; ele desenvolve as suas próprias ferramentas para acelerar a Resposta a Incidentes (IR) e proteger contra Riscos Digitais.

Esta secção materializa a união entre a engenharia de software e a cibersegurança. Aqui arquivo os *scripts* desenvolvidos para automatizar tarefas de defesa e testar o meu progresso.

---

## 🛠️ O Arsenal (Ferramentas Desenvolvidas)

### 1. CyberOps CLI Quizzer (`cyberops_quizzer.py`) v3.1
* **Descrição:** Motor de estudo desenvolvido do zero que consome uma base de dados JSON (`questoes_cbrops.json`). Possui barra de progresso, sistema de "pular questão", modo de seleção por módulo e tratamento de codificação para maior resiliência.
* **Competências:** Manipulação de JSON, ANSI Colors, UX em Terminal e Estudo Ativo.

### 2. SOC IPS Unit: Active Response (`soc_ips_blocker.py`)
* **Descrição:** Ferramenta de **Resposta Ativa**. O script disseca logs de autenticação, identifica ataques de Força Bruta via Regex e oferece uma interface para bloqueio real no Firewall (Netsh/Iptables) com suporte a *Whitelists*.
* **Competências:** Regex, Integração com OS (Subprocess), Gestão de Firewall e Lógica de IPS.

### 3. File Integrity & Hash Checker (`hash_checker.py`)
* **Descrição:** Utilitário para garantir a **Integridade** (Tríade CIA). Calcula hashes SHA-256 de arquivos em blocos de memória, permitindo comparar binários suspeitos com hashes oficiais para detectar adulterações ou malwares disfarçados.
* **Competências:** Criptografia (Hashlib), Manipulação de Arquivos Binários e Forense Digital.

---

## 🚀 Como Executar

1. Certifique-se de que possui o Python 3.10+ instalado.
2. Navegue até a pasta: `cd scripts-and-automation`
3. Para o simulador: `python cyberops_quizzer.py`
4. Para o bloqueador (Modo Real exige Admin/Sudo): `python soc_ips_blocker.py`

---

### 🛰️ Transmissão de Entrada: Próximas Missões...
* [ ] **VT Threat Intel API:** Integração automática com VirusTotal para reputação de IPs detectados.
* [ ] **Log Dashboard:** Interface web para visualização gráfica das tentativas de invasão bloqueadas.
* [ ] **PCAP Auto-Analyzer:** Extração automática de metadados de arquivos de captura de rede.

**[!] Novas ferramentas e módulos de defesa serão descriptografados em breve...**
