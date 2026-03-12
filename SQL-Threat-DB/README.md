# 🗄️ SQL Threat Database & CyberOps Backend

> **Missão:** Centralizar a telemetria de segurança e o conhecimento técnico. Este diretório contém a modelagem e os scripts relacionais que atuam como o "cérebro" do nosso laboratório DevSecOps.

Enquanto os scripts em Python (Sensores/IPS) operam na ponta (Endpoint/Rede), este banco de dados relacional é o destino final para a retenção de logs a longo prazo, análise de incidentes e o backend de dados do simulador de exames.

---

## 🏗️ Arquitetura de Dados

O banco foi modelado com dois domínios principais:

1. **Threat Intelligence (SOC Logs):**
   * Armazena os registros de ataques detectados pelo `soc_ips_blocker.py`.
   * Mantém o histórico de IPs maliciosos, contagem de tentativas (Força Bruta) e status de bloqueio no firewall.
2. **CyberOps Quiz Engine:**
   * Uma estrutura normalizada para armazenar módulos, perguntas, alternativas e explicações do simulador da certificação Cisco CyberOps, substituindo o antigo arquivo JSON estático por um modelo escalável.



---

## 📜 Ordem de Execução dos Scripts

Para provisionar o banco de dados localmente (compatível com PostgreSQL, MySQL ou SQLite), execute os scripts na seguinte ordem:

1. `01_schema_ddl.sql`: Cria as tabelas, chaves primárias e estrangeiras (Estrutura).
2. `02_data_seed_dml.sql`: Insere a carga inicial de dados (Módulos do curso e banco de questões).
3. `03_soc_queries.sql`: Contém consultas analíticas prontas para uso do Blue Team (ex: Top 5 IPs atacantes, taxa de acerto no quiz).
