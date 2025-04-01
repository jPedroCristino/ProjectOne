import pandas as pd

def calcular_media_movel(dados):
    """Processa dados e calcula a média móvel, exibindo informações detalhadas."""
    try:
        df = pd.DataFrame.from_dict(dados, orient="index")
        df.columns = ['1. open', '2. high', '3. low', '4. close', '5. volume']
        df = df.iloc[::-1]  # Ordena cronologicamente
        
        # Formatação para exibição
        pd.set_option('display.float_format', lambda x: f"{x:.8f}".rstrip('0').rstrip('.'))
        
        print("\n=== Estrutura do DataFrame ===")
        print("Colunas:", df.columns.tolist())
        print("\nExemplo de Dados (5 primeiras linhas):")
        print(df.head())
        
        # Cálculos
        df["close"] = df["4. close"].astype(float)
        df["media_movel"] = df["close"].rolling(window=7).mean()
        
        return df
    
    except Exception as e:
        print(f"\n Erro na análise: {e}")
        return None