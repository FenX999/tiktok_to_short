import os, sys, httplib2

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from apiclient.discovery import build


from conf import api_conf

secret  = api_conf.CREDENTIALS

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.cloud.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   secret))

def get_authenticated_service():
    flow = flow_from_clientsecrets(
        secret,
        scope= api_conf.YOUTUBE_UPLOAD_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return build(api_conf.YOUTUBE_API_SERVICE_NAME, 
                    api_conf.YOUTUBE_API_VERSION,
                    http = credentials.authorize(httplib2.Http()))
