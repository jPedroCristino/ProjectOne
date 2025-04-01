# ProjectOne
Sistema de Monitoramento de Preços de Criptomoedas

## Funcionalidades
- Coleta dados históricos da API Alpha Vantage
- Calcula média móvel de 7 dias
- Gera alertas locais quando o preço ultrapassa a média
- Registra todos os eventos em arquivo de log

## Como usar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute: `python main.py`
3. Verifique os resultados em `eventos.log`