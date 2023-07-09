import os, json, time, random

from conf.reports import path_configuration
from conf.channel import short_metadata, video_metadata
from tools.write_read_report import instantiate_report_to_list, write_report
from short.tiktok_downloader import prep_daily_post
from API.utube.video_upload import upload



def fetch_file_or_none(path_to_video):
    list_file = os.listdir(path_to_video)
    if len(list_file) == 0:
        return None
    else:
        return list_file

def fetch_short_to_upload(list_file, downloaded_report):
    """
    """
    obj = random.choice(list_file)
    for el in downloaded_report:
        if el['video_name']+'.mp4' == obj:
            return el

def run_short():
    print('runnng short script')
    paths = path_configuration(tiktok = True)
    history = instantiate_report_to_list(paths['uploaded_path'])
    dled = instantiate_report_to_list(paths['downloaded_path'])
    path_to_video = paths['video_source']
    #instantiate error message
    attr_er = 'Attributes Error last video source was not for the attr choosen.'
    name_er = "File Name Error the file name in the report doesn't correspond of the actual file" 
    #function logic
    if not dled:
        dled = crawl_account()

    if history is None:
        count = 1
    else:
        count = len(history)

    check_file = fetch_file_or_none(paths['video_source'])
    if not check_file:
        os.remove(paths['downloaded_path'])
        print("No file to upload running scraper script...")
        prep_daily_post()
    else:
        obj = fetch_short_to_upload(check_file, dled) 
        params = short_metadata(obj['account'], count)
        fullpath = os.path.join(path_to_video, obj['video_name']+'.mp4')
        try:
            response = upload(fullpath, params, 'public', obj)
            if 'id' in response[0]['short']:
                write_report(paths['uploaded_path'], response)
                os.remove(fullpath)
            else:
                print(response)
        except Exception as e:
            print(e)
