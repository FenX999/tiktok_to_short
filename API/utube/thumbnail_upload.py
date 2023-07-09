import os

from oauth2client.tools import argparser

from authenticate import get_authenticated_service



def instantiate_thumbnail(youtube, video_id, path_to_thumbnail):
    youtube.thumbnails().set(videoId=video_id, media_body=file).execute()
    

def upload_thumbnail(video_id, path_to_thumbnail):
    argparser.add_argument('--video_id', required=False, help="ID of the video whose thumbnails need updating.")
    argparser.add_argument('--file', required=False, help='Path to image file.')
    args = argparser.parse_args()
    if not os.path.exists(path_to_thumbnail):
        exit('No such file check the path.')
        
    youtube = get_authenticated_service()
    try:
        instantiate_thumbnail(youtube, video_id, path_to_thumbnail)
        print("The custom thumbnail was successfully set.")
    except HttpError as e:
        print(f"an http error occured:\n{e.resp.status\ne.content}")
        
        
