from datetime import datetime

def registrar_evento(mensagem):
    """Registra eventos do sistema em um arquivo de log."""
    with open("eventos.log", "a") as f:
        f.write(f"{datetime.now()} - {mensagem}\n")
