import sqlite3
import os
import time

# Estética Cyberpunk/SOC
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
CIANO = '\033[96m'
RESET = '\033[0m'
NEGRITO = '\033[1m'

DB_PATH = "cyberops_soc.db"

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner():
    print(f"{VERMELHO}{NEGRITO}")
    print(r"  ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗")
    print(r" ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝")
    print(r" ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝███████╗")
    print(r" ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔═══╝ ╚════██║")
    print(r" ╚██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝██║     ███████║")
    print(r"  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝")
    print(f"{CIANO}        [ SECURITY OPERATIONS CENTER - TERMINAL ENGINE V5.0 ]        {RESET}")
    print(f"{AZUL}{'='*70}{RESET}")

def obter_modulos(cursor):
    cursor.execute("SELECT modulo_id, numero_modulo, nome_modulo FROM tb_modulos_curso ORDER BY modulo_id")
    return cursor.fetchall()

def visualizar_historico():
    limpar()
    exibir_banner()
    print(f"{AMARELO}{NEGRITO}>>> HISTÓRICO DAS ÚLTIMAS 10 SESSÕES DE TREINAMENTO <<<{RESET}\n")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT m.nome_modulo, p.total_questoes, p.acertos, p.data_sessao 
        FROM tb_progresso_estudos p
        JOIN tb_modulos_curso m ON p.modulo_id = m.modulo_id
        ORDER BY p.data_sessao DESC LIMIT 10
    ''')
    sessoes = cursor.fetchall()
    
    if not sessoes:
        print(f"  {VERMELHO}[!] Nenhum registro encontrado. Vá estudar, recruta!{RESET}")
    else:
        print(f"  {'DATA/HORA':<18} | {'MÓDULO':<25} | {'ACERTOS':<8} | {'%':<5}")
        print("  " + "-" * 65)
        for mod, total, acertos, data in sessoes:
            perc = (acertos/total)*100
            cor = VERDE if perc >= 80 else AMARELO
            print(f"  {data[5:16]:<18} | {mod[:25]:<25} | {acertos}/{total:<6} | {cor}{perc:>5.1f}%{RESET}")
            
    conn.close()
    input(f"\n{CIANO}Pressione ENTER para voltar ao menu...{RESET}")

def gerenciar_limite_historico(cursor):
    """Garante que apenas os 10 registros mais recentes permaneçam no banco."""
    cursor.execute('''
        DELETE FROM tb_progresso_estudos 
        WHERE sessao_id NOT IN (
            SELECT sessao_id FROM tb_progresso_estudos 
            ORDER BY data_sessao DESC LIMIT 10
        )
    ''')

def executar_quiz(modulo_id, nome_modulo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao FROM tb_questoes_quiz WHERE modulo_id = ?", (modulo_id,))
    questoes = cursor.fetchall()
    
    if not questoes:
        print(f"\n{VERMELHO}[!] Módulo sem questões cadastradas.{RESET}")
        time.sleep(1.5)
        return

    acertos = 0
    erros = 0
    total = len(questoes)
    
    for i, (pergunta, a, b, c, d, correta, explicacao) in enumerate(questoes, 1):
        limpar()
        exibir_banner()
        print(f"{CIANO}SESSÃO ATUAL: {nome_modulo}{RESET}")
        print(f"{AMARELO}PROGRESSO: {i}/{total} | ACERTOS: {VERDE}{acertos}{RESET} | ERROS: {VERMELHO}{erros}{RESET}\n")
        
        print(f"{NEGRITO}{pergunta}{RESET}\n")
        print(f" {a}\n {b}\n {c}\n {d}\n")
        
        resp = input(f"{AZUL}RESPOSTA > {RESET}").strip().upper()
        
        if resp == correta:
            print(f"\n{VERDE}{NEGRITO}[✓] POSITIVO! Resposta correta.{RESET}")
            acertos += 1
        else:
            print(f"\n{VERMELHO}{NEGRITO}[✗] NEGATIVO! Resposta incorreta.{RESET}")
            print(f"O correto seria: {correta}")
            erros += 1
        
        if explicacao:
            print(f"\n{AMARELO}ANALISTA SOC:> {RESET}{explicacao}")
            
        input(f"\n{CIANO}Pressione ENTER para prosseguir...{RESET}")

    # Salva e limpa o banco
    cursor.execute("INSERT INTO tb_progresso_estudos (modulo_id, total_questoes, acertos) VALUES (?, ?, ?)", (modulo_id, total, acertos))
    gerenciar_limite_historico(cursor)
    conn.commit()
    conn.close()
    
    limpar()
    exibir_banner()
    print(f"{CIANO}SIMULADO FINALIZADO!{RESET}")
    print(f"Aproveitamento: {(acertos/total)*100:.2f}%")
    input("\nENTER para retornar...")

def menu():
    while True:
        limpar()
        exibir_banner()
        
        if not os.path.exists(DB_PATH):
            print(f"{VERMELHO}[!] Erro crítico: Banco de dados não detectado!{RESET}")
            break

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        modulos = obter_modulos(cursor)
        conn.close()

        print(f"{NEGRITO}SELECIONE UMA OPERAÇÃO:{RESET}\n")
        print(f" {VERDE}[H]{RESET} - Visualizar Histórico de Exames (Top 10)")
        print(f" {VERMELHO}[S]{RESET} - Encerrar Sistema")
        print("-" * 30)
        
        for m in modulos:
            print(f" [{m[1]}] - {m[2]}")
        
        opcao = input(f"\n{AZUL}COMANDO > {RESET}").strip().upper()
        
        if opcao == 'S': break
        if opcao == 'H': 
            visualizar_historico()
            continue
            
        selecionado = next((m for m in modulos if m[1] == opcao.zfill(2)), None)
        if selecionado:
            executar_quiz(selecionado[0], selecionado[2])
        else:
            print(f"{VERMELHO}Opção inválida!{RESET}")
            time.sleep(0.8)

if __name__ == "__main__":
    menu()
