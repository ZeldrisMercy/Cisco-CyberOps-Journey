# 🗄️ SQL Threat Database & CyberOps Backend

> **Missão:** Centralizar a telemetria de segurança e o conhecimento técnico. Este diretório contém a modelagem e os scripts relacionais (ETL) que atuam como o "cérebro" do laboratório DevSecOps.

Enquanto os scripts em Python (Sensores/IPS) operam na ponta, este banco de dados **SQLite** é o destino final para a retenção de logs a longo prazo, análise de incidentes e o backend escalável do nosso simulador de exames.

---

## 🏗️ Arquitetura de Dados (Modelagem)

O banco foi desenhado para suportar dois domínios críticos:

1. **Threat Intelligence (SOC Logs):**
   * Tabela `tb_threat_logs`: Armazena os registros de ataques detectados pelo IPS local. Mantém o histórico de IPs maliciosos, contagem de tentativas (Força Bruta) e status de bloqueio no firewall.
2. **CyberOps Quiz Engine:**
   * Tabelas `tb_modulos_curso` e `tb_questoes_quiz`: Uma estrutura relacional que substitui arquivos estáticos JSON, permitindo consultas complexas por módulo.
   * Tabela `tb_progresso_estudos`: Grava a nota final do operador após cada simulado, gerando métricas de aprovação ao longo do tempo.

---

## 🚀 Como Inicializar o Banco (ETL & Seed)

Se você acabou de clonar o repositório, o banco de dados precisará ser construído e populado. Siga a ordem abaixo no seu terminal:

1. **Criar a base e importar dados legados:**
   * Execute: `python db_migrator.py`
   * *O que faz:* Cria o arquivo `cyberops_soc.db`, constrói as tabelas DDL e faz um processo de ETL (Extract, Transform, Load) para migrar as questões antigas do formato JSON para o modelo SQL.
2. **Injetar dados novos (Redes & Threat Intel):**
   * Execute: `python run_seed.py`
   * *O que faz:* Roda o script `02_data_seed_dml.sql` por baixo dos panos, inserindo os módulos recentes de protocolos de rede e simulando logs de ataques de força bruta.

---

## 🛠️ Ferramentas de Operação

Com o banco de dados provisionado, o arsenal principal está pronto para uso:

* **Simulador Interativo:** `python cyberops_quizzer_db.py`
  * O novo motor V4. Consulta as questões dinamicamente no banco via SQL, aplica a prova e faz o `INSERT` da sua nota final no banco de dados.
* **Painel de Telemetria:** `python soc_analytics.py`
  * Dashboard analítico no terminal. Executa queries de agregação (`GROUP BY`, `JOIN`, `SUM`) para exibir o histórico de notas dos simulados e listar os "Top IPs Atacantes" registrados na base do SOC.
