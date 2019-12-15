from __future__ import print_function
from gmail.gmail import Gmail
from message.message import Message

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    g = Gmail()
    m = Message()
    service =  g.getService()
    
    m.send_message(service, "me", m.create_message("dsuhas4u@gmail.com", "Hey There", "Hello"))
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    main()
