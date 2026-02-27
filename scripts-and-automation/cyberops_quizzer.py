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
      ____           _                   ____             
     / ___| _   _  _| |__   ___  _ __  / ___|  ___   ___ 
    | |    | | | || | '_ \ / _ \| '__| \___ \ / _ \ / __|
    | |___ | |_| || || |_)|| __/| |     ___) | (_) | (__ 
     \____| \__, || |_.__/ \___||_|    |____/ \___/ \___|
            |___/         TERMINAL OPS CENTER v3.1
    ==========================================================
    """ + RESET)

def carregar_questoes(ficheiro_json):
    try:
        # 'utf-8-sig' limpa o erro de 'char 2' causado pelo Windows
        with open(ficheiro_json, 'r', encoding='utf-8-sig') as f:
            conteudo = f.read().strip()
            if not conteudo:
                print(f"{VERMELHO}[ERRO] O arquivo JSON está vazio.{RESET}")
                return None
            return json.loads(conteudo)
    except json.JSONDecodeError as e:
        print(f"{VERMELHO}[ERRO DE SINTAXE NO JSON]{RESET}")
        print(f"Linha: {e.lineno}, Coluna: {e.colno}")
        print(f"Mensagem: {e.msg}")
        print(f"{AMARELO}Dica: Verifique se falta uma vírgula entre as questões ou se há uma vírgula sobrando no final.{RESET}")
        input("\nPressione ENTER para tentar corrigir...")
        return None
    except Exception as e:
        print(f"{VERMELHO}[ERRO CRÍTICO]: {e}{RESET}")
        return None

def barra_progresso(atual, total):
    largura = 30
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

        if user_input == 'SAIR': return None
        
        if user_input == 'P':
            puladas += 1
            print(f"\n {AMARELO}Questão pulada. Gabarito: {q['resposta_correta']}{RESET}")
            time.sleep(2)
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

def menu_principal():
    while True:
        limpar_ecra()
        exibir_banner()
        print(f"  {NEGRITO}1.{RESET} Simulado Completo (100 Questões)")
        print(f"  {NEGRITO}2.{RESET} Escolher Módulo Específico")
        print(f"  {NEGRITO}0.{RESET} Sair do Terminal")
        
        opcao = input(f"\n  {CIANO}Selecione uma opção:{RESET} ").strip()

        questoes_base = carregar_questoes('questoes_cbrops.json')
        if not questoes_base and opcao != '0':
            input("\nCorrija o arquivo JSON e pressione ENTER...")
            continue

        if opcao == '1':
            res = executar_quiz(questoes_base, "FULL SCAN")
            if res: exibir_resultado(res)
        elif opcao == '2':
            selecao = escolher_modulo(questoes_base)
            if selecao:
                res = executar_quiz(selecao[0], selecao[1])
                if res: exibir_resultado(res)
        elif opcao == '0':
            break

def escolher_modulo(todas_questoes):
    # Extrai os prefixos dos módulos para o menu
    prefixos = sorted(list(set([q['dominio'].split(' - ')[0] for q in todas_questoes])))
    limpar_ecra()
    exibir_banner()
    for i, p in enumerate(prefixos, 1):
        print(f"  {NEGRITO}{i}.{RESET} {p}")
    
    op = input(f"\n  {CIANO}Escolha o módulo:{RESET} ")
    try:
        escolhido = prefixos[int(op)-1]
        return [q for q in todas_questoes if q['dominio'].startswith(escolhido)], escolhido
    except:
        return None

def exibir_resultado(resultado):
    pontos, pulos, total = resultado
    limpar_ecra()
    exibir_banner()
    print(f"\n {NEGRITO}RELATÓRIO DE MISSÃO FINALIZADO{RESET}")
    print(f" Acertos: {VERDE}{pontos}{RESET} | Puladas: {AMARELO}{pulos}{RESET} | Erros: {VERMELHO}{total-pontos-pulos}{RESET}")
    input("\nPressione ENTER para voltar...")

if __name__ == "__main__":
    menu_principal()
