import requests
import json

# URL da nossa API Java
API_URL = "http://localhost:8080/api/v1/threats"

# Simulando um ataque de força bruta que o Python detectou
ataque_detectado = {
    "ipOrigem": "172.16.254.1",
    "tentativasFalhas": 99,
    "statusResolucao": "BLOQUEADO_VIA_API",
    "ferramentaOrigem": "python_sensor_v2"
}

print(f"[*] Enviando alerta de ameaça para o API Gateway (Java)...")

try:
    # Fazendo a requisição HTTP POST
    resposta = requests.post(API_URL, json=ataque_detectado)
    
    # Verificando se a API aceitou
    if resposta.status_code == 200:
        print("\033[92m[✓] SUCESSO! A API processou e salvou o ataque.\033[0m")
        print("Retorno do Java:")
        print(json.dumps(resposta.json(), indent=2))
    else:
        print(f"\033[91m[X] Erro na API. Status: {resposta.status_code}\033[0m")

except Exception as e:
    print(f"\033[91m[!] O servidor Java está rodando? Erro de conexão: {e}\033[0m")
