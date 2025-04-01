import requests
import json

# Carrega configurações do JSON
with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config["api_key"]

def obter_dados(ativo="BTC/USD"):
    """Obtém dados históricos do ativo informado via API."""
    
    # Separando símbolo e mercado do ativo (ex.: "BTC/USD")
    parts = ativo.split("/")
    if len(parts) != 2:
        print("Formato inválido para ativo. Use 'BTC/USD'")
        return None
    symbol, market = parts

    # URL da API para criptomoedas
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={API_KEY}"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        key = "Time Series (Digital Currency Daily)"
        if key not in dados:
            print("Chave de dados não encontrada. Resposta da API:", dados)
            return None

        return dados[key]
    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return None
