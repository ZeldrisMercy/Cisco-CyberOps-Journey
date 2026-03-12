import json
import sqlite3
import os

# =======================================================================
# CYBEROPS ETL MIGRATOR: JSON -> SQLite (V2 - Smart Mapping)
# =======================================================================

ARQUIVO_JSON = "../scripts-and-automation/questoes_cbrops.json" 
ARQUIVO_DB = "cyberops_soc.db"

def configurar_banco(cursor):
    print("[*] Verificando/Criando estrutura do banco de dados...")
    
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS tb_modulos_curso (
            modulo_id INTEGER PRIMARY KEY,
            numero_modulo TEXT NOT NULL UNIQUE,
            nome_modulo TEXT NOT NULL,
            foco_principal TEXT
        );

        CREATE TABLE IF NOT EXISTS tb_questoes_quiz (
            questao_id INTEGER PRIMARY KEY AUTOINCREMENT,
            modulo_id INTEGER NOT NULL,
            pergunta TEXT NOT NULL,
            opcao_a TEXT NOT NULL,
            opcao_b TEXT NOT NULL,
            opcao_c TEXT NOT NULL,
            opcao_d TEXT NOT NULL,
            resposta_correta TEXT NOT NULL,
            explicacao TEXT,
            FOREIGN KEY (modulo_id) REFERENCES tb_modulos_curso(modulo_id)
        );
    ''')

def migrar_dados():
    print("=== INICIANDO MIGRAÇÃO DE DADOS (JSON -> SQL) ===")

    if not os.path.exists(ARQUIVO_JSON):
        print(f"\n[!] ERRO FATAL: Arquivo base '{ARQUIVO_JSON}' não encontrado.")
        return

    conn = sqlite3.connect(ARQUIVO_DB)
    cursor = conn.cursor()

    configurar_banco(cursor)

    print("[*] Configurando os 10 módulos do blueprint no banco de dados...")
    modulos_iniciais = [
        (1, '01', 'The Danger', 'Security Concepts'),
        (2, '02', 'Cybersecurity Pro', 'Security Monitoring'),
        (3, '03', 'Windows Fortress', 'Host-Based Analysis'),
        (4, '04', 'Linux Fortress', 'Host-Based Analysis'),
        (5, '05', 'Net Protocols & Encapsulation', 'Network Concepts'),
        (6, '06', 'Ethernet n IP', 'Network Concepts'),
        (7, '07', 'Connectivity Verification', 'Network Concepts'),
        (8, '08', 'ARC & MAC IP', 'Network Concepts'),
        (9, '09', 'Transport Layer', 'Network Concepts'),
        (10, '10', 'Net Application Services', 'Network Concepts')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO tb_modulos_curso (modulo_id, numero_modulo, nome_modulo, foco_principal) 
        VALUES (?, ?, ?, ?)
    ''', modulos_iniciais)

    print(f"[*] Lendo base de conhecimento legado: {ARQUIVO_JSON}")
    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8-sig') as f:
            questoes = json.load(f)
    except json.JSONDecodeError:
        print("\n[!] ERRO FATAL: O arquivo JSON está corrompido ou mal formatado.")
        return

    print("[*] Injetando registros na tabela tb_questoes_quiz...")
    contador = 0
    
    # enumerate(questoes) nos dá a posição (índice i) de cada questão, começando do 0
    for i, q in enumerate(questoes):
        try:
            # LÓGICA DE MAPEAMENTO INTELIGENTE:
            # Se a chave existir, usa ela. Se não, infere pelo índice matemático.
            if 'modulo' in q:
                modulo_id = int(q['modulo'])
            else:
                if i < 25: 
                    modulo_id = 1
                elif i < 50: 
                    modulo_id = 2
                elif i < 75: 
                    modulo_id = 3
                else: 
                    modulo_id = 4
            
            opcao_a = q['opcoes'][0]
            opcao_b = q['opcoes'][1]
            opcao_c = q['opcoes'][2]
            opcao_d = q['opcoes'][3]

            cursor.execute('''
                INSERT INTO tb_questoes_quiz 
                (modulo_id, pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (modulo_id, q['pergunta'], opcao_a, opcao_b, opcao_c, opcao_d, q['resposta_correta'], q['explicacao']))
            
            contador += 1
            
        except Exception as e:
            print(f"  [X] Falha na migração da questão: '{q.get('pergunta', 'Desconhecida')[:30]}...' -> Erro: {e}")

    conn.commit()
    conn.close()

    print(f"\n[+] MIGRAÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"[+] {contador} questões antigas foram estruturadas no banco relacional '{ARQUIVO_DB}'.")

if __name__ == "__main__":
    migrar_dados()
