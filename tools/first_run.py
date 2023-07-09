def check_youtube_api_credentials():
    from conf import api_conf
    data = api_conf.CREDENTIALS
    if data.exists():
        return True
    else:
        print('This script could not find the youtube API credentials make sure to DL and move it inside the conf directory')
        checked_input = input('Have you finished with your credentials? ("y") ')
        if checked_input == "y":
            pass


def check_short_metadata():
    from conf import channel
    data = channel.short_metadata('test', 0)
    dct = {
        "tag": len(data['metadata'][0]['video_tags']),
        'description':  len(data['metadata'][0]['video_description']),
        'title': len(data['metadata'][0]['video_title']),
        'category': len(data['metadata'][0]['category']),
        }
    for k , v in dct.items():
        if v == 0:
            print(f"the Key {k} is not informed")
            print("please open the channel.py inside the conf directory with your text editor")
        else:
            return True

def check_search_queries():
    from conf import scraper
    data = scraper.search_queries()
    if len(data['tags']) == 0:
        print("please open the scraper.py in the conf directory inside your text editor")
        checked_input = input('Have you finished with your credentials? ("y") ')
        if checked_input == "y":
            pass
    else:
        return True

def check_webdriver_path():
    from conf import sele_config
    data = sele_config.WEBDRIVER_PATH
    if len(data) == 0:
        print('please inform the path to your google webdriver in the sele_config.py inside the conf directory')
        checked_input = input('Have you finished with your credentials? ("y") ')
        if checked_input == "y":
            pass
    else:
        return True

def check_all_conf():
    checking = True
    while checking:
        print("checking credentials.json in conf module...")
        api = check_youtube_api_credentials()
        print("checking short metadata in channel module...")
        metadata = check_short_metadata()
        print("checking tag query in scraper module...")
        tags = check_search_queries()
        print("checking google webdriver path inside sele_config module...")
        webdriver = check_webdriver_path()
        if api and metadata and tags and webdriver == True:
            checking = False
        else:
            pass
