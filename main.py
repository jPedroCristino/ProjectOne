import json
from data_fetcher import obter_dados
from analysis import calcular_media_movel
from logger import registrar_evento

def main():
    try:
        # Carrega configurações
        with open("config.json", "r") as f:
            config = json.load(f)

        ativo = config["ativo"]
        
        # Obtém os dados
        dados = obter_dados(ativo)
        
        if dados:
            df = calcular_media_movel(dados)
            
            if df is not None:
                # Exibe dados mesmo sem alerta
                preco_atual = df["close"].iloc[-1]
                media_movel = df["media_movel"].iloc[-1]
                
                print("\n=== Dados Analisados ===")
                print(f"Preço Atual: {preco_atual:.2f}")
                print(f"Média Móvel (7 dias): {media_movel:.2f}\n")
                
                # Lógica do Alerta
                if preco_atual > media_movel:
                    mensagem = f"ALERTA DISPARADO! Preço ({preco_atual:.2f}) > Média ({media_movel:.2f})"
                    registrar_evento(mensagem)
                    print("🔥 " + mensagem)
                else:
                    print(" Status: Preço abaixo da média móvel. Nenhum alerta necessário.")

    except Exception as e:
        registrar_evento(f"Erro crítico: {str(e)}")
        print(f"Falha no sistema: {e}")

if __name__ == "__main__":
    main()