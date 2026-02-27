# 🐍 Automação e Threat Intelligence (DevSec)

> **Missão:** Um analista de SOC de elite não se limita a operar *dashboards* construídos por terceiros; ele desenvolve as suas próprias ferramentas para acelerar a Resposta a Incidentes (IR) e proteger contra Riscos Digitais.

Esta secção materializa a união entre a engenharia de software e a cibersegurança. Aqui arquivo os *scripts* desenvolvidos para automatizar tarefas de defesa e testar o meu progresso.

---

## 🛠️ O Arsenal (Ferramentas Desenvolvidas)

### 1. CyberOps CLI Quizzer (`cyberops_quizzer.py`) v3.1
* **Descrição:** Motor de estudo desenvolvido do zero que consome uma base de dados JSON. Possui barra de progresso, sistema de "pular questão", modo de seleção por módulo e tratamento de codificação `utf-8-sig` para maior resiliência.
* **Competências:** Manipulação de JSON, ANSI Colors, UX em Terminal e Estudo Ativo.

### 2. SOC IPS Unit: Active Response (`soc_ips_blocker.py`)
* **Descrição:** Ferramenta de **Resposta Ativa**. O script disseca logs de autenticação (SSH), identifica ataques de Força Bruta via Regex e oferece uma interface para bloqueio real no Firewall (Netsh/Iptables) com suporte a *Whitelists*.
* **Competências:** Regex, Integração com OS (Subprocess), Gestão de Firewall e Lógica de IPS.

### 3. File Integrity & Hash Checker (`hash_checker.py`) v3.0
* **Descrição:** Utilitário para garantir a **Integridade** (Tríade CIA). Calcula hashes SHA-256 de arquivos em blocos de memória (eficiente para arquivos grandes), permite comparação com hashes oficiais e possui modo de **Escaneamento em Lote** para diretórios inteiros.
* **Competências:** Criptografia (Hashlib), Manipulação de Arquivos Binários, Forense Digital e Otimização de I/O.

---

## 🚀 Como Executar

1. Certifique-se de que possui o Python 3.10+ instalado.
2. Navegue até a pasta: `cd scripts-and-automation`
3. Para o simulador: `python cyberops_quizzer.py`
4. Para o bloqueador (Modo Real exige Admin/Sudo): `python soc_ips_blocker.py`
5. Para o verificador de integridade: `python hash_checker.py`

---

### 🛰️ Transmissão de Entrada: Próximas Missões...

* [ ] **FIM (File Integrity Monitoring) Watchdog:** Implementação de vigilância em tempo real utilizando eventos do Kernel para detectar e calcular hashes de novos arquivos instantaneamente.
* [ ] **VT Threat Intel API:** Integração automática com a API do VirusTotal para reputação global de hashes suspeitos e IPs detectados.
* [ ] **Log Dashboard:** Interface visual para monitoramento gráfico de tentativas de invasão e telemetria de bloqueios ativos.
* [ ] **PCAP Auto-Analyzer:** Scripts para extração automática de metadados de capturas de rede (.pcap).

**[!] Novas ferramentas e módulos de defesa serão descriptografados em breve...**
