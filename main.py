from google_email.email_receiver import EmailReceiver
from google_email.email_message import EmailMessage


def main():
    client = EmailReceiver()
    limit = int(input("Ingrese el número de correos a recibir: "))
    emails = client.fetch_emails(limit)
    for email in emails:
        print(f"De: {email['from']}")
        print(f"Asunto: {email['subject']}")
        print(f"Mensaje: {email['body']}\n\n")


if __name__ == "__main__":
    main()
