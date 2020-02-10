from __future__ import print_function
from gmail.gmail import Gmail
from gcontact.gcontact import GContact
from config import config
from helper.helper import Helper

class Main:
    def __init__(self):
        self.gml = Gmail()
        self.service = self.gml.getService()
        self.gcService = GContact()
        self.results = self.service.users().labels().list(userId='me').execute()
        self.labels = self.results.get('labels', [])
        self.hlp = Helper()


    def sendEmails(self, filterLabel):
        label = self.gml.getLables(self.labels, filterLabel);
        unreadEmails, ids = self.gml.getTodaysColleagueNames(self.service, label)
        birthday, anniversary = self.hlp.getAllNamesFromHeaders(unreadEmails)
        allContacts = self.gcService.getAllContacts()
        self.hlp.sendEmailsToAll(self.service, birthday, anniversary, allContacts)

def main():
      
    m = Main()
    # Send Work Anniversary Emails
    m.sendEmails(config.WORK_ANNIVERSARY_LABEL)
    # Send Happy Birthday Emails Emails
    m.sendEmails(config.BIRTHDAY_LABEL)
    
                 
if __name__ == '__main__':
    main()
