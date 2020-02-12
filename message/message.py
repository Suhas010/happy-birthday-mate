from email.mime.text import MIMEText
from config import config
import base64
from apiclient import errors

class Message:
    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string())}
    
    def send_message(self, service, message):
        try:
            message = (service.users().messages().send(userId="me", body=message).execute())
            print ('Message Id: %s' % message['id'])
            return message
        except 'error':
            print ('An error occurred:')
    
    def ModifyMessage(self, service, user_id, msg_id):
        try:
            message = service.users().messages().modify(userId=user_id, id=msg_id,
                                                        body={"removeLabelIds": ["UNREAD"]}).execute()

            label_ids = message['labelIds']

            return message
        except errors.HttpError, error:
            print('An error occurred: %s' % error)

    def ListMessagesWithLabels(self, service, user_id="me", label_ids=[]):
        """List all Messages of the user's mailbox with label_ids applied."""
        try:
            response = service.users().messages().list(userId=user_id, labelIds=label_ids, q="is:unread").execute()
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

    def RemoveFromLabel(self, service, msg_id, msg_labels):
        try:
            message = service.users().messages().modify(userId="me", id=msg_id,
                                                        body=msg_labels).execute()

            label_ids = message['labelIds']

            print 'Message ID: %s - With Label IDs %s' % (msg_id, label_ids)
            return message
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
