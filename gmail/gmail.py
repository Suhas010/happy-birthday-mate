import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from config import config
class Gmail:
    def __init__(self):
        print "suhas"
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
