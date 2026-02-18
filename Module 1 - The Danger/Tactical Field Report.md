# 🛡️ Cisco CyberOps Associate: Journey

![Cisco](https://img.shields.io/badge/CISCO-044342?style=for-the-badge&logo=cisco&logoColor=white)
![Netacad](https://img.shields.io/badge/NETACAD-00BCEB?style=for-the-badge&logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-COMPLETED-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue?style=for-the-badge)

## 📁 Module 01: The Danger

> [!NOTE]
> **Resumo Executivo:** Este módulo consolida a base teórica sobre a superfície de ataque global, analisando desde vulnerabilidades em dispositivos IoT até grandes violações de dados corporativos, além de estabelecer o ambiente de laboratório virtualizado para operações de defesa.

---

## 📑 Tactical Field Report: Lab Executions

### 🔬 Análise de Vulnerabilidades: Case Study "Top Hacker"
**Referência:** *1.0.6 Atividade de Classe - Top Hacker nos Mostra Como é Feito*

Análise técnica sobre como sistemas "seguros" são comprometidos através de tecnologias comuns.

> [!IMPORTANT]
> **Vetor de Ataque:** Exploração de protocolos de comunicação sem fio e vulnerabilidades em hardware de infraestrutura.

* **Relatório de Execução:** Investigação de técnicas de interceptação de dados em trânsito e análise de como a falta de criptografia em protocolos legados permite o controle total de dispositivos por atacantes.
* **Aprendizado Crítico:** A segurança por obscuridade não é uma defesa válida; a visibilidade sobre o que o atacante pode obter (dados/controle) é o primeiro passo para a mitigação.

---

### 🖥️ Infraestrutura: Setup da Workstation de Análise
**Referência:** *1.1.5 Laboratório - Instalando as Máquinas Virtuais*

Provisionamento de ambiente controlado para análise de ameaças e resposta a incidentes.

* **Ação Técnica:** Importação e configuração da VM `CyberOps Workstation` via VirtualBox utilizando o padrão OVF.
* **Configuração de Rede:** Ajuste de adaptadores de rede (Bridged/NAT) para garantir isolamento do host físico.
* **Relatório de Execução:** Validação de conectividade via CLI (`ip address`) e teste de navegação segura dentro do ambiente convidado (Guest).
* **Aprendizado Crítico:** O uso de snapshots e isolamento de rede protege a máquina host contra infecções por malware durante processos de investigação.

---

### 📂 Inteligência de Ameaças: Estudos de Caso de Alto Perfil
**Referência:** *1.1.6 Laboratório - Estudos de caso de cibersegurança*

Análise retrospectiva de ataques reais para identificação de padrões de adversários.

* **Alvos Analisados:** Stuxnet, Marriott, Nações Unidas e Microsoft Customer Support.
* **Relatório de Execução:** Mapeamento do "Quem, O Quê e Porquê" de cada incidente, focando nas ferramentas utilizadas (Weaponization) e no impacto financeiro/reputacional.
* **Aprendizado Crítico:** Grandes violações frequentemente utilizam falhas em cadeias de suprimentos ou má gestão de acesso para atingir objetivos de espionagem ou ganho financeiro.

---

### 🌐 Superfície de Ataque: Vulnerabilidades em IoT
**Referência:** *1.2.3 Laboratório - Aprendendo os detalhes dos ataques*

Investigação da insegurança inerente em dispositivos de Internet das Coisas.

* **Vertical de Foco:** Indústria, Saúde e Sistemas de Energia.
* **Relatório de Execução:** Pesquisa de vulnerabilidades causadas por sistemas operacionais embarcados antigos e falta de patches de segurança.
* **Aprendizado Crítico:** A escala da IoT (50 bilhões de dispositivos até 2030) cria uma superfície de ataque massiva que exige defesas baseadas em rede, já que o host muitas vezes não é atualizável.

---

### 👤 Modelagem de Adversário: Visualização dos Black Hats
**Referência:** *1.3.4 Laboratório - Visualização dos Black Hats*

Criação de perfis de ameaça baseados em motivação e método.

* **Ação Técnica:** Desenvolvimento de três cenários hipotéticos correlacionando Atacante -> Motivo -> Método de Ataque -> Mitigação.
* **Relatório de Execução:** Simulação de ataques direcionados a vulnerabilidades de negócios específicos para testar controles preventivos.
* **Aprendizado Crítico:** Entender a motivação do atacante (ex: lucro vs. ideologia) permite priorizar quais ativos críticos devem receber camadas adicionais de proteção.

---

**Analista Responsável:** Ícaro de Souza Mariano  
**Data do Relatório:** 18/02/2026
