import os
SENDER = "suhas.more@joshsoftware.com"
TO = "suhas.more@joshsoftware.com"
SCOPES = ['https://www.googleapis.com/auth/gmail.compose', 'https://www.googleapis.com/auth/gmail.labels', "https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.modify", "https://mail.google.com/"]
TOKEN = "token.pickle"

BIRTHDAY_LABEL = "Happy Birthday"
WORK_ANNIVERSARY_LABEL = "Work Anivarsary"
CLIENT_ID = os.environ["CLIENT_ID_HBM"]
CLIENT_SECRET = os.environ["CLIENT_SECRET_HBM"]
PEOPLE_SCOPE = "https://www.googleapis.com/auth/contacts.readonly"

WORK_ANNIVERSARY_LABEL_HEADER = "Congratulations"
BIRTHDAY_HEADER = "Happy Birthday"

WORK_ANNIVERSARY_SUBJECT_LINE = "Happy Work Anniversary %s <EOM/>"
WORK_ANNIVERSARY_MESSAGE = ''''''

BIRTHDAY_SUBJECT_LINE = "Happy Birthday %s <EOM/>"
BIRTHDAY_MESSAGE = ''''''
