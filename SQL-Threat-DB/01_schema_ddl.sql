-- ==============================================================================
-- SOC & CYBEROPS EXAM DATABASE SCHEMA (DDL)
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- DOMÍNIO 1: THREAT INTELLIGENCE (Integração com Python IPS)
-- ------------------------------------------------------------------------------

CREATE TABLE tb_threat_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY, -- Use SERIAL se for PostgreSQL
    ip_origem VARCHAR(45) NOT NULL,        -- Suporta IPv4 e IPv6
    tentativas_falhas INT NOT NULL,
    status_resolucao VARCHAR(20) NOT NULL, -- Ex: 'BLOQUEADO', 'WHITELIST', 'MONITORANDO'
    data_incidente TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ferramenta_origem VARCHAR(50) DEFAULT 'soc_ips_blocker_v1'
);

-- ------------------------------------------------------------------------------
-- DOMÍNIO 2: CYBEROPS QUIZ ENGINE (Backend de Estudos)
-- ------------------------------------------------------------------------------

CREATE TABLE tb_modulos_curso (
    modulo_id INT PRIMARY KEY,
    numero_modulo VARCHAR(10) NOT NULL UNIQUE, -- Ex: '01', '10'
    nome_modulo VARCHAR(100) NOT NULL,         -- Ex: 'Net Application Services'
    foco_principal VARCHAR(50)                 -- Ex: 'Redes', 'Host', 'Security'
);

CREATE TABLE tb_questoes_quiz (
    questao_id INT AUTO_INCREMENT PRIMARY KEY, -- Use SERIAL se for PostgreSQL
    modulo_id INT NOT NULL,
    pergunta TEXT NOT NULL,
    opcao_a VARCHAR(255) NOT NULL,
    opcao_b VARCHAR(255) NOT NULL,
    opcao_c VARCHAR(255) NOT NULL,
    opcao_d VARCHAR(255) NOT NULL,
    resposta_correta CHAR(1) NOT NULL,         -- 'A', 'B', 'C' ou 'D'
    explicacao TEXT,
    CONSTRAINT fk_modulo FOREIGN KEY (modulo_id) REFERENCES tb_modulos_curso(modulo_id)
);

-- Tabela para rastrear seu progresso e Active Recall
CREATE TABLE tb_progresso_estudos (
    sessao_id INT AUTO_INCREMENT PRIMARY KEY,
    data_sessao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modulo_id INT NOT NULL,
    total_questoes INT NOT NULL,
    acertos INT NOT NULL,
    CONSTRAINT fk_progresso_modulo FOREIGN KEY (modulo_id) REFERENCES tb_modulos_curso(modulo_id)
);
