import os
from flask_mail import Mail, Message

class EmailSender():
    """ a wrapper to send emails, from an email """
    
    def __init__(self, app=None):
        self.EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
        self.EMAIL_SENDER_PASSWORD = os.environ.get('EMAIL_SENDER_PASSWORD')
        self.EMAIL_RECEIVING = os.environ.get('EMAIL_RECEIVING')

        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = self.EMAIL_SENDER
        app.config['MAIL_PASSWORD'] = self.EMAIL_SENDER_PASSWORD
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        self.mail = Mail(app)

    def send_email(self, name=None, email=None, subject=None, user_message=None):
        """ send email from a server email to a specific email """

        msg = Message(subject=subject,
                        sender =("PORTFOLIO", self.EMAIL_SENDER),
                        recipients = [self.EMAIL_RECEIVING])
        msg.body = f'Persona:{name}\nEmail: {email}\n{user_message}'
        msg.html = f"""
                        <h1>Portfolio Message</h1>
                        <h2>My name is: {name}</h2>
                        <h2>My email is: {email}</h2>
                        <p>{user_message}</p>
                    """
        self.mail.send(msg)