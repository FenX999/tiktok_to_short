import time, os, json

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#internal module
from conf.reports import path_configuration #config file that store internal path to json file that store historical data 
from conf.scraper import search_queries, scope # config file that store keyword for the program to look for.
from API.sele.core import SeleniumFullScreenInstance # function that instanciatiate a selenium browser we keep full screen to deal with the load of capcha 
from API.sele.tiktok import wait_for_tiktok_cookie, fetch_results, scroll_for_new_results 
from API.sele.behavior import get_bottom_page


def write_update_account(path, entry):
    if os.path.exists(path) and os.path.isfile(path):
        laccount = []
        f = open(path, 'r')
        data = json.load(f)
        f.close()
        for i in data:
            if i['account'] not in laccount:
                laccount.append(i['account'])
        if len(entry) > 1:
            for i in entry:
                if i['account'] not in laccount:
                    data.append(i)
                else:
                    pass
        if len(entry) == 1:
            if entry['account'] not in laccount:
                data.append(entry)
            else:
                print('data already saved passing...')
        json.dump(data, open(path, 'w'), indent=2)
    else:
        print(f'no file found at {path} creating before writing...')
        json.dump(data, open(path, 'w'), indent=2)

def scrape_account_from_tag():
    tags = search_queries()
    report = []
    checked_account = []
    browser = SeleniumFullScreenInstance()
    for tag in tags['tags']:
        url = scope(tiktok=True, target=tag)
        link = url['tag_url']
        browser.get(link)
        time.sleep(3)
        wait_for_tiktok_cookie(browser)
        check_tag = input('Do you wish to go with that tag? (y or n)')
        if check_tag != 'y':
            pass
        else:
            total = fetch_results(browser, "tiktok-x6y88p-DivItemContainerV2")
            get_bottom_page(browser)
            time.sleep(6)
            ntotal = fetch_results(browser, "tiktok-x6y88p-DivItemContainerV2")
            if len(total) < len(ntotal):
                results = scroll_for_new_results(browser, "tiktok-x6y88p-DivItemContainerV2", total, ntotal )
                print(len(results))
                count = 0
                for div in results:
                    count += 1
                    #print(count)
                    try:
                        author = div.find_element(By.CLASS_NAME, 'user-name').text
                        #print(f'found by class ')
                    except NoSuchElementException:
                        try:
                            author = div.find_element(By.TAG_NAME, 'h4').text
                            #print(f'found by tag ')
                        except NoSuchElementException:
                            pass
                    data = {
                    'tags': tag,
                    'account': author,
                    }
                    report.append(data)
                for i in report:
                    if i not in checked_account:
                        checked_account.append(i)
                path = generate_report_path(tiktok=True, scraped_all = True)
                write_update_account(path, checked_account)
    print('end of iteration')


if __name__ == '__main__':
    scrape_account_from_tag()
                
