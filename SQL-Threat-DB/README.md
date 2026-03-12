# 🗄️ SQL Threat Database & CyberOps Backend 

> **Missão:** Centralizar a telemetria de segurança e o conhecimento técnico. Este diretório contém a modelagem relacional, os scripts de migração (ETL) e o motor principal de estudos do laboratório.

Este módulo marca a transição de arquivos estáticos JSON para uma arquitetura relacional robusta utilizando **SQLite**. Aqui, unimos a Engenharia de Software com a Cibersegurança para criar um ambiente de estudo e análise de dados escalável.

---

## 🏗️ Arquitetura e Fluxo de Dados

O ecossistema é alimentado por três camadas de dados:
1. **Threat Intelligence:** Armazenamento de logs de ataques detectados para análise de tendências.
2. **Knowledge Base:** Banco de questões estruturado pelos 10 módulos da certificação Cisco CyberOps Associate.
3. **User Telemetry:** Monitoramento de desempenho do operador com histórico de acertos e controle automático de logs (Anti-Flood).

---

## 🚀 Guia para Recrutas: Como rodar este projeto?

Se você é novo no mundo Git/Python, siga este "Manual de Campo" para colocar a central de operações para rodar no seu PC.

### 1. Preparando o Terreno
Você precisará do **[Python (v3.10+)](https://www.python.org/downloads/)** e do **[Git](https://git-scm.com/downloads)** instalados em sua máquina.

### 2. Clonando o Repositório
Abra o seu terminal (CMD ou PowerShell) e digite os comandos abaixo:
```bash
# Clone o repositório oficial
git clone [https://github.com/ZeldrisMercy/Cisco-CyberOps-Journey.git](https://github.com/ZeldrisMercy/Cisco-CyberOps-Journey.git)

# Entre na pasta do banco de dados
cd Cisco-CyberOps-Journey/SQL-Threat-DB
```

### 3. Provisionando o Banco de Dados (Setup Inicial)
Para criar a estrutura e importar o conhecimento legado do repositório, execute:
```bash
# Passo A: Migra as questões do JSON antigo para o Banco SQL
python db_migrator.py

# Passo B: Injeta as novas questões de Redes e logs de SOC
python run_seed.py
```

---

## 🛠️ O Centro de Comando (Scripts Ativos)

### 🔴 CyberOps DB Quizzer (`cyberops_quizzer_db.py`)
O motor principal de treinamento focado na certificação.
* **Feedback em Tempo Real:** Painel tático que mostra acertos e erros durante a execução.
* **Persistência de Dados:** Grava o score final automaticamente no banco de dados.
* **Histórico Integrado:** Acesse a opção `[H]` no menu para ver seus últimos 10 desempenhos.
* **Auto-Cleanup:** O sistema mantém apenas as 10 sessões mais recentes para evitar "flood" no banco.

### 🔵 SOC Telemetry Analytics (`soc_analytics.py`)
Dashboard analítico para extrair inteligência do banco. Exibe os IPs atacantes mais recorrentes e um resumo gráfico do seu progresso acadêmico.

---

## 📊 Estrutura de Tabelas (SQL)

| Tabela | Função |
| :--- | :--- |
| `tb_modulos_curso` | Lista os 10 domínios do blueprint oficial CyberOps. |
| `tb_questoes_quiz` | Contém perguntas, alternativas e explicações técnicas detalhadas. |
| `tb_progresso_estudos` | Registra scores, data e aproveitamento percentual. |
| `tb_threat_logs` | Histórico de IPs bloqueados e telemetria de ataques. |

---

## 🔗 Links Oficiais da Operação

* 🌐 **Repositório Principal (Git):** [Cisco-CyberOps-Journey](https://github.com/ZeldrisMercy/Cisco-CyberOps-Journey)
* 🐍 **Módulo de Automações Base (Versão Python/JSON):** [Acessar scripts-and-automation](../scripts-and-automation/)

---
*Desenvolvido e mantido por **Ícaro de Souza Mariano** | Conecte-se comigo no [LinkedIn](http://www.linkedin.com/in/icaro-s-m).*
