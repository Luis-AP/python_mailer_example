import imaplib
import email
from email.header import decode_header
from decouple import config


class EmailReceiver:
    def __init__(self):
        self.server = imaplib.IMAP4_SSL(config("EMAIL_IMAP_SERVER"))
        self.email = config("EMAIL_ADDRESS")
        self.server.login(self.email, config("EMAIL_PASSWORD"))
        self.server.select("inbox")  # Selecciona la bandeja de entrada

    def fetch_emails(self, limit=10):
        status, messages = self.server.search(None, "ALL")
        messages = messages[0].split()[-limit:]  # Obtiene los últimos 'limit' correos

        emails = []
        for mail in messages:
            _, msg = self.server.fetch(mail, "(RFC822)")
            for response_part in msg:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding)
                    from_ = msg["From"]
                    body = self.get_body(msg)
                    emails.append({"from": from_, "subject": subject, "body": body})
        return emails

    def get_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if (
                    content_type == "text/plain"
                    and "attachment" not in content_disposition
                ):
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

    def __del__(self):
        if self.server:
            try:
                self.server.logout()
            except:
                pass
            self.server = None
