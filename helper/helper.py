from config import config
from message.message import Message

class Helper:
  
  def getExactName(self, person):
    if person.startswith(config.WORK_ANNIVERSARY_LABEL_HEADER):
      newPerson = person.replace(config.WORK_ANNIVERSARY_LABEL_HEADER, "")
      return newPerson.strip()
    elif person.startswith(config.BIRTHDAY_HEADER):
      newPerson = person.replace(config.BIRTHDAY_HEADER, "")
      return newPerson.strip()
    return person.strip()

  def getNamesFromSubject(self, subject):
    birthdayMates, workAnniversaryMates = [], []
    allPeople = subject.rsplit(", ")
    if allPeople[0].startswith(config.BIRTHDAY_HEADER):
      if len(allPeople) > 1:
        for person in allPeople:
          birthdayMates.append(self.getExactName(person))
      else:
        birthdayMates.append(self.getExactName(allPeople[0]))
    elif allPeople[0].startswith(config.WORK_ANNIVERSARY_LABEL_HEADER):
      if len(allPeople) > 1:
        for person in allPeople:
          workAnniversaryMates.append(self.getExactName(person))
      else:
        workAnniversaryMates.append(self.getExactName(allPeople[0]))

    return birthdayMates, workAnniversaryMates;

  """ Return array of person having birthday and having there work anniversary """
  def getAllNamesFromHeaders(self, arr):
    for item in arr:
      birthdayMates, workAnniversaryMates = self.getNamesFromSubject(item["Subject"])
    return birthdayMates, workAnniversaryMates;

  def sendBirthdayMails(self, service, mates):
    msg = Message()
    for mate in mates:
      message = msg.create_message(config.SENDER, config.BIRTHDAY_SUBJECT_LINE % (mate["name"].title()), config.BIRTHDAY_MESSAGE % (mate["name"].title()))
      msg.send_message(service, config.SENDER, message)
  
  
  def sendAnniversaryEmails(self, service, mates):
    msg = Message()
    for mate in mates:
      message = msg.create_message(config.SENDER, config.WORK_ANNIVERSARY_SUBJECT_LINE % (mate["name"].title()), config.WORK_ANNIVERSARY_MESSAGE % (mate["name"].title()))
      msg.send_message(service, config.SENDER, message)
  
  def plain(self, str):
    str = str.encode("utf-8")
    str = str.lower()
    str = " ".join(str.split())
    return str

  def findEmailInAllPeoples(self, persons, allPeoples ):
    mates = []
    for person in persons:
      # print(person)
      for people in allPeoples["connections"]:
        # print(person.encode("utf-8"), people["names"][0]["displayName"].encode("utf-8"), search(person.encode("utf-8"), people["names"][0]["displayName"].encode("utf-8")))
        if(self.plain(person) == self.plain(people["names"][0]["displayName"])):
          mates.append({ "email": self.plain(people["emailAddresses"][0]["value"]), "name": self.plain(person)})
    return mates
    
  def sendEmailsToAll(self, service, birthdayMates, anniversaryMates, allPeoples):
    print(len(allPeoples["connections"]))
    if len(birthdayMates):
      emails = self.findEmailInAllPeoples(birthdayMates, allPeoples)
      self.sendBirthdayMails(service, emails)
    if len(anniversaryMates):
      emails = self.findEmailInAllPeoples(anniversaryMates, allPeoples)
      self.sendAnniversaryEmails(service, emails)