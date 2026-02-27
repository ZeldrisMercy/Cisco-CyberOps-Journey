import re
from collections import Counter

# Padrão para capturar IPs em tentativas de login falhas
# Exemplo de linha: Feb 27 02:30:01 server sshd[123]: Failed password for root from 192.168.1.50 port 54321 ssh2
REGEX_IP = r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

def analisar_tentativas_invasao(arquivo_log):
    print(f"\n[+] Iniciando varredura forense: {arquivo_log}")
    
    try:
        with open(arquivo_log, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        # Extrai todos os IPs que falharam no login
        ips_encontrados = re.findall(REGEX_IP, conteudo)
        contagem = Counter(ips_encontrados)
        
        if not ips_encontrados:
            print("[-] Nenhum padrão de ataque detectado.")
            return

        print(f"[!] Alerta: {len(ips_encontrados)} tentativas de Força Bruta detectadas!\n")
        print(f"{'IP DO ATACANTE':<20} | {'TENTATIVAS'}")
        print("-" * 35)

        # Filtra IPs com mais de 3 tentativas (Comportamento Suspeito)
        for ip, total in contagem.items():
            status = " [CRÍTICO]" if total > 5 else ""
            print(f"{ip:<20} | {total}{status}")
            
    except FileNotFoundError:
        print(f"[ERRO] Arquivo {arquivo_log} não encontrado.")

if __name__ == "__main__":
    analisar_tentativas_invasao("auth_test.log")
