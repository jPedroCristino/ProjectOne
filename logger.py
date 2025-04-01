from datetime import datetime

def registrar_evento(mensagem):
    """Registra eventos em arquivo de log com timestamp."""
    with open("eventos.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {mensagem}\n")