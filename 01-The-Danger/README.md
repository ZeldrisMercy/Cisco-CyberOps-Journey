# 📁 Module 01: The Danger & Security Concepts

> [!NOTE]
> **Resumo Executivo:**
> Este módulo fundamenta o vocabulário tático de um analista SOC. Ele disseca a anatomia de ataques, perfis de ameaça, impacto de vazamentos de dados e os princípios arquiteturais universais de segurança (Triade CIA, Modelos de Acesso e CVSS), essenciais para o exame CBROPS 200-201.

---

## 🛡️ Fundamentos Arquiteturais (O Core da Prova)

Para projetar defesas ou analisar incidentes, é necessário dominar as métricas e modelos padrão da indústria cobrados no exame:

### 1. A Tríade CIA e o Framework AAA
* **Confidencialidade:** Garantir que apenas pessoal autorizado leia os dados (Ex: Criptografia AES).
* **Integridade:** Garantir que os dados não foram alterados em trânsito ou em repouso (Ex: Hashes SHA-256).
* **Disponibilidade (Availability):** Garantir que os sistemas estejam acessíveis quando necessários (Ex: Redundância, Mitigação DDoS).
> **AAA (Authentication, Authorization, Accounting):** Quem é você? (Autenticação); O que você pode fazer? (Autorização); O que você fez enquanto esteve aqui? (Auditoria/Accounting).

### 2. Modelos de Controle de Acesso (Access Control Models)
* **DAC (Discretionary Access Control):** O criador/dono do arquivo decide quem tem acesso. (Muito flexível, porém perigoso em ambientes corporativos).
* **MAC (Mandatory Access Control):** Controle rigoroso baseado em rótulos de confidencialidade (ex: *Top Secret*, *Confidencial*). O sistema operacional impõe a regra, o usuário não pode alterar.
* **RBAC (Role-Based Access Control):** Acesso baseado na função do usuário na empresa (ex: Grupo "RH" ou "Engenharia"). É o padrão mais usado no mercado corporativo.

### 3. Métricas de Risco: CVSS v3.1 (Common Vulnerability Scoring System)
O SOC não conserta tudo ao mesmo tempo; ele prioriza baseado na pontuação CVSS. O *Base Score* é calculado usando métricas como:
* **Attack Vector (AV):** O ataque pode ser feito pela internet (Network) ou exige acesso físico?
* **Attack Complexity (AC):** É fácil de explorar (Low) ou requer condições super específicas (High)?
* **Privileges Required (PR):** O atacante precisa já ter uma conta de Administrador (High) ou nenhuma conta (None)?

---

## 💀 Anatomia de um Ataque: Case Study "Aupticon"

Análise técnica de espionagem industrial através de um **Watering Hole Attack** (site de terceiros infectado).

### ⛓️ The Kill Chain Breakdown (Mapeamento Tático)

| Fase | Ação Técnica | Falha de Defesa (Gap) |
| :--- | :--- | :--- |
| **1. Recon** | OSINT em redes sociais para mapear engenheiros. | N/A (Dados públicos). |
| **2. Weaponization** | **Iframe Injection** no site da liga de boliche. | Falha de segurança no site do terceiro. |
| **3. Delivery** | Engenheiro acessa o site e baixa o payload. | Navegação pessoal em dispositivo corporativo. |
| **4. Exploitation** | Malware infecta notebook e busca persistência. | Endpoint Protection insuficiente. |
| **5. Lateral Movement** | Atacante pivota para um **Termostato IoT**. | **IoT com credenciais padrão** na mesma rede. |
| **6. Actions on Obj.** | Exfiltração de P&D e destruição de backups. | **Rede Plana** (Sem VLANs) e Backups online. |

> [!WARNING]
> **Lição Crítica:**
> Dispositivos IoT são frequentemente o elo mais fraco. Eles **DEVEM** ser isolados em uma VLAN segregada devido à falta de *patching* nativo.

---

## 🧠 Ameaças e Classificação de Dados

* **The "Evil Twin" Attack:** Access Point (AP) falso com o mesmo **SSID** de uma rede legítima para interceptar credenciais (MitM).
* **Data Impact:**
  1. 🔴 **PII:** Identifica um indivíduo civilmente (CPF, RG).
  2. 🟡 **PHI:** Histórico médico e diagnósticos (Regulados por HIPAA/LGPD).

---

## 📑 Tactical Field Report: Lab Executions

* **[Lab 1.1.5 - Workstation Setup]:** Provisionamento de ambiente controlado via VirtualBox isolado via rede NAT/Bridged para proteger a máquina host física.
* **[Lab 1.3.4 - Visualização dos Black Hats]:** Criação de perfis de ameaça (Hacktivistas, APTs, Insiders) baseados em motivação e método.
