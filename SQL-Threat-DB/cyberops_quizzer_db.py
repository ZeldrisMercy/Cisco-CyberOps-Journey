import sqlite3
import os
import time

# Estética SOC
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
CIANO = '\033[96m'
RESET = '\033[0m'

DB_PATH = "cyberops_soc.db"

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_modulos(cursor):
    """Busca dinamicamente os módulos cadastrados no banco."""
    cursor.execute("SELECT modulo_id, numero_modulo, nome_modulo FROM tb_modulos_curso ORDER BY modulo_id")
    return cursor.fetchall()

def executar_quiz(modulo_id, nome_modulo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Busca as questões específicas do módulo escolhido
    cursor.execute("""
        SELECT pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao 
        FROM tb_questoes_quiz 
        WHERE modulo_id = ?
    """, (modulo_id,))
    
    questoes = cursor.fetchall()
    
    if not questoes:
        print(f"\n{AMARELO}[!] Nenhuma questão cadastrada para este módulo ainda.{RESET}")
        time.sleep(2)
        return

    acertos = 0
    total = len(questoes)
    
    limpar()
    print(f"{CIANO}=== INICIANDO SIMULADO: MÓDULO {nome_modulo} ==={RESET}\n")
    
    for i, q in enumerate(questoes, 1):
        pergunta, a, b, c, d, correta, explicacao = q
        
        print(f"{AZUL}[Questão {i}/{total}]{RESET} {pergunta}\n")
        print(f"  {a}")
        print(f"  {b}")
        print(f"  {c}")
        print(f"  {d}\n")
        
        resposta = input(f"Comando (A/B/C/D ou 'S' p/ sair) > ").strip().upper()
        
        if resposta == 'S':
            print("\n[!] Simulado abortado pelo operador.")
            break
            
        if resposta == correta:
            print(f"{VERDE}[✓] CORRETO!{RESET}\n")
            acertos += 1
        else:
            print(f"{VERMELHO}[✗] INCORRETO.{RESET} A resposta certa era: {correta}")
            if explicacao:
                print(f"💡 {AMARELO}Explicação: {explicacao}{RESET}\n")
            
        input("Pressione ENTER para a próxima...")
        limpar()

    # DML: Gravação do progresso de estudos no banco de dados
    if resposta != 'S':
        cursor.execute('''
            INSERT INTO tb_progresso_estudos (modulo_id, total_questoes, acertos)
            VALUES (?, ?, ?)
        ''', (modulo_id, total, acertos))
        conn.commit()
        
        aproveitamento = (acertos / total) * 100
        print(f"{CIANO}=== RELATÓRIO DO SIMULADO ==={RESET}")
        print(f"Módulo alvo: {nome_modulo}")
        print(f"Pontuação final: {acertos}/{total} ({aproveitamento:.1f}%)")
        
        if aproveitamento >= 80:
            print(f"{VERDE}Status: APROVADO - Nível tático atingido.{RESET}")
        else:
            print(f"{AMARELO}Status: REVISÃO RECOMENDADA.{RESET}")
        
        print(f"\n[+] Progresso salvo no banco de dados com sucesso.")
        input("\nPressione ENTER para voltar ao Centro de Comando...")

    conn.close()

def menu():
    while True:
        limpar()
        print(f"{VERMELHO}")
        print(" ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗")
        print("██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝")
        print("██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝███████╗")
        print("██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔═══╝ ╚════██║")
        print("╚██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝██║     ███████║")
        print(" ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝")
        print(f"{RESET}")
        print(f"{CIANO}        DB QUIZZER ENGINE v4.0 - SQL POWERED        {RESET}")
        print("=" * 60)
        
        if not os.path.exists(DB_PATH):
            print(f"{VERMELHO}[!] Banco de dados não encontrado. Rode o db_migrator.py primeiro.{RESET}")
            break

        # Traz os módulos dinamicamente do banco
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        modulos = obter_modulos(cursor)
        conn.close()

        print("Selecione o módulo para iniciar a varredura:\n")
        for m in modulos:
            # Formata para mostrar o número exato ex: [01] - The Danger
            print(f" [{m[1]}] - {m[2]}")
            
        print("\n [00] - Desligar Sistema")
        
        opcao = input("\nComando > ").strip()
        
        if opcao == '00' or opcao == '0':
            break
            
        # Busca o módulo escolhido na lista
        modulo_selecionado = next((m for m in modulos if m[1] == opcao.zfill(2)), None)
        
        if modulo_selecionado:
            executar_quiz(modulo_selecionado[0], modulo_selecionado[2])
        else:
            print(f"{VERMELHO}[!] Módulo inválido ou não cadastrado.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    menu()
