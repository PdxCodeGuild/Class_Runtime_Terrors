import threading
from django.core.mail import EmailMessage, get_connection


class EmailThread(threading.Thread):
    def __init__(
        self,
        subject,
        content,
        sender_email,
        receiver_email,
        reply_to_email=None,
        connection=None,
    ):
        self.subject = subject
        self.content = content
        self.sender = sender_email
        self.connection = connection
        self.recipient_list = [
            receiver_email,
        ]
        self.reply_to_email = reply_to_email
        self.reply_to_email_list = []
        if self.reply_to_email:
            self.reply_to_email_list.append(self.reply_to_email)
        threading.Thread.__init__(self)

    def run(self):
        if self.connection:
            kwargs = {"headers": {"Message-ID": "foo"}, "connection": self.connection}
        else:
            kwargs = {"headers": {"Message-ID": "foo"}}
        msg = EmailMessage(
            self.subject,
            self.content,
            self.sender,
            self.recipient_list,
            reply_to=self.reply_to_email_list,
            **kwargs,
        )
        msg.content_subtype = "html"
        msg.send()


def send_html_mail(
    subject, content, sender_email, receiver_email, reply_to_email=None, connection=None
):
    EmailThread(
        subject,
        content,
        sender_email,
        receiver_email,
        reply_to_email,
        connection=connection,
    ).start()