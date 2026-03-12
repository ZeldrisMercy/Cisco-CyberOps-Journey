-- ==============================================================================
-- CARGA INICIAL DE DADOS (DML) - CYBEROPS & SOC DB
-- ==============================================================================

-- 1. Populando os Módulos do Curso
INSERT INTO tb_modulos_curso (modulo_id, numero_modulo, nome_modulo, foco_principal) VALUES
(1, '01', 'The Danger', 'Security Concepts'),
(2, '02', 'Cybersecurity Pro', 'Security Monitoring'),
(3, '03', 'Windows Fortress', 'Host-Based Analysis'),
(4, '04', 'Linux Fortress', 'Host-Based Analysis'),
(5, '05', 'Net Protocols & Encapsulation', 'Network Concepts'),
(8, '08', 'ARC & MAC IP', 'Network Concepts'),
(9, '09', 'Transport Layer', 'Network Concepts'),
(10, '10', 'Net Application Services', 'Network Concepts');

-- 2. Migrando as Questões do Quiz (Amostra Inicial)
INSERT INTO tb_questoes_quiz (modulo_id, pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao) VALUES
(5, 'Durante o processo de encapsulamento no modelo TCP/IP, como é chamada a PDU (Protocol Data Unit) na Camada de Transporte?', 'A) Quadro (Frame)', 'B) Pacote (Packet)', 'C) Segmento (Segment)', 'D) Dado (Data)', 'C', 'Na camada de Transporte (Transport Layer), os dados são encapsulados em Segmentos (TCP) ou Datagramas (UDP).'),

(8, 'Qual protocolo é responsável por mapear um endereço IPv4 lógico para um endereço MAC físico em uma rede local Ethernet?', 'A) DNS', 'B) DHCP', 'C) ICMP', 'D) ARP', 'D', 'O Address Resolution Protocol (ARP) descobre o endereço MAC associado a um determinado endereço IPv4 na mesma sub-rede.'),

(9, 'Ao analisar um tráfego de rede, um analista de SOC observa um Three-Way Handshake (SYN, SYN-ACK, ACK). A qual protocolo e camada esse tráfego pertence?', 'A) UDP - Camada de Aplicação', 'B) TCP - Camada de Transporte', 'C) IP - Camada de Internet', 'D) ICMP - Camada de Rede', 'B', 'O Three-Way Handshake é o mecanismo do protocolo TCP (camada de Transporte) para estabelecer uma conexão confiável e orientada à conexão.'),

(10, 'Um ataque de amplificação e reflexão foi detectado direcionado à porta 53/UDP. Qual serviço de rede está sendo explorado?', 'A) HTTP', 'B) FTP', 'C) DNS', 'D) SSH', 'C', 'A porta 53 (usualmente UDP para queries padrão) é utilizada pelo serviço DNS, que é frequentemente alvo de ataques de amplificação DDoS.');

-- 3. Simulando Logs de Ameaças (Para testar o SOC Dashboard no futuro)
INSERT INTO tb_threat_logs (ip_origem, tentativas_falhas, status_resolucao) VALUES
('192.168.1.1', 2, 'WHITELIST'),
('203.0.113.45', 15, 'BLOQUEADO'),
('198.51.100.22', 4, 'MONITORANDO'),
('203.0.113.45', 8, 'BLOQUEADO'),
('10.0.0.50', 1, 'WHITELIST');
