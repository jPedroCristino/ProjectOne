import json
from data_fetcher import obter_dados
from analysis import calcular_media_movel
from alert import enviar_email
from logger import registrar_evento

# Carrega configurações
with open("config.json", "r") as f:
    config = json.load(f)

ativo = config["ativo"]

# Obtém os dados da API
dados = obter_dados(ativo)

if dados:
    df = calcular_media_movel(dados)

    if df is not None:
        preco_atual = df["close"].iloc[-1]
        media_movel = df["media_movel"].iloc[-1]

        if preco_atual > media_movel:
            mensagem = f"Alerta! O preço atual ({preco_atual}) ultrapassou a média móvel ({media_movel})."
            if config["alerta_email"]:
                enviar_email(mensagem)
            registrar_evento(mensagem)
        else:
            print("Nenhum alerta disparado.")
