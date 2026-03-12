import sqlite3

# Conecta no seu banco
conn = sqlite3.connect("cyberops_soc.db")
cursor = conn.cursor()

# Lê o arquivo SQL que criamos mais cedo e executa tudo
with open("02_data_seed_dml.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
print("[+] Novas questões e logs de ameaças injetados com sucesso!")
