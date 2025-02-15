from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class MailSender:
    """
    A class to send emails using the SMTP protocol.
    At creation time it asks for the email, password and recipient's email.
    This because all this informations cannot be stored in the class, for security reasons.
    Note: only works with Libero Mail.
    """
    def __init__(self, mail: str = None, password: str = None, recipient: list = None):
        """
        Initializes the MailSender object.
        If mail, password or recipient are None, the user will be asked to input them.
        Arguments:
            mail (str|None): the email address of the sender.
            password (str|None): the password of the sender.
            recipient (list|None): the email addresses of the recipients.
        """
        if mail is None:
            self.mail = input("Enter your email: ")
        else:
            self.mail = mail
        if self.mail.split("@")[1] != "libero.it":
            raise ValueError("Only Libero Mail is supported.")
        if password is None:
            self.password = input("Enter your password: ")
        else:
            self.password = password
        if recipient is None:
            self.recipient = input("Enter the recipients' emails (comma separated): ").split(",")
        else:
            self.recipient = recipient

    def send_mail(self, subject: str, body: str) -> bool:
        """
        Sends an email to all recipients.
        Args:
            subject (str): the subject of the email.
            body (str): the body of the email.
        Returns:
            bool: True if the email was sent successfully to all recipients, False otherwise.
        """
            
        msg = MIMEMultipart()
        msg["From"] = self.mail
        msg["To"] = ""
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        success = False
        try:
            server = smtplib.SMTP("smtp.libero.it", 587)
            server.starttls()
            server.login(self.mail, self.password)
            server.sendmail(self.mail, self.recipient, msg.as_string())
            print("Email sent successfully!")
            success = True
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()
            return success
