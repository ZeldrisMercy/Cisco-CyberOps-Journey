import re
import subprocess
import platform
import json
import os
from collections import Counter
from datetime import datetime

# PALETA DE CORES (Ideal para temas escuros)
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
CIANO = '\033[96m'
RESET = '\033[0m'

LOG_FONTE = "auth_test.log"
WHITELIST = ["127.0.0.1", "192.168.1.1"]

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_relatorio(dados_bloqueio):
    """Gera um log forense em JSON para o analista."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arq = f"relatorio_ataque_{timestamp}.json"
    with open(nome_arq, 'w') as f:
        json.dump(dados_bloqueio, f, indent=4)
    return nome_arq

def executar_bloqueio(ip, modo_real):
    sistema = platform.system()
    comando = f"sudo iptables -A INPUT -s {ip} -j DROP" if sistema == "Linux" else f"netsh advfirewall firewall add rule name='SOC_BLOCK_{ip}' dir=in action=block remoteip={ip}"

    if not modo_real:
        return f"{AMARELO}[SIMULADO]{RESET}"
    else:
        try:
            subprocess.run(comando, shell=True, check=True, capture_output=True)
            return f"{VERDE}[BLOQUEADO]{RESET}"
        except:
            return f"{VERMELHO}[FALHA]{RESET}"

def processar_logs(modo_real):
    limpar()
    print(f"{CIANO}>>> INICIANDO ANÁLISE DE TRÁFEGO HOST-BASED <<<{RESET}\n")
    print(f"{'IP ORIGEM':<18} | {'FALHAS':<8} | {'STATUS':<15}")
    print("-" * 50)
    
    dados_para_json = []

    try:
        with open(LOG_FONTE, 'r') as f:
            dados = f.read()
        
        ips = re.findall(r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", dados)
        relatorio = Counter(ips)

        for ip, total in relatorio.items():
            if ip in WHITELIST:
                print(f"{AZUL}{ip:<18}{RESET} | {total:<8} | {CIANO}[WHITELIST]{RESET}")
                continue

            status = "PENDENTE"
            if total >= 5:
                status = executar_bloqueio(ip, modo_real)
                dados_para_json.append({"ip": ip, "tentativas": total, "data": str(datetime.now())})
                print(f"{VERMELHO}{ip:<18}{RESET} | {total:<8} | {status}")
            else:
                print(f"{ip:<18} | {total:<8} | {AMARELO}[SUSPEITO]{RESET}")

        if dados_para_json and modo_real:
            arq = salvar_relatorio(dados_para_json)
            print(f"\n{VERDE}[✓] Relatório Forense gerado: {arq}{RESET}")
                
    except FileNotFoundError:
        print(f"{VERMELHO}[!] Erro: Arquivo de log não encontrado.{RESET}")
    
    input("\nPressione ENTER para voltar ao Centro de Comando...")

def menu():
    while True:
        limpar()
        print(f"{VERMELHO}")
        print(" ██████  ██████  ██████   ██████  ██████  ██████ ")
        print(" ██      ██  ██  ██  ██  ██  ██  ██  ██  ██      ")
        print(" ██████  ██  ██  ██      ██  ██  ██████  ██████ ")
        print("     ██  ██  ██  ██  ██  ██  ██  ██          ██ ")
        print(" ██████  ██████  ██████   ██████  ██      ██████ ")
        print(f"        S O C  -  I P S  U N I T {RESET}")
        print("-" * 45)
        print(f"1. {AMARELO}[Módulo de Teste]{RESET} Analisar e Simular")
        print(f"2. {VERMELHO}[Módulo Real]{RESET} Bloquear Ameaças")
        print("0. Desligar Sistema")
        
        op = input("\nComando > ")
        if op == '1': processar_logs(False)
        elif op == '2': processar_logs(True)
        elif op == '0': break

if __name__ == "__main__":
    menu()
