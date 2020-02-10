from __future__ import print_function
from gmail.gmail import Gmail
from gcontact.gcontact import GContact
from config import config


def main():
    # initialise gmail service with proper credintials
    gml = Gmail()
    service = gml.getService()
    gcService = GContact()
    # contact = 
    
    # get all gmail labels
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    
    # if no labels found return
    if not labels:
        return
    
    # get exact lable
    label = gml.getLables(labels, config.BIRTHDAY_LABEL);
    unreadEmail, ids = gml.getTodaysColleagueNames(service, label)
    print (unreadEmail, ids)
    print(gcService.getAllContacts())
                 
if __name__ == '__main__':
    main()
