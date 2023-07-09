def scope(tiktok = False, utube=False, target=None):
    params = {}
    if utube == True:
        params['base_url'] = 'https://youtube.com/'
        params['about'] = '/about' 
        params['playlist'] = '/playlist'
        params['videos'] = '/videos'
        params['search_query'] = 'results?search_query='
        if target:
            params['channel_url']= params['base_url']+target
            params['channel_about'] = params['channel_url']+params['about']
            params['channel_playlist'] = params['channel_url']+params['playlist']
            params['channel_videos'] = params['channel_url']+params['videos']
    if tiktok == True:
        params['base_url'] = "https://www.tiktok.com/"
        params['tag_endpoint'] = "tag/"
        params['search'] = 'search?q='
        if target is not None:
            params['account_url'] = params['base_url']+"@"+target
            params['tag_url'] = params['base_url'] + params['tag_endpoint']+target
    return params

def search_queries():
    """
    this function host a list of string for the script to run a tiktok search for.
    """
    data = {}
    data['tags'] =[]
    return data

def utube_targets():
    pass #future version
