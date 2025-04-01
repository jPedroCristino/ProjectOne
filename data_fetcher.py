import requests
import json

def obter_dados(ativo="BTC/USD"):
    """Obtém dados históricos da API Alpha Vantage."""
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            
        symbol, market = ativo.split("/") if "/" in ativo else (None, None)
        
        if not symbol or not market:
            raise ValueError("Formato inválido para ativo. Use 'MOEDA/MERCADO'")
            
        url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={config['api_key']}"
        
        resposta = requests.get(url)
        dados = resposta.json()
        
        if "Time Series (Digital Currency Daily)" not in dados:
            raise KeyError("Estrutura de dados inválida da API")
            
        return dados["Time Series (Digital Currency Daily)"]
        
    except Exception as e:
        print(f"Erro na obtenção de dados: {e}")
        return None