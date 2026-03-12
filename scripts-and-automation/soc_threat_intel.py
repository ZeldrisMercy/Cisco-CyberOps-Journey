import requests
import json
import time

# ==========================================
# CONFIGURAÇÕES DO SOC
# ==========================================
ABUSEIPDB_API_KEY = "10876350a2794321b03ebe9dbf2c109337d387983263c935dc27f481eb79b9a3e3dab04120544e75" 
JAVA_API_URL = "http://localhost:8080/api/v1/threats"

# --- NOVAS CREDENCIAIS DO TELEGRAM ---
TELEGRAM_TOKEN = "8652012151:AAE_A5IGAujJazDB8sAIJyf6j-LRq5kDua0"
TELEGRAM_CHAT_ID = "5633129982"

ips_suspeitos = ["79.124.40.174", "8.8.8.8", "88.216.214.115", "83.111.76.194"]

def enviar_alerta_telegram(ip, pais, score):
    """Dispara um alerta em tempo real para o celular do analista."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    # Formatando a mensagem com estilo (Negrito e Monospace)
    mensagem = (
        f"🚨 *ALERTA CRÍTICO SOC* 🚨\n\n"
        f"🛡️ *Ameaça:* Tentativa de Invasão\n"
        f"🌐 *Origem:* `{ip}`\n"
        f"📍 *País:* {pais}\n"
        f"🔥 *Risco:* {score}%\n\n"
        f"✅ _Ação: IP bloqueado e registrado no Gateway Java._"
    )
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown" # Permite usar formatação bonita
    }
    
    try:
        requests.post(url, json=payload)
        print("    📱 [!] Alerta disparado para o celular do analista.")
    except Exception as e:
        print(f"    📱 [X] Falha ao enviar Telegram: {e}")

def verificar_reputacao(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}
    headers = {'Accept': 'application/json', 'Key': ABUSEIPDB_API_KEY}
    
    print(f"[*] Analisando IP: {ip} no AbuseIPDB...")
    resposta = requests.get(url, headers=headers, params=querystring)
    
    if resposta.status_code == 200:
        dados = resposta.json()['data']
        score = dados['abuseConfidenceScore']
        pais = dados['countryCode']
        print(f"    -> Score de Risco: {score}% | País: {pais}")
        return score, pais # Agora retornamos o país também
    return 0, "Unknown"

def enviar_para_java(ip, score, pais):
    if score > 50:
        print(f"\033[91m[!] AMEAÇA CONFIRMADA! Risco de {score}%. Enviando para o Gateway Java...\033[0m")
        ataque_detectado = {
            "ipOrigem": ip,
            "tentativasFalhas": score,
            "statusResolucao": "BLOQUEADO_VIA_INTEL",
            "ferramentaOrigem": "abuseipdb_sensor_v1"
        }
        try:
            res = requests.post(JAVA_API_URL, json=ataque_detectado)
            if res.status_code == 200:
                print("\033[92m    [✓] IP salvo com sucesso no banco corporativo.\033[0m")
                enviar_alerta_telegram(ip, pais, score) # <--- CHAMA O ALARME AQUI!
        except Exception as e:
            print(f"    [X] Erro ao contatar a API Java: {e}")
    else:
        print(f"\033[92m[✓] IP Limpo ou com risco baixo ({score}%). Nenhuma ação necessária.\033[0m\n")

# ==========================================
# INÍCIO DA OPERAÇÃO
# ==========================================
print("=== INICIANDO MOTOR DE THREAT INTELLIGENCE ===\n")
for ip in ips_suspeitos:
    score_risco, pais_origem = verificar_reputacao(ip)
    enviar_para_java(ip, score_risco, pais_origem)
    time.sleep(1)
