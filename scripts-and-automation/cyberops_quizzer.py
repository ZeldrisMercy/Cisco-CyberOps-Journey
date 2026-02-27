import json
import random
import os
import time

# Códigos de cor ANSI para o terminal
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_questoes(ficheiro_json):
    try:
        with open(ficheiro_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{VERMELHO}[Erro] O ficheiro {ficheiro_json} não foi encontrado.{RESET}")
        return None

def executar_quiz(questoes):
    pontuacao = 0
    total = len(questoes)
    
    # Baralhar as questões para não ser sempre a mesma ordem
    random.shuffle(questoes)

    limpar_ecra()
    print(f"{AZUL}===================================================={RESET}")
    print(f"{AZUL}🛡️  CYBEROPS ASSOCIATE (200-201) - CLI QUIZZER  🛡️{RESET}")
    print(f"{AZUL}===================================================={RESET}\n")
    print("Pressiona ENTER para começar o simulacro de SOC...")
    input()

    for idx, q in enumerate(questoes, 1):
        limpar_ecra()
        print(f"{AMARELO}[Questão {idx}/{total}] Domínio: {q['dominio']}{RESET}\n")
        print(f"{q['pergunta']}\n")
        
        for opcao in q['opcoes']:
            print(opcao)
            
        resposta_user = input("\nA tua resposta (A/B/C/D): ").strip().upper()

        print("\nProcessando a resposta...")
        time.sleep(1) # Efeito de suspense

        if resposta_user == q['resposta_correta']:
            print(f"{VERDE}✅ ACERTASTE!{RESET}")
            pontuacao += 1
        else:
            print(f"{VERMELHO}❌ ERRASTE.{RESET} A resposta correta era: {q['resposta_correta']}")
            
        print(f"\n{AZUL}💡 Explicação Tática:{RESET} {q['explicacao']}")
        print("\n----------------------------------------------------")
        input("Pressiona ENTER para a próxima questão...")

    # Relatório Final
    limpar_ecra()
    print(f"{AZUL}===================================================={RESET}")
    print(f"📊 RELATÓRIO FINAL DE OPERAÇÕES")
    print(f"{AZUL}===================================================={RESET}")
    print(f"Pontuação: {pontuacao} de {total}")
    
    percentagem = (pontuacao / total) * 100
    if percentagem == 100:
        print(f"{VERDE}Classificação: Tier 3 Threat Hunter. Impecável!{RESET}")
    elif percentagem >= 70:
        print(f"{AMARELO}Classificação: Tier 2 IR Analyst. Bom trabalho, mas requer revisão.{RESET}")
    else:
        print(f"{VERMELHO}Classificação: Tier 1 Triage. O adversário passou pelas defesas. Estuda mais!{RESET}")

if __name__ == "__main__":
    ficheiro_dados = 'questoes_cbrops.json'
    dados_questoes = carregar_questoes(ficheiro_dados)
    
    if dados_questoes:
        executar_quiz(dados_questoes)
