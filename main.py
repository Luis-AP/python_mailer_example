from google_email.email_receiver import EmailReceiver
from google_email.email_message import EmailMessage
from google_email.email_client import EmailClient


def send_email():
    recipient = input("Ingrese el correo electrónico del destinatario: ")
    subject = input("Ingrese el asunto del correo: ")
    body = input("Ingrese el cuerpo del mensaje: ")

    message = EmailMessage(recipient, subject, body)
    client = EmailClient()
    client.send_email(message)
    print("Correo enviado exitosamente.")


def receive_emails(limit):
    receiver = EmailReceiver()
    try:
        emails = receiver.fetch_emails(limit)
        for email in emails:
            print(f"De: {email['from']}")
            print(f"Asunto: {email['subject']}")
            print(f"Mensaje: {email['body']}\n\n")
    except Exception as e:
        print(f"Error al recibir correos: {e}")


def main():
    while True:
        print("Menú de Opciones:")
        print("1. Enviar un correo electrónico")
        print("2. Recibir correos electrónicos")
        print("3. Salir")

        choice = input("Seleccione una opción (1/2/3): ")

        if choice == "1":
            send_email()
        elif choice == "2":
            limit = int(input("Ingrese el número de correos a recibir: "))
            receive_emails(limit=limit)
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
