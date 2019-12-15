from email.mime.text import MIMEText
from config import config
import base64
class Message:
    def create_message(self, to, subject, message_text):
        """Create a message for an email.

        Args:
            from: Email address of the sender.
            to: Email address of the receiver.
            subject: The subject of the email message.
            message_text: The text of the email message.

        Returns:
            An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = config.TO
        message['from'] = config.SENDER
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string())}
    
    def send_message(self, service, user_id, message):
        """Send an email message.

        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address.
            message: Message to be sent.

        Returns:
            Sent Message.
        """
        try:
            message = (service.users().messages().send(userId=user_id, body=message).execute())
            print ('Message Id: %s' % message['id'])
            return message
        except 'error':
            print ('An error occurred:')
