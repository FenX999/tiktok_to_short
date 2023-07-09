import http.client 
import httplib2, os, random, sys, time, argparse, json


from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.tools import argparser

from API.utube.authenticate import get_authenticated_service


#httplib configuration.
httplib2.RETRY = 1

MAX_RETRY = 10

RETRIABLE_EXCEPTIONS = (
    httplib2.HttpLib2Error, 
    IOError, 
    http.client.NotConnected,
    http.client.IncompleteRead, 
    http.client.ImproperConnectionState,
    http.client.CannotSendRequest, 
    http.client.CannotSendHeader,
    http.client.ResponseNotReady, 
    http.client.BadStatusLine
    )

RETRIABLE__STATUS_CODE = [
    500,
    502,
    503,
    504
]




VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')



def initialize_upload(youtube,  file_path, options, source):
    tags = None
    if options.keywords:
        tags = [i for i in options.keywords]

    body=dict(
    snippet=dict(
      title=options.title,
      description=options.description,
      tags=tags,
      categoryId=options.category
    ),
    status=dict(
      privacyStatus=options.privacyStatus
    )
    )

    insert_request = youtube.videos().insert(
    part=','.join(body.keys()),
    body=body,
    media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
    )

    report = resumable_upload(insert_request, source)
    return report


def resumable_upload(insert_request, source):
    response = None
    error = None
    retry = 0 
    details = {}
    posts = {}
    data = {}
    report = []
    while response is None:
        try:
            print("Uploading File...")
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print("Video id '%s' was succesfully uploaded." % response['id'])
                    details.update(response)
                    posts.update(source)
                    data = {
                        'short': details,
                        'source': source,
                    }
                    report.append(data)
                else:
                    exit("The Upload failed with an unexpected response: '%s'" % response)
        except HttpError as e :
            if e.resp.status in RETRIABLE__STATUS_CODE:
                error = f"A retriable HTTP error occured:\n{e.resp.status, e.content}" 
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"a retriable error occured: {e}"
        
        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRY:
                exit("Number of attempt exceeded...")
            
            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print(f"Sleeping {sleep_seconds} seconds before reatempting...")
            time.sleep(sleep_seconds)
    return report 

    

def upload(file_path, params, upload_status, source):
    time.sleep(60)
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=False, help='Video file to upload')
    parser.add_argument('--title', help='Video Title', default=params['metadata'][0]['video_title'])
    parser.add_argument('--description', help='Video Description', default=params['metadata'][0]['video_description'])
    parser.add_argument('--category',  default=params['metadata'][0]['category'])
    parser.add_argument('--keywords', help='Keyword comma separated', default=params['metadata'][0]['video_tags'])
    parser.add_argument('--privacyStatus', choices=VALID_PRIVACY_STATUSES, default=upload_status, help='Video privacy status.')
    args = parser.parse_args()
    youtube = get_authenticated_service()
    try:
        report = initialize_upload(youtube, file_path, args, source)
        return report
    except HttpError as e:
        print(f"an Http error occured:\n{e.resp.status, e.content}")


