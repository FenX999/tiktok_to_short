def short_metadata(author, count):
    '''
    function that instantiate a dictionnary with metadata needed
    for video uploading in youtube such as title, description, tags, category.
    make sure to inform all the variable below.
    take author and count as variable to get the possibility to format your metadata with those informations
    (see title and description for more info)
    video_tags > 
        populate this python list with selected tags that will be used on you youtube short
        be aware of the 500 char limit that youtube Imposes,
    video_description > 
        your video description you can tag the tiktok account by adding the {author} tag,
    video_title > 
        your video title there is a counter {count} logic within the script base on the length of the upload report,
    category > 
        the theme of your video wich is number baser more info here 
        https://entreresource.com/youtube-video-categories-full-list-explained-and-which-you-should-use/
    '''
    data_post = {}
    data_post['metadata'] = {
        'video_tags':[],
        'video_description': f"""""",                
        'video_title':f'', 
        'Playlists':"", 
        'category': "", 
    },    
    return data_post

def video_metadata(download_report, count):
    pass # for future version 

