import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from config import config

class GContact:
  def __init__(self):
    print("initializing Gmail Contact Service")

    # validate and authenticate
    FLOW = OAuth2WebServerFlow(
        client_id= config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        scope=config.PEOPLE_SCOPE)

    # store credentials locally
    storage = Storage('info.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
      credentials = tools.run_flow(FLOW, storage)

    http = httplib2.Http()
    http = credentials.authorize(http)

    people_service = build(serviceName='people', version='v1', http=http)
    # Get name and emails from people service
    feed = people_service.people().connections().list(resourceName='people/me', personFields='names,emailAddresses').execute()
    return feed
