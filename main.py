from __future__ import print_function
from gmail.gmail import Gmail
from message.message import Message

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    g = Gmail()
    service =  g.getService()
    m = Message()
    # m.send_message(service, "me", m.create_message("dsuhas4u@gmail.com", "Hey There", "Hello"))
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            if label["name"] == "Happy Birthday":
                ne = []
                ne.append(label["id"])
                res = m.ListMessagesWithLabels(service, "me", ne)
                for r in res:
                    mes = m.GetMessage(service, r["id"])
                    ar = mes["payload"]["headers"]
                    for head in ar:
                        if head["name"] == "Subject":
                            print(head["value"])

                            
if __name__ == '__main__':
    main()
