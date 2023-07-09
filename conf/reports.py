from pathlib import Path 

def path_configuration(tiktok = False, utube= False, target=None):
    """
    A function that host path for the script to run through use tiktok = True to instantiate the short script 
    the utube and target are for further implementation in the future.
    """
    params = {}
    params['root_path'] = str(Path().resolve())
    if utube == True:
        params['report_endpoint'] = "/Reports/utube"
    if tiktok == True:
        params['report_endpoint'] = "/Reports/tiktok"
    params['scraped_endpoint'] = "/scraped"
    if target is not None:
        params['channel_name_endpoint'] = '/'+target
        params['scraped_channel_path'] = params['scraped_path']+params['channel_name_endpoint']+params['scraped_channel_filename']
    params['scraped_channel_filename'] = "/scraped.json"
    params['scraped_all_filename'] = '/all_scraped.json'
    params['black_listed_filename'] = '/black_listed.json'
    params['uploaded_endpoint'] =  "/uploaded"
    params['uploaded_filename'] = "/upload.json"
    params['downloaded_endpoint'] = "/downloaded"
    params['downloaded_filename'] = "/downloaded.json"
    params['video_scraped'] = "/Downloaded"
    params['video_edited'] = '/Output'
    params['report_path'] = params['root_path']+params['report_endpoint']
    params['scraped_path'] = params['report_path']+params['scraped_endpoint']
    #full path 
    params['scraped_all_path'] = params['scraped_path']+params['scraped_all_filename']
    params['black_listed_path'] = params['scraped_path']+params['black_listed_filename']
    params['downloaded_path'] = params['report_path']+params['downloaded_endpoint']+params['downloaded_filename']
    params['uploaded_path'] = params['report_path']+params['uploaded_endpoint']+params['uploaded_filename']
    params['video_source'] = params['root_path']+params['video_scraped']
    params['video_to_upload'] = params['root_path']+params['video_edited']
    return params
        

