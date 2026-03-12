import sqlite3
import os

# Estética SOC
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
CIANO = '\033[96m'
RESET = '\033[0m'

DB_PATH = "cyberops_soc.db"

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_relatorios():
    limpar()
    print(f"{CIANO}===================================================={RESET}")
    print(f"{CIANO}       SOC TELEMETRY & STUDY ANALYTICS DASHBOARD      {RESET}")
    print(f"{CIANO}===================================================={RESET}\n")
    
    if not os.path.exists(DB_PATH):
        print(f"{VERMELHO}[!] Banco de dados não encontrado.{RESET}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ---------------------------------------------------------
    # MÉTRICA 1: Progresso de Estudos (Últimas Sessões)
    # ---------------------------------------------------------
    print(f"{AMARELO}[1] HISTÓRICO DE SIMULADOS (Últimas 5 sessões){RESET}")
    cursor.execute('''
        SELECT m.nome_modulo, p.total_questoes, p.acertos, p.data_sessao 
        FROM tb_progresso_estudos p
        JOIN tb_modulos_curso m ON p.modulo_id = m.modulo_id
        ORDER BY p.data_sessao DESC LIMIT 5
    ''')
    sessoes = cursor.fetchall()
    
    if not sessoes:
        print("  [!] Nenhum simulado registrado no banco ainda.\n")
    else:
        print(f"  {'DATA/HORA':<18} | {'MÓDULO':<30} | {'SCORE':<7} | {'STATUS'}")
        print("  " + "-" * 75)
        for s in sessoes:
            modulo, total, acertos, data = s
            aproveitamento = (acertos / total) * 100 if total > 0 else 0
            cor = VERDE if aproveitamento >= 80 else AMARELO
            status = "APROVADO" if aproveitamento >= 80 else "REVISAR"
            print(f"  {data[:16]:<18} | {modulo[:30]:<30} | {acertos}/{total:<4} | {cor}{aproveitamento:.1f}% ({status}){RESET}")
    print("\n" + "=" * 60 + "\n")

    # ---------------------------------------------------------
    # MÉTRICA 2: Top Ameaças (Logs do SOC)
    # ---------------------------------------------------------
    print(f"{AMARELO}[2] TOP IPs ATACANTES (Threat Intel Database){RESET}")
    cursor.execute('''
        SELECT ip_origem, COUNT(*) as total_incidentes, SUM(tentativas_falhas)
        FROM tb_threat_logs
        WHERE status_resolucao != 'WHITELIST'
        GROUP BY ip_origem
        ORDER BY SUM(tentativas_falhas) DESC LIMIT 3
    ''')
    ameacas = cursor.fetchall()
    
    if not ameacas:
        print("  [!] Nenhuma ameaça registrada na base.\n")
    else:
        print(f"  {'IP ORIGEM':<16} | {'INCIDENTES':<12} | {'TOTAL DE FALHAS (BRUTEFORCE)'}")
        print("  " + "-" * 65)
        for a in ameacas:
            print(f"  {VERMELHO}{a[0]:<16}{RESET} | {a[1]:<12} | {a[2]}")
            
    conn.close()
    input(f"\n{CIANO}Pressione ENTER para retornar ao Centro de Comando...{RESET}")

if __name__ == "__main__":
    mostrar_relatorios()
