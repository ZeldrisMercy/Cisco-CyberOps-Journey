# 🛡️ Centro de Operações & Threat Intel: CyberOps (CBROPS 200-201)

![Cisco](https://img.shields.io/badge/CISCO-044342?style=for-the-badge&logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-EM_PROGRESSO-warning?style=for-the-badge)
![Focus](https://img.shields.io/badge/FOCUS-BLUE%20TEAM%20%7C%20DEVSEC-blue?style=for-the-badge)

Bem-vindo ao meu ecossistema de estudos e portfólio técnico. Este repositório documenta a minha jornada prática em Cibersegurança e Desenvolvimento Seguro, unindo a preparação para a certificação **Cisco CyberOps Associate**, os laboratórios do programa **Hackers do Bem** e a minha base académica em **Sistemas de Informação pela Uniube**.

> **Missão:** Ir além da teoria estática. O objetivo aqui é documentar táticas de defesa (Threat Intel, Hardening, Monitoramento) e provar a aplicação prática de conceitos de resposta a incidentes (IR), construindo pontes sólidas entre a infraestrutura de segurança e o desenvolvimento de software.

---

## 🗺️ Mapa de Batalha (Blueprint da Certificação)

Navegue pelos módulos abaixo para aceder aos meus *Tactical Field Reports*, resumos dinâmicos e quizzes de revisão.

| Domínio | Relatórios Táticos | Estudo Ativo (Quizzes) |
| :--- | :--- | :--- |
| **1. Security Concepts** | [📁 Módulo 01: The Danger](./01-The-Danger/README.md) | [🧠 Quiz Mód. 1](./01-The-Danger/QUIZ.md) |
| **2. Security Monitoring** | [📁 Módulo 02: Cybersecurity Pro](./02-Cybersecurity-Pro/README.md) | [🧠 Quiz Mód. 2](./02-Cybersecurity-Pro/QUIZ.md) |
| **3. Host-Based Analysis** | [📁 Módulo 03: Windows Fortress](./03-Windows-Fortress/README.md) | [🧠 Quiz Mód. 3](./03-Windows-Fortress/QUIZ.md) |
| **4. Network Intrusion** | [📁 Módulo 04: Linux Fortress](./04-Linux-Fortress/README.md) | [🧠 Quiz Mód. 4](./04-Linux-Fortress/QUIZ.md) |

---

## ⚡ O Diferencial: DevSecOps & Automação

Acredito que a melhor forma de defender um sistema é compreendendo como ele é construído. Com o objetivo de atuar no desenvolvimento de software aplicado à segurança corporativa e proteção contra riscos digitais, este repositório traz um forte viés prático:

* **[🐍 Scripts & Automação](./scripts-and-automation/):** Os meus scripts (Python/Bash) criados para parseamento de logs, consumo de APIs de Threat Intel (ex: VirusTotal) e automação de triagem de incidentes.
* **[🔍 Análise de Tráfego (PCAP) & Labs](./labs-and-pcap/):** Investigações documentadas utilizando Wireshark para isolar tráfego malicioso em ambientes virtualizados.
* **Engenharia Reversa de Conceitos:** Aplicação de conceitos de redes e Sistemas Operativos diretamente na construção de código seguro.

---

## 🗃️ Active Recall & Desenvolvimento Próprio

Acredito que a melhor forma de fixar o conhecimento é construindo as ferramentas que o testam. Em vez de utilizar aplicações de *flashcards* de terceiros, desenvolvi a minha própria solução de repetição espaçada:

* 💻 **[CyberOps CLI Quizzer](./scripts-and-automation/cyberops_quizzer.py):** Um script em Python desenvolvido do zero que consome uma base de dados JSON (`questoes_cbrops.json`) com centenas de conceitos sobre portas, protocolos e TTPs. Funciona nativamente no terminal, simulando o ambiente de um analista e gerando relatórios do meu desempenho nos estudos. 

> *Sinta-se à vontade para clonar o script, adicionar as suas próprias perguntas no ficheiro JSON e testar os seus conhecimentos diretamente a partir do seu terminal!*

---
*Desenvolvido e mantido por **Ícaro de Souza Mariano** | Conecte-se comigo no [LinkedIn](http://www.linkedin.com/in/icaro-s-m).*
