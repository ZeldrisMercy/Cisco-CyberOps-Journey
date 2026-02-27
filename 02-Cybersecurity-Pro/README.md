# 📁 Module 02: Cybersecurity Professionals & SOC Operations

> [!NOTE]
> **Resumo Executivo:**
> Este módulo consolida a transição para a carreira de defensor de rede (Blue Team). O foco recai sobre a estrutura de um Centro de Operações de Segurança (SOC), o ciclo de vida de Resposta a Incidentes (NIST), o uso tático de SIEM/SOAR e as métricas operacionais que definem o sucesso na mitigação de riscos.

---

## 🏛️ A Estrutura de um SOC (O Tripé)

Uma operação de segurança eficiente depende do equilíbrio perfeito entre três pilares: **Pessoas, Processos e Tecnologias**.

### 1. Pessoas (Níveis de Analistas)
* **Tier 1 (Analista de Triagem):** Monitora a fila de alertas do SIEM. Valida se um alerta é um Falso Positivo ou um Incidente Real. Abre o ticket e isola a máquina temporariamente.
* **Tier 2 (Responder / Analista de IR):** Recebe o ticket escalonado pelo Tier 1. Faz a investigação profunda (Forense, Análise de Malware) e executa a contenção avançada e erradicação.
* **Tier 3 (Threat Hunter / SME):** Atua de forma **proativa**. Em vez de esperar um alerta do SIEM, ele caça ameaças ocultas (stealth) na rede buscando reduzir o *Dwell Time*.

### 2. Processos (NIST SP 800-61 r2)
Para a prova da Cisco, o ciclo de vida de Resposta a Incidentes segue estritamente o modelo NIST:
1. **Preparação:** Criar políticas, treinar a equipe, configurar backups e assinar ferramentas. (A fase mais importante).
2. **Detecção e Análise:** Onde o Tier 1 atua. Identificar o vetor, escopo e impacto através de IoCs (Indicadores de Comprometimento).
3. **Contenção, Erradicação e Recuperação:** * *Contenção:* Isolar o host da rede para o malware não se espalhar.
   * *Erradicação:* Remover o malware, deletar contas falsas.
   * *Recuperação:* Restaurar backups, religar o sistema e monitorar.
4. **Atividades Pós-Incidente (Lessons Learned):** Reunião para documentar o que falhou e como melhorar as defesas para o futuro.

### 3. Tecnologias (SIEM vs. SOAR)
* **SIEM (Security Information and Event Management):** O "Cérebro" passivo. Suas principais funções são:
  * **Agregação:** Coletar logs de firewalls, roteadores e Windows em um só lugar.
  * **Normalização:** Converter formatos de logs diferentes (ex: Syslog do Linux e Event ID do Windows) para um formato padrão legível.
  * **Correlação:** Ligar eventos isolados para descobrir um ataque (Ex: 5 falhas de login no VPN + 1 sucesso + 1 download massivo no File Server = Alerta de Risco).
* **SOAR (Security Orchestration, Automation, and Response):** O "Braço" ativo. Enquanto o SIEM apenas avisa, o SOAR executa ações automáticas (Runbooks) como bloquear um IP no firewall ou desabilitar um usuário no Active Directory via API.

---

## 📊 SOC Metrics (Métricas de Defesa)

Diferenciação crítica para análise de performance do time:
* **MTTD (Mean Time to Detect):** Tempo médio para *identificar* a intrusão.
* **MTTC (Mean Time to Contain):** Tempo médio para *conter* a ameaça (isolar o host).
* **MTTR (Mean Time to Respond/Recover):** Tempo médio para *conter, remediar e restaurar* o ambiente completamente.
* **Dwell Time:** O tempo que o inimigo permaneceu escondido na rede antes de ser detectado. A meta do Threat Hunter é zerar isso.

---

## 📑 Tactical Field Report: Lab Executions

* **[Lab 2.2.5 - Tornando-se um Defensor]:** * **Intel de Carreira:** Mapeamento de vagas de SOC via Glassdoor, identificando as certificações e qualificações reais exigidas pelo mercado.
  * **Treinamento Técnico (Legal Hacking):** Investigação da plataforma *Google Gruyere* para testes legais de habilidades. Compreender a mentalidade ofensiva (Red Team) é o primeiro passo para construir regras de detecção eficientes (Blue Team).

> [!TIP]
> **Visão de Mercado:** Profissionais que conseguem projetar defesas através de automação (DevSec) possuem um diferencial gigantesco nas seleções atuais, pois reduzem drasticamente o MTTC de um SOC.
