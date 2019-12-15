from email.mime.text import MIMEText
from config import config
import base64
from apiclient import errors

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

    def ListMessagesWithLabels(self, service, user_id="me", label_ids=[]):
        """List all Messages of the user's mailbox with label_ids applied."""
        try:
            response = service.users().messages().list(userId=user_id,
                                                    labelIds=label_ids).execute()
            print(response)
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])

                while 'nextPageToken' in response:
                    page_token = response['nextPageToken']
                    response = service.users().messages().list(userId=user_id,
                                                            labelIds=label_ids,
                                                            pageToken=page_token).execute()
                messages.extend(response['messages'])

                return messages
        except errors.HttpError, error:
            print ('An error occurred: %s' % error)

    def GetMessage(self, service, msg_id):
        """ Get """
        try:
            message = service.users().messages().get(userId="me", id=msg_id).execute()
            return message
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
