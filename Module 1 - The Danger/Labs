# 🕵️‍♂️ Tactical Field Report: Threat Intel & Setup

![Status](https://img.shields.io/badge/Status-Mission_Accomplished-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Recon_&_Environment-red?style=for-the-badge)
![Environment](https://img.shields.io/badge/Environment-VirtualBox_Lab-blue?style=for-the-badge)

> [!NOTE]
> **Resumo Operacional:** Este log documenta a preparação do ambiente de laboratório (VOC) e a análise inicial de vetores de ataque em tecnologias comuns e infraestruturas críticas.

---

## 📡 Lab 1.0.6: Top Hacker Shows Us How It Is Done

**Objetivo:** Análise de vulnerabilidades em tecnologias "seguras" (RFID, Wireless) sob a ótica de um atacante.

* **Fonte de Intel:** Pablos Holman (TEDx).
* **Vetor Identificado:** Transmissões de rádio de curto alcance sem criptografia adequada.
* **Mitigação:** Uso de "bloqueadores" físicos (carteiras blindadas) e implementação de criptografia forte no design do hardware.

> [!WARNING]
> **Insight Crítico:** A maioria dos sistemas modernos sacrifica segurança em nome da conveniência, criando uma superfície de ataque massiva em cartões de crédito e chaves digitais.

---

## 🖥️ Lab 1.1.5: Virtual Operations Center (VOC) Setup

**Objetivo:** Implantação da estação de trabalho `CyberOps Workstation` (Linux) para análise segura.

| Especificação | Detalhe |
| :--- | :--- |
| **Host Físico** | Lenovo LOQ (Intel i5 13th Gen, 16GB RAM, RTX 2050Ti) |
| **Hypervisor** | Oracle VirtualBox |
| **Guest VM** | CyberOps Workstation (Arch: Linux 64-bit) |
| **Formato** | OVA (Open Virtualization Format) |

> [!TIP]
> **Troubleshooting de Rede:**
> Caso a VM não pegue IP via DHCP, alterar o adaptador de rede nas configurações do VirtualBox de **NAT** para **Bridged Adapter** (selecionando a placa `Intel Dual Band Wireless` ou Ethernet correspondente).
>
> **Credenciais Padrão:** `user: analyst` | `pass: cyberops`

---

## 🌍 Lab 1.1.6: Global Threat Case Studies

**Objetivo:** Dissecção de ataques de alto perfil para compor a base de conhecimento de ameaças.

| Incidente | Alvo | Vetor / Método | Impacto |
| :--- | :--- | :--- | :--- |
| **Stuxnet** | Infraestrutura Nuclear (Irã) | Malware (Worm) via USB | Danos físicos às centrífugas (Ciberguerra). |
| **Marriott** | Setor Hoteleiro | Acesso não autorizado a DB | Vazamento de 500 milhões de registros hóspedes. |
| **Microsoft** | Suporte ao Cliente | Falha de Configuração | Exposição de dados de analytics de suporte. |

> [!IMPORTANT]
> **Custo do Cibercrime:** Estimativas apontam prejuízos globais superando **US$ 600 Bilhões** anualmente.

---

## 🔌 Lab 1.2.3: IoT Vulnerability Surface

**Objetivo:** Mapeamento de riscos na "Internet das Coisas" (50 bilhões de dispositivos previstos até 2030).

* **O Problema:** Dispositivos IoT frequentemente possuem _hardcoded credentials_ e não suportam atualizações de firmware.
* **Verticais em Risco:**
    * 🏭 **Indústria:** Sensores SCADA expostos.
    * 🏥 **Saúde:** Marcapassos e bombas de insulina vulneráveis.
    * 🏛️ **Governo:** Câmeras de tráfego e sensores urbanos.

---

## 🎭 Lab 1.3.4: Visualizing the Black Hats

**Objetivo:** Modelagem de ameaças criando perfis psicológicos e táticos de atacantes.

### 🗂️ Perfilamento de Ameaças

1.  **O Hacktivista**
    * **Motivação:** Ideológica / Política.
    * **Método:** DDoS ou Defacement.
    * **Alvo:** Sites governamentais ou corporações polêmicas.

2.  **O Cibercriminoso**
    * **Motivação:** Financeira.
    * **Método:** Ransomware ou Roubo de Cartões.
    * **Alvo:** Varejo e Bancos.

3.  **O State-Sponsored (APT)**
    * **Motivação:** Espionagem Geopolítica.
    * **Método:** Zero-day exploits, persistência longa.
    * **Alvo:** Infraestrutura crítica de nações rivais.
