import re
import subprocess
import platform
import logging
import os
from collections import Counter
from datetime import datetime

# CONFIGURAÇÕES INICIAIS
LOG_FONTE = "auth_test.log"
ARQUIVO_BLOQUEADOS = "ips_bloqueados.log"
LIMIAR_FALHAS = 5
WHITELIST = ["127.0.0.1", "192.168.1.1"]

# Configuração de Auditoria
logging.basicConfig(filename=ARQUIVO_BLOQUEADOS, level=logging.INFO, 
                    format='%(asctime)s - [SOC] - %(message)s')

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerenciar_whitelist():
    limpar()
    print("--- GESTÃO DE WHITELIST ---")
    print(f"IPs atuais: {WHITELIST}")
    novo_ip = input("\nDigite o IP para adicionar (ou ENTER para voltar): ").strip()
    if novo_ip:
        WHITELIST.append(novo_ip)
        print(f"[+] {novo_ip} adicionado com sucesso!")
        import time
        time.sleep(1)

def executar_bloqueio(ip, modo_real):
    sistema = platform.system()
    if sistema == "Linux":
        comando = f"sudo iptables -A INPUT -s {ip} -j DROP"
    else:
        comando = f"netsh advfirewall firewall add rule name='SOC_BLOCK_{ip}' dir=in action=block remoteip={ip}"

    if not modo_real:
        print(f"    [MODO TESTE] Ignorando execução real. Comando seria: {comando}")
    else:
        try:
            # Executa o comando no SO
            subprocess.run(comando, shell=True, check=True, capture_output=True)
            print(f"    [SUCESSO] IP {ip} bloqueado no Firewall do {sistema}.")
            logging.info(f"BLOQUEIO REAL: IP {ip} via {sistema} Firewall.")
        except subprocess.CalledProcessError:
            print(f"    [ERRO] Falha ao bloquear {ip}. Execute como Administrador/Sudo.")

def processar_logs(modo_real):
    limpar()
    tipo = "VALENDO (PRODUÇÃO)" if modo_real else "TESTE (SIMULAÇÃO)"
    print(f"=== INICIANDO VARREDURA: MODO {tipo} ===\n")
    
    try:
        with open(LOG_FONTE, 'r') as f:
            dados = f.read()
        
        # Regex (Módulo 4 Linux)
        tentativas = re.findall(r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", dados)
        relatorio = Counter(tentativas)

        for ip, total in relatorio.items():
            if ip in WHITELIST:
                print(f"[!] {ip:<15} | Falhas: {total} -> IGNORADO (Whitelist)")
                continue

            if total >= LIMIAR_FALHAS:
                print(f"[🔴] {ip:<15} | Falhas: {total} -> STATUS: BLOQUEAR")
                executar_bloqueio(ip, modo_real)
            else:
                print(f"[🟡] {ip:<15} | Falhas: {total} -> STATUS: MONITORANDO")
                
    except FileNotFoundError:
        print(f"[ERRO] Arquivo {LOG_FONTE} não encontrado.")
    
    input("\nProcessamento concluído. Pressione ENTER para voltar ao menu...")

def menu():
    while True:
        limpar()
        print("==========================================")
        print("       SOC IPS UNIT - ACTIVE RESPONSE     ")
        print("==========================================")
        print("1. [Módulo de Teste] Simular Bloqueios")
        print("2. [Módulo Real] Executar Bloqueios no Firewall")
        print("3. Gerenciar Whitelist (Lista Branca)")
        print("0. Sair")
        
        opcao = input("\nSelecione uma opção: ").strip()

        if opcao == '1':
            processar_logs(modo_real=False)
        elif opcao == '2':
            confirmar = input("⚠ AVISO: Isso alterará as regras do seu Firewall. Continuar? (s/n): ")
            if confirmar.lower() == 's':
                processar_logs(modo_real=True)
        elif opcao == '3':
            gerenciar_whitelist()
        elif opcao == '0':
            break

if __name__ == "__main__":
    menu()
