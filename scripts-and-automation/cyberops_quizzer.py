import json
import random
import os
import time

# Paleta de Cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
CIANO = '\033[96m'
NEGRITO = '\033[1m'
RESET = '\033[0m'

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner():
    print(f"{CIANO}{NEGRITO}")
    print(r"""
    ==========================================================
      ____               _                 ____             
     / ___| _   _  _ __ | |__    ___  _ __/ ___|  ___   ___ 
    | |    | | | || '_ \| '_ \  / _ \| '__\___ \ / _ \ / __|
    | |___ | |_| || |_) || |_) ||  __/| |   ___) | (_) | (__ 
     \____| \__, || .__/ |_.__/  \___||_|  |____/ \___/ \___|
            |___/ |_|        TERMINAL OPS CENTER v2.0
    ==========================================================
    """ + RESET)

def carregar_questoes(ficheiro_json):
    try:
        with open(ficheiro_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"{VERMELHO}[ERRO CRÍTICO] Falha ao carregar base de dados: {e}{RESET}")
        return None

def barra_progresso(atual, total):
    largura = 40
    progresso = int((atual / total) * largura)
    barra = "█" * progresso + "-" * (largura - progresso)
    percentual = int((atual / total) * 100)
    return f"{AZUL}[{barra}] {percentual}%{RESET}"

def executar_quiz(questoes):
    pontuacao = 0
    total = len(questoes)
    random.shuffle(questoes)

    for idx, q in enumerate(questoes, 1):
        limpar_ecra()
        exibir_banner()
        print(f" {barra_progresso(idx-1, total)}")
        print(f"\n {NEGRITO}DOMÍNIO:{RESET} {AMARELO}{q['dominio']}{RESET}")
        print(f" {NEGRITO}QUESTÃO {idx} de {total}{RESET}\n")
        print(f" {CIANO}» {q['pergunta']}{RESET}\n")
        
        for opcao in q['opcoes']:
            print(f"   {opcao}")
            
        print(f"\n {AMARELO}[Dica: Digite 'SAIR' para encerrar o teste]{RESET}")
        user_input = input(f" {NEGRITO}Sua resposta (A/B/C/D):{RESET} ").strip().upper()

        if user_input == 'SAIR':
            print(f"\n{AMARELO}Encerrando operações... Até logo, Analista.{RESET}")
            time.sleep(1)
            return None # Sinaliza saída antecipada

        # Validação de entrada
        while user_input not in ['A', 'B', 'C', 'D']:
            print(f" {VERMELHO}Entrada inválida! Escolha A, B, C ou D.{RESET}")
            user_input = input(f" Sua resposta: ").strip().upper()
            if user_input == 'SAIR': return None

        if user_input == q['resposta_correta']:
            print(f"\n {VERDE}{NEGRITO}✅ ANALISE CORRETA!{RESET}")
            pontuacao += 1
        else:
            print(f"\n {VERMELHO}{NEGRITO}❌ ALERTA: RESPOSTA INCORRETA.{RESET}")
            print(f" {NEGRITO}Gabarito:{RESET} {VERDE}{q['resposta_correta']}{RESET}")
            
        print(f"\n {CIANO}{NEGRITO}INTELIGÊNCIA TÁTICA:{RESET}\n {q['explicacao']}")
        print(f"\n{AZUL}----------------------------------------------------------{RESET}")
        input(" Pressione ENTER para prosseguir...")

    return pontuacao

def menu_principal():
    while True:
        limpar_ecra()
        exibir_banner()
        print(f"  {NEGRITO}1.{RESET} Iniciar Simulado CyberOps")
        print(f"  {NEGRITO}2.{RESET} Ver Metodologia de Estudo")
        print(f"  {NEGRITO}0.{RESET} Sair do Terminal")
        
        opcao = input(f"\n  {CIANO}Selecione uma opção:{RESET} ").strip()

        if opcao == '1':
            dados = carregar_questoes('questoes_cbrops.json')
            if dados:
                res = executar_quiz(dados)
                if res is not None:
                    limpar_ecra()
                    exibir_banner()
                    print(f"\n {NEGRITO}FINALIZADO!{RESET}")
                    print(f" Score: {VERDE}{res}{RESET} acertos de {len(dados)}")
                    input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '2':
            limpar_ecra()
            exibir_banner()
            print("  ESTRATÉGIA DE ESTUDO ATIVO:")
            print("  - Baseado no Blueprint oficial 200-201.")
            print("  - Foco em análise baseada em host e rede.")
            input("\nPressione ENTER para voltar...")
        elif opcao == '0':
            print(f"\n  {AMARELO}Logoff efetuado com sucesso.{RESET}")
            break
        else:
            print(f"\n  {VERMELHO}Opção inválida!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()
