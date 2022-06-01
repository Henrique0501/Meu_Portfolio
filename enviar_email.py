import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configs_email import config_login, config_senha


def mandar_email(to, subject, msg):
    host = "smtp.gmail.com"
    port = 587
    login = config_login
    senha = config_senha

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = to
    email_msg['Subject'] = subject
    email_msg.attach(MIMEText(msg, 'plain'))

    # Enviar
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    # Fechar
    server.quit()
