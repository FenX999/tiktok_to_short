import requests, time, os


"""
source https://stackoverflow.com/questions/68127678/tiktok-api-get-video-url-from-post-video-not-showing
"""

def make_requests(selenium_instance, url, debug=False):
    s = requests.Session()
    selenium_user_agent = selenium_instance.execute_script("return navigator.userAgent;")
    selenium_referer = selenium_instance.current_url
    s.headers.update({"user-agent": selenium_user_agent, 'Referer': selenium_referer})
    for cookie in selenium_instance.get_cookies():
        s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
    response = s.get(url)
    if debug == True:
        print(response.headers)
    return response

def download(path, request):
    with open(path, 'wb') as f:
        for chunk in request.iter_content(chunk_size=255): 
            if chunk:
                f.write(chunk)


def dl_or_try_again(path, request, steps):
    rsize = request.headers['Content-Length']
    for i in range(steps):
        time.sleep(3)
        download(path, request)
        fsize = os.path.getsize(path)
        if int(fsize)> int(rsize) /2:
             print(f"{path.split('/')[-1]} downloaded\n @: {time.asctime()} \nfile size: {fsize} \nrequest size : {rsize}")
             break
        else:
            os.remove(path)
            pass
    fsize = os.path.getsize(path)
    if int(fsize)< int(rsize) /2:
        print(f"An error writting the file subside after {steps} attemps")
        os.remove(path)

def download_file(selenium_instance, path, filename, url, music=False, video=False, image=False):   
    if music == True:
        extension = '.mp3'
    if video == True:
        extension = '.mp4'
    if image == True:
        extension = '.jpeg'
    name = filename + extension
    full_path = os.path.join(path, name)
    if url.split(':')[0] == 'blob':
        nurl = url[5:]
    if url.split(':')[0] == 'https':
        nurl = url
    r = make_requests(selenium_instance, nurl)
    dl_or_try_again(full_path, r, 3)

