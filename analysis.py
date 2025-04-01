import pandas as pd

def calcular_media_movel(dados):
    """Converte os dados em um DataFrame e calcula a média móvel de 7 dias."""

    try:
        df = pd.DataFrame.from_dict(dados, orient="index")
        df = df.iloc[::-1]  # Ordena da mais antiga para a mais recente

        # Imprime as colunas disponíveis para depuração
        print("Colunas do DataFrame:", df.columns.tolist())
        print("Exemplo de dados:", df.head())

        # Define a coluna correta do preço de fechamento
        df["close"] = df["4. close"].astype(float)

        # Calcula a média móvel
        df["media_movel"] = df["close"].rolling(window=7).mean()
        return df
    except Exception as e:
        print(f"Erro na análise de dados: {e}")
        return None
