import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config


class EmailClient:
    def __init__(self):
        self.server = smtplib.SMTP(
            config("EMAIL_SMTP_SERVER"), int(config("EMAIL_SMTP_PORT"))
        )
        self.email = config("EMAIL_ADDRESS")
        self.server.starttls()
        self.server.login(self.email, config("EMAIL_PASSWORD"))

    def send_email(self, email_message):
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = email_message.to
        msg["Subject"] = email_message.subject
        msg.attach(MIMEText(email_message.body, "plain"))
        self.server.send_message(msg)
        del msg  # Es importante eliminar el objeto mensaje después de enviarlo

    def __del__(self):
        # Verificar si esta conectado antes de cerrar la conexión
        if self.server:
            try:
                self.server.quit()
            except:
                pass
            self.server = None
