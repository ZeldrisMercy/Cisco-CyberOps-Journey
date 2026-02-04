# 🛡️ Cisco CyberOps Associate: Journey

![Cisco](https://img.shields.io/badge/Cisco-NetAcad-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Blue_Team-blue?style=for-the-badge)

## 📂 Module 01: The Danger

> [!NOTE]
> **Resumo Executivo:**
> Este módulo fundamenta o vocabulário tático de um analista SOC, dissecando a anatomia de ataques, perfis de ameaça e o impacto financeiro/legal de vazamentos de dados.

---

## 💀 Anatomia de um Ataque: Case Study "Aupticon"
**Referência:** *1.1.4 Anatomia de um Ataque*

Análise técnica do incidente envolvendo espionagem industrial e sabotagem contra a empresa Aupticon.

> [!IMPORTANT]
> **Vetor Inicial (Initial Access):**
> O ataque não começou na empresa, mas em um **Watering Hole** (site de terceiros infectado).

### ⛓️ The Kill Chain Breakdown

| Fase | Ação Técnica | Falha de Defesa (Gap) |
| :--- | :--- | :--- |
| **1. Recon** | OSINT em redes sociais para mapear engenheiros. | N/A (Dados públicos). |
| **2. Weaponization** | **Iframe Injection** no site da liga de boliche. | Falha de segurança no site do terceiro. |
| **3. Delivery** | Engenheiro acessa o site e baixa o payload. | Navegação pessoal em dispositivo corporativo. |
| **4. Exploitation** | Malware infecta notebook e busca persistência. | Endpoint Protection insuficiente. |
| **5. Lateral Movement** | Atacante pivota para um **Termostato IoT**. | **IoT com credenciais padrão** na mesma rede de dados. |
| **6. Actions on Obj.** | Exfiltração de P&D e destruição de backups. | **Rede Plana** (Sem VLANs) e Backups online/vulneráveis. |

> [!WARNING]
> **Lição Crítica:**
> Dispositivos IoT (Internet das Coisas) são frequentemente o elo mais fraco. Eles **DEVEM** estar isolados em uma VLAN segregada, sem acesso a servidores de arquivos críticos.

---

## 🧠 Conceitos Táticos

### 📡 1.1.1 The "Evil Twin" Attack
> [!CAUTION]
> **Definição:** Um ataque Man-in-the-Middle (MitM) onde o atacante configura um Access Point (AP) falso com o mesmo **SSID** de uma rede legítima.
>
> **Objetivo:** Interceptar credenciais ou injetar malware em usuários que se conectam automaticamente.

### 🎭 1.2 Agentes de Ameaça (Threat Actors)

* 👹 **Hacktivistas:** Motivados por ideologia política/social.
* 💰 **Crime Organizado:** Motivados exclusivamente por lucro financeiro.
* 🕵️ **State-Sponsored (APT):** Espionagem nacional, sabotagem ou ciberguerra.
* internal **Insiders:** O perigo interno (intencional ou acidental).

### 🗄️ 1.3 Classificação de Dados (Data Impact)

Para priorização de incidentes em um SOC:

1.  🔴 **PII (Personally Identifiable Information):** Dados que identificam um indivíduo (CPF, RG, Biometria).
2.  🟡 **PHI (Protected Health Information):** Histórico médico, diagnósticos (Regulados por leis como HIPAA/LGPD).
3.  🔵 **PSI (Personal Security Information):** Dados de segurança pessoal.

---

## 🛠️ Laboratórios & Prática

- [ ] **Lab 1.1.5:** Instalação de Máquinas Virtuais (Setup do Lab).
- [ ] **Lab 1.3.4:** Perfilamento de Cybercriminosos.

---
*Documentação mantida por **Ícaro de Souza Mariano** | Especialista em Formação*
