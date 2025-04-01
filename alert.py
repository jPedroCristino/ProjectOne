import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Carrega configurações do JSON
with open("config.json", "r") as f:
    config = json.load(f)

EMAIL_DESTINATARIO = config["email_destinatario"]

def enviar_email(mensagem):
    """Envia um e-mail de alerta usando SMTP."""

    remetente = "seuemail@gmail.com"  # Substitua pelo seu e-mail
    senha = "SUA_SENHA_OU_SENHA_DE_APP"  # Substitua pela senha ou senha de aplicativo
    
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = EMAIL_DESTINATARIO
    msg["Subject"] = "Alerta: Monitoramento de Preço"
    msg.attach(MIMEText(mensagem, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, EMAIL_DESTINATARIO, msg.as_string())
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
