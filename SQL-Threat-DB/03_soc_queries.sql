-- ==============================================================================
-- CONSULTAS ANALÍTICAS (DQL) - SOC & CYBEROPS EXAM
-- ==============================================================================

-- QUERY 1: Top 5 IPs Atacantes (Blue Team Analytics)
-- Conta quantas vezes um IP tentou invadir e soma o total de falhas.
SELECT 
    ip_origem, 
    COUNT(*) as total_incidentes,
    SUM(tentativas_falhas) as total_falhas_bruteforce,
    status_resolucao
FROM tb_threat_logs
WHERE status_resolucao != 'WHITELIST'
GROUP BY ip_origem, status_resolucao
ORDER BY total_falhas_bruteforce DESC
LIMIT 5;

-- QUERY 2: Relatório de Questões por Módulo (Gestão de Estudos)
-- Cruza a tabela de módulos com a de questões para saber onde você tem mais material de estudo.
SELECT 
    m.numero_modulo,
    m.nome_modulo,
    m.foco_principal,
    COUNT(q.questao_id) as total_questoes_cadastradas
FROM tb_modulos_curso m
LEFT JOIN tb_questoes_quiz q ON m.modulo_id = q.modulo_id
GROUP BY m.numero_modulo, m.nome_modulo, m.foco_principal
ORDER BY m.numero_modulo ASC;

-- QUERY 3: Histórico de IPs Bloqueados nas Últimas 24 Horas
SELECT 
    ip_origem, 
    tentativas_falhas, 
    data_incidente 
FROM tb_threat_logs 
WHERE status_resolucao = 'BLOQUEADO' 
  AND data_incidente >= datetime('now', '-1 day'); 
  -- Nota: a função datetime() é sintaxe do SQLite. Se for usar PostgreSQL depois, muda para NOW() - INTERVAL '1 DAY'.
