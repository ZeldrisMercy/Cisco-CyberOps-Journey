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
            |___/ |_|        TERMINAL OPS CENTER v3.0
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

def executar_quiz(questoes, modo_selecionado="GERAL"):
    pontuacao = 0
    puladas = 0
    total = len(questoes)
    random.shuffle(questoes)

    for idx, q in enumerate(questoes, 1):
        limpar_ecra()
        exibir_banner()
        print(f" {NEGRITO}MODO:{RESET} {CIANO}{modo_selecionado}{RESET}")
        print(f" {barra_progresso(idx-1, total)}")
        print(f"\n {NEGRITO}DOMÍNIO:{RESET} {AMARELO}{q['dominio']}{RESET}")
        print(f" {NEGRITO}QUESTÃO {idx} de {total}{RESET} | {VERDE}Acertos: {pontuacao}{RESET}\n")
        print(f" {CIANO}» {q['pergunta']}{RESET}\n")
        
        for opcao in q['opcoes']:
            print(f"   {opcao}")
            
        print(f"\n {AMARELO}[Dicas: 'P' para Pular | 'SAIR' para Encerrar]{RESET}")
        user_input = input(f" {NEGRITO}Sua resposta:{RESET} ").strip().upper()

        if user_input == 'SAIR':
            return None
        
        if user_input == 'P':
            puladas += 1
            print(f"\n {AMARELO}Questão pulada. A resposta era: {q['resposta_correta']}{RESET}")
            time.sleep(1.5)
            continue

        while user_input not in ['A', 'B', 'C', 'D']:
            print(f" {VERMELHO}Escolha A, B, C, D ou P.{RESET}")
            user_input = input(f" Sua resposta: ").strip().upper()
            if user_input == 'SAIR': return None
            if user_input == 'P': break
        
        if user_input == 'P': 
            puladas += 1
            continue

        if user_input == q['resposta_correta']:
            print(f"\n {VERDE}{NEGRITO}✅ ANÁLISE CORRETA!{RESET}")
            pontuacao += 1
        else:
            print(f"\n {VERMELHO}{NEGRITO}❌ ALERTA: RESPOSTA INCORRETA.{RESET}")
            print(f" {NEGRITO}Gabarito:{RESET} {VERDE}{q['resposta_correta']}{RESET}")
            
        print(f"\n {CIANO}{NEGRITO}INTELIGÊNCIA TÁTICA:{RESET}\n {q['explicacao']}")
        print(f"\n{AZUL}----------------------------------------------------------{RESET}")
        input(" Pressione ENTER para prosseguir...")

    return pontuacao, puladas, total

def escolher_modulo(todas_questoes):
    modulos = sorted(list(set([q['dominio'].split(' - ')[0] for q in todas_questoes])))
    
    while True:
        limpar_ecra()
        exibir_banner()
        print(f"  {NEGRITO}ESCOLHA O MÓDULO DE TREINAMENTO:{RESET}\n")
        for i, mod in enumerate(modulos, 1):
            print(f"  {NEGRITO}{i}.{RESET} {mod}")
        print(f"  {NEGRITO}0.{RESET} Voltar")
        
        opcao = input(f"\n  {CIANO}Seleção:{RESET} ").strip()
        
        if opcao == '0':
            return None
        
        try:
            idx = int(opcao) - 1
            if 0 <= idx < len(modulos):
                filtro = modulos[idx]
                selecionadas = [q for q in todas_questoes if q['dominio'].startswith(filtro)]
                return selecionadas, filtro
        except:
            pass

def menu_principal():
    while True:
        limpar_ecra()
        exibir_banner()
        print(f"  {NEGRITO}1.{RESET} Simulado Completo (100 Questões)")
        print(f"  {NEGRITO}2.{RESET} Escolher Módulo Específico")
        print(f"  {NEGRITO}0.{RESET} Sair do Terminal")
        
        opcao = input(f"\n  {CIANO}Selecione uma opção:{RESET} ").strip()

        questoes_base = carregar_questoes('questoes_cbrops.json')
        if not questoes_base: break

        if opcao == '1':
            res = executar_quiz(questoes_base, "FULL SCAN")
            if res:
                exibir_resultado(res)
        elif opcao == '2':
            selecao = escolher_modulo(questoes_base)
            if selecao:
                q_filtradas, nome_mod = selecao
                res = executar_quiz(q_filtradas, nome_mod)
                if res:
                    exibir_resultado(res)
        elif opcao == '0':
            print(f"\n  {AMARELO}Logoff efetuado com sucesso.{RESET}")
            break

def exibir_resultado(resultado):
    pontos, pulos, total = resultado
    limpar_ecra()
    exibir_banner()
    print(f"\n {NEGRITO}RELATÓRIO DE MISSÃO FINALIZADO{RESET}")
    print(f" {AZUL}--------------------------------{RESET}")
    print(f" Acertos: {VERDE}{pontos}{RESET}")
    print(f" Puladas: {AMARELO}{pulos}{RESET}")
    print(f" Erros:   {VERMELHO}{total - pontos - pulos}{RESET}")
    print(f" Total:   {total}")
    input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    menu_principal()
