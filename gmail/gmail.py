import os.path
import pickle
import json
from DateTime import DateTime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from message.message import Message
from config import config

class Gmail:
    def __init__(self):
        print "Initialising Gmail Service"
        
    def getService(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(config.TOKEN):
            with open(config.TOKEN, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', config.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(config.TOKEN, 'wb') as token:
                pickle.dump(creds, token)

        return build('gmail', 'v1', credentials=creds)
    
    def getLables(self, labels, name):
        for label in labels:
            if label["name"] == name:
                return label
    
    def getTodaysColleagueNames(self, service, label):
        arrayOfEmail, emails, ids, msg, i = [], {}, [], Message(), 0
        ids.append(label["id"])
        allMessages = msg.ListMessagesWithLabels(service, "me", ids)
        if not allMessages:
            return False, False
        for m in allMessages:
            mail = msg.GetMessage(service, m["id"])
            headers = mail["payload"]["headers"]
            for header in headers:
                if(header["name"] == "Date"):
                    emails["Date"] = header["value"]
                if(header["name"] == "Subject"):
                    emails["Subject"] = header["value"]
            arrayOfEmail.append(emails)
        return arrayOfEmail, allMessages;