# 🕵️‍♂️ Tactical Field Report: Threat Intel & Setup

![Status](https://img.shields.io/badge/Status-Mission_Accomplished-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Recon_&_Environment-red?style=for-the-badge)
![Environment](https://img.shields.io/badge/Environment-VirtualBox_Lab-blue?style=for-the-badge)

> [!NOTE]
> [cite_start]**Resumo Operacional:** Registro de execução técnica focado na configuração do ambiente de virtualização (CyberOps Workstation) e análise forense de vetores de ataque em infraestruturas críticas e IoT[cite: 29, 33, 166, 199].

---

## 📡 Lab 1.0.6: Top Hacker Shows Us How It Is Done

[cite_start]**Objetivo:** Desconstrução de vulnerabilidades em tecnologias sem fio (RFID/Wireless)[cite: 3, 5].

### 🛠️ Execution Log
1.  [cite_start]**Reconnaissance:** Analisada apresentação de Pablos Holman sobre vetores de ataque em sistemas "seguros"[cite: 6, 8].
2.  **Target Analysis (RFID/Wireless):**
    * [cite_start]Identificado que chips RFID e chaves de carros transmitem dados que podem ser clonados[cite: 15].
    * [cite_start]O ataque explora vulnerabilidades em tecnologias comuns usadas diariamente[cite: 5, 8].
3.  **Mitigation Strategy:**
    * [cite_start]✅ Pesquisa sobre métodos para atenuar o hack, como bloqueio físico de sinal[cite: 16, 26].

---

## 🖥️ Lab 1.1.5: Virtual Operations Center (VOC) Setup

[cite_start]**Objetivo:** Deploy da estação de trabalho `CyberOps Workstation` (Linux) no VirtualBox[cite: 31, 33].

### 🛠️ Execution Log
**1. Environment Provisioning:**
* [cite_start]**Host:** PC com 8GB+ RAM e 40GB+ disco livre[cite: 45].
* [cite_start]**Hypervisor:** Oracle VirtualBox instalado e configurado[cite: 51, 53].
* [cite_start]**Image Deployment:** Importado arquivo `cyberops_workstation.ova` seguindo padrão OVF[cite: 60, 68].

**2. Network Troubleshooting (Critical):**
> [!WARNING]
> [cite_start]Erro comum: interface física não encontrada na inicialização[cite: 83, 87].

* [cite_start]**Ação Corretiva:** Alterada configuração de rede nas configurações da VM (Change Network Settings) para selecionar o adaptador correto ou usar NAT[cite: 81, 90, 93].

**3. System Access & Verification:**
Realizado login no terminal da VM com as credenciais padrão:
```bash
$ login: analyst
$ password: cyberops
$ ip address
# Verificação de conectividade e endereço IP[cite: 99, 100, 120].
### 3️⃣ Bloco: Lab 1.1.6 (Estudos de Caso)
*Copie este e cole abaixo.*

```markdown
---

## 🌍 Lab 1.1.6: Global Threat Case Studies

[cite_start]**Objetivo:** Profiling de ataques cibernéticos de alto perfil e análise de impacto econômico[cite: 157, 160].

### 🛠️ Execution Log
**Case #1: Stuxnet**
* [cite_start]**Alvo:** Infraestrutura crítica e sistemas industriais[cite: 173].
* **Análise:** Investigação sobre motivação e métodos de sabotagem.

**Case #2: Marriott & Outros**
* [cite_start]**Casos:** Violação de dados da Marriott, Nações Unidas e Microsoft[cite: 174, 175, 176].
* [cite_start]**Impacto:** Análise do "quem, o quê, onde e por que" de cada ataque[cite: 180].

> [!IMPORTANT]
> [cite_start]**Impacto Global:** O custo do crime cibernético para a economia global é estimado em mais de **US$ 600 Bilhões** anualmente[cite: 165].
---

## 🔌 Lab 1.2.3: IoT Vulnerability Surface

[cite_start]**Objetivo:** Análise de vulnerabilidades na Internet das Coisas (IoT)[cite: 199].

### 🛠️ Execution Log
[cite_start]**Cenário:** Projeção de 50 bilhões de dispositivos IoT ativos até 2030[cite: 204].

1.  [cite_start]**Vulnerability Scan:** Dispositivos IoT frequentemente possuem sistemas operacionais antigos e sem patches[cite: 206].
2.  [cite_start]**Exploit Scenario:** A segurança nem sempre é considerada no design do produto[cite: 205].
3.  [cite_start]**Verticals:** Pesquisadas vulnerabilidades em Indústria, Energia, Saúde e Governo[cite: 212].
4.  [cite_start]**Mitigation:** Análise de medidas para limitar a vulnerabilidade desses dispositivos[cite: 226].
---

## 🎭 Lab 1.3.4: Visualizing the Black Hats

[cite_start]**Objetivo:** Threat Modeling e criação de perfis de atacantes[cite: 231].

### 🛠️ Execution Log
[cite_start]Desenvolvi três cenários de ataque hipotéticos para entender motivações[cite: 236]:

| Cenário | Atacante/Grupo | Motivo | Método | Mitigação |
| :--- | :--- | :--- | :--- | :--- |
| **Cenário 1** | [cite_start]Definir Ator [cite: 244] | [cite_start]Motivação Específica [cite: 246] | [cite_start]Método Utilizado [cite: 247] | [cite_start]Prevenção [cite: 252] |
| **Cenário 2** | [cite_start]Definir Grupo [cite: 255] | [cite_start]Motivação [cite: 256] | [cite_start]Método [cite: 257] | [cite_start]Prevenção [cite: 262] |
| **Cenário 3** | [cite_start]Definir Ator [cite: 264] | [cite_start]Motivação [cite: 266] | [cite_start]Método [cite: 267] | [cite_start]Prevenção [cite: 269] |
