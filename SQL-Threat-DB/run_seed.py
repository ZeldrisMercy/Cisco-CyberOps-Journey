import sqlite3

# Conecta no seu banco
conn = sqlite3.connect("cyberops_soc.db")
cursor = conn.cursor()

print("[*] Aplicando patch na estrutura do banco de dados...")

# 1. Garante que as tabelas de SOC e Progresso existam no SQLite
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS tb_threat_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_origem TEXT NOT NULL,
        tentativas_falhas INTEGER NOT NULL,
        status_resolucao TEXT NOT NULL,
        data_incidente TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ferramenta_origem TEXT DEFAULT 'soc_ips_blocker_v1'
    );

    CREATE TABLE IF NOT EXISTS tb_progresso_estudos (
        sessao_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_sessao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modulo_id INTEGER NOT NULL,
        total_questoes INTEGER NOT NULL,
        acertos INTEGER NOT NULL,
        FOREIGN KEY (modulo_id) REFERENCES tb_modulos_curso(modulo_id)
    );
''')

print("[*] Injetando a carga de dados (Seed)...")

# 2. Lê o arquivo SQL e executa tudo
try:
    with open("02_data_seed_dml.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())
    print(f"\033[92m[+] Novas questões e logs de ameaças injetados com sucesso!\033[0m")
except Exception as e:
    print(f"\033[91m[X] Erro ao injetar o arquivo SQL: {e}\033[0m")

conn.commit()
conn.close()
