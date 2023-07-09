#python3 modules
import time, json, os
#selenium modules
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains 

#internal module
from conf.reports import path_configuration #config file that store internal path to json file that store historical data 
from conf.scraper import scope # config file that store keyword for the program to look for.
from API.sele.core import SeleniumFullScreenInstance # function that instanciatiate a selenium browser
from API.sele.tiktok import wait_for_tiktok_cookie, fetch_results, scroll_for_new_results# function that make the processus wait for a human captcha and once validate the cookie banner 
from API.sele.behavior import get_bottom_page, scroll_to # behaviorial function that scroll down throught the webpage
from tools.write_read_report import instantiate_report_to_list, write_report
from short.tag_scraper import scrape_account_from_tag
from API.request.dl import download_file


def filter_upload(path_to_uploaded):
    dled = instantiate_report_to_list(path_to_uploaded)
    filtered_post = []
    for i in dled:
        for el in i:
            post = el['source']['post_url']
            if post not in filtered_post:
                filtered_post.append(post)
                return filtered_post
            else:
                print("Filter_upload error: found duplicate in uploaded report.")
                pass
        

def clean_account(account, black_list):
    nlist = []
    for i in account:
        if i in black_list:
            pass
        else:
            nlist.append(i)
    return nlist

def account_validator(selenium_instance, obj, black_list, black_list_path):
    url = scope(tiktok = True, target=obj['account'])
    link = url['account_url']
    selenium_instance.get(link)
    time.sleep(2)
    wait_for_tiktok_cookie(selenium_instance)
    checked_target = input('do you wich to proceed with this target? ')
    if checked_target != 'y':
        check_black_list = input('do you want to black list this account? ')
        if check_black_list != "y":
            return False
        else:
            black_list.append(obj)
            json.dump(black_list, open(black_list_path, 'w'), indent=2)
            return False
    else:
        return True

def iterate_posts(selenium_instance, css_selector, list_obj, path_to_video, path_to_uploaded):
    uploaded_post = filter_upload(path_to_uploaded)
    posts = fetch_results(selenium_instance, css_selector)
    get_bottom_page(selenium_instance)
    nposts = fetch_results(selenium_instance, css_selector)
    if len(posts) == len(nposts):
        all_posts = nposts
    if len(posts)< len(nposts):
        all_posts = scroll_for_new_results(selenium_instance, css_selector, posts, nposts)
    for post in all_posts:
        if uploaded_post:
            if post in uploaded_post:
                pass
        scroll_to(selenium_instance, post)
        post.click()
        checked_target = input('do you wish to proceed with this post? ')
        if checked_target != 'y':
            selenium_instance.back()
            pass
        else:
            try:
                video_wraper = selenium_instance.find_element(By.CLASS_NAME, 'tiktok-15ggvmu-DivVideoWrapper')
                if video_wraper:
                    current_url = selenium_instance.current_url
                    video = video_wraper.find_element(By.TAG_NAME, 'video')
                    video_name = current_url.split('/')[-1]
                    url = video.get_attribute('src')
                    download_file(selenium_instance, path_to_video, video_name, url, video=True)
                    data = {
                        'source': 'short',
                        'tag':list_obj['tags'],
                        'account': list_obj['account'],
                        'post_url': current_url,
                        'video_name': video_name,
                    }
                    return data
            except NoSuchElementException:
                print('no video found with this post please check your selenium attributes.')
                selenium_instance.back()
                pass

def iterate_dl_account(selenium_instance, params, css_selector_post):
    path_to_black_list = params['black_listed_path']
    path_to_video = params['video_source']
    path_to_dl_report = params['downloaded_path']
    path_to_uploaded = params['uploaded_path']
    history = instantiate_report_to_list(path_to_uploaded)
    black_list = instantiate_report_to_list(path_to_black_list)
    account = clean_account(instantiate_report_to_list(params['scraped_all_path']), black_list)
    print(f'length of scraped account is {len(account)}')
    if account and history and black_list:
        for i in account:
                check_account = account_validator(selenium_instance, i, black_list, path_to_black_list)
                if not check_account:
                    pass
                else:
                    data = iterate_posts(selenium_instance, css_selector_post, i, path_to_video, path_to_uploaded)
                    write_report(path_to_dl_report, data)
    if account and black_list:
        if not history:
            history = []
        for i in account:
            check_account = account_validator(selenium_instance, i, black_list, path_to_black_list)
            if not check_account:
                count += 1
                print(f'count at {count} on {len(account)} accounts') 
                pass
            else:
                data = iterate_posts(selenium_instance, css_selector_post, i, path_to_video, path_to_uploaded)
                write_report(path_to_dl_report, data)
    if account and history:
        if not black_list:
            black_list = []
        for i in account:
            check_account = account_validator(selenium_instance, i, black_list, path_to_black_list)
            if not check_account:
                pass
            else:
                data = iterate_posts(selenium_instance, css_selector_post, i, path_to_video, path_to_uploaded)
                write_report(path_to_dl_report, data)
                          
    return data

def prep_daily_post():
    paths = path_configuration(tiktok = True) 
    browser = SeleniumFullScreenInstance()
    selenium_class =  "tiktok-x6y88p-DivItemContainerV2" #class name that encapsulate posts result to check first if no results shows of
    for i in range(50):
        iterate_dl_account(browser, paths, selenium_class)
        check_prep = input('Do you wish to continue? ')
        if check_prep != 'y':
            break

   
   
