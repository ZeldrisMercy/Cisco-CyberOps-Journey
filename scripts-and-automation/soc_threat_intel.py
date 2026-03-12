import requests
import json
import time

# ==========================================
# CONFIGURAÇÕES DO SOC
# ==========================================
ABUSEIPDB_API_KEY = "10876350a2794321b03ebe9dbf2c109337d387983263c935dc27f481eb79b9a3e3dab04120544e75" 
JAVA_API_URL = "http://localhost:8080/api/v1/threats"

# Vamos simular que o seu firewall detectou esses 3 IPs tentando acessar sua rede
ips_suspeitos = ["118.25.6.39", "8.8.8.8", "185.153.199.117"] 
# Dica: O 8.8.8.8 é o DNS do Google (limpo). Os outros são conhecidos por ataques.

def verificar_reputacao(ip):
    """Consulta o IP no AbuseIPDB para saber se é um atacante conhecido."""
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': ABUSEIPDB_API_KEY
    }
    
    print(f"[*] Analisando IP: {ip} no AbuseIPDB...")
    resposta = requests.get(url, headers=headers, params=querystring)
    
    if resposta.status_code == 200:
        dados = resposta.json()['data']
        score = dados['abuseConfidenceScore']
        pais = dados['countryCode']
        print(f"    -> Score de Risco: {score}% | País: {pais}")
        return score
    else:
        print(f"    [!] Erro ao consultar a API do AbuseIPDB. Status: {resposta.status_code}")
        return 0

def enviar_para_java(ip, score):
    """Envia o IP malicioso para o nosso Gateway em Java salvar no banco."""
    # Só vamos bloquear se a chance de ser hacker for maior que 50%
    if score > 50:
        print(f"\033[91m[!] AMEAÇA CONFIRMADA! Risco de {score}%. Enviando para o Gateway Java...\033[0m")
        
        ataque_detectado = {
            "ipOrigem": ip,
            "tentativasFalhas": score, # Usando o score como base de tentativas para o teste
            "statusResolucao": "BLOQUEADO_VIA_INTEL",
            "ferramentaOrigem": "abuseipdb_sensor_v1"
        }
        
        try:
            res = requests.post(JAVA_API_URL, json=ataque_detectado)
            if res.status_code == 200:
                print("\033[92m    [✓] IP salvo com sucesso no banco de dados corporativo.\033[0m\n")
        except Exception as e:
            print(f"    [X] Erro ao contatar a API Java: {e}\n")
    else:
        print(f"\033[92m[✓] IP Limpo ou com risco baixo ({score}%). Nenhuma ação necessária.\033[0m\n")

# ==========================================
# INÍCIO DA OPERAÇÃO
# ==========================================
print("=== INICIANDO MOTOR DE THREAT INTELLIGENCE ===\n")
for ip in ips_suspeitos:
    score_risco = verificar_reputacao(ip)
    enviar_para_java(ip, score_risco)
    time.sleep(1) # Pausa dramática para não sobrecarregar a rede
