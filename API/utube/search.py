import time, requests, os
from conf.scraper import hashtags

import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def utube_api_scope():
    params = {}
    params['url'] = 'https://www/googleapis.com/'
    params['youtube_api'] = "youtube"
    params['version'] = 'v3'
    params['search'] = 'search'
    params['scope_search'] = params['url']+'/'+params['youtube_api']+'/'+params['version']+'/'+params['search']
    params['key'] = 'AIzaSyADINZrzhKOSk9bWVIDeHbYwJyVyjhZWcE'
    return params

def youtube_search(options):
    params = utube_api_scope()
    youtube = build(params['youtube_api'], params['version'], developerKey= params['key'])
    search_response = youtube.search().list(
        q= options.q,
    part='id, snippet',
    maxResults=options.max_results).execute()
    
    videos = []
    channels = []
    playlists = []
    
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s (%s)' % (search_result['snippet']['title'],
                                       search_result['id']['channelId']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                        search_result['id']['playlistId']))

    print(''.join(i for i in channels))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='streetfashion')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
