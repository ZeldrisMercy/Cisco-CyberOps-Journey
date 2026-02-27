import hashlib
import os
import time

# Estética SOC
CIANO = '\033[96m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
RESET = '\033[0m'

def gerar_hashes(caminho_arquivo):
    """Gera múltiplos hashes simultaneamente para o arquivo."""
    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256()
    }
    
    try:
        with open(caminho_arquivo, "rb") as f:
            for bloco in iter(lambda: f.read(8192), b""):
                for h in hashes.values():
                    h.update(bloco)
        
        return {nome: h.hexdigest() for nome, h in hashes.items()}
    except Exception as e:
        return str(e)

def main():
    print(f"{CIANO}=== INTEGRITY SCANNER PRO v3.0 ==={RESET}")
    caminho = input("\nArraste o arquivo ou cole o caminho: ").strip().replace('"', '').replace("'", "")

    if os.path.isfile(caminho):
        res = gerar_hashes(caminho)
        print(f"\n[+] Resultados para: {os.path.basename(caminho)}")
        print(f"  > MD5:    {res['md5']}")
        print(f"  > SHA-1:  {res['sha1']}")
        print(f"  > SHA-256: {VERDE}{res['sha256']}{RESET}")
        
        # Funcionalidade de Comparação Rápida
        esperado = input(f"\n{AMARELO}Comparar com hash oficial? (Cole aqui ou Enter para pular): {RESET}").strip().lower()
        if esperado:
            if esperado in res.values():
                print(f"{VERDE}[✓] INTEGRIDADE CONFIRMADA: O arquivo é idêntico ao original.{RESET}")
            else:
                print(f"\033[91m[X] ALERTA: HASH NÃO CONCORDA! Possível adulteração.{RESET}")
    
    elif os.path.isdir(caminho):
        print(f"\n[!] Analisando diretório... (Modo Forense)")
        for arquivo in os.listdir(caminho):
            arq_full = os.path.join(caminho, arquivo)
            if os.path.isfile(arq_full):
                h256 = gerar_hashes(arq_full)['sha256']
                print(f"  {arquivo:<25} | SHA-256: {h256}")
    else:
        print("\n[!] Caminho inválido.")

    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    main()
