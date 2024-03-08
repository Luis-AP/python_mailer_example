from google_email.email_client import EmailClient
from google_email.email_message import EmailMessage


def main():
    client = EmailClient()
    message = EmailMessage(
        "lap18958@gmail.com",
        "Clase Git - Github",
        "Mensaje de prueba para explicar el uso de la clase EmailClient y EmailMessage.",
    )
    client.send_email(message)


if __name__ == "__main__":
    main()
