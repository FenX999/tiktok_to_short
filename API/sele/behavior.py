import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def scroll_to(selenium_instance, el):
    """
    Scroll an element into view, using JS
    """
    try:
        selenium_instance.execute_script("arguments[0].scrollIntoView();", el)
    except SELENIUM_EXCEPTIONS:
        return


def scroll_bottom(selenium_instante):
    last_height =  selenium_instante.execute_script("return document.body.scrollHeight")
    while True:
        try:
            #selenium_instante.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            ActionChains(selenium_instante).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(4)
        except TimeoutException:
            ActionChains(selenium_instante).send_keys(Keys.PAGE_UP).perform()
            time.sleep(2)
            ActionChains(selenium_instante).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        try:
            new_height = selenium_instante.execute_script("return document.body.scrollHeight")
        except TimeoutException:
            ActionChains(selenium_instante).send_keys(Keys.PAGE_UP).perform()
            time.sleep(2)
            ActionChains(selenium_instante).send_keys(Keys.PAGE_DOWN).perform()
            new_height = selenium_instante.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_bottom_page(selenium_instante):
    scrolldown = selenium_instante.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;"
        )
    match=False
    while match==False:
        last_count = scrolldown
        time.sleep(3)
        scrolldown
        if last_count== scrolldown:
            match=True
    return match


def open_newtab(selenium_instante):
    selenium_instante.execute_script("window.open('');")
    selenium_instante.switch_to.window(selenium_instante.window_handles[1])

def close_newtab(selenium_instante):
    selenium_instante.close()
    selenium_instante.switch_to.window(selenium_instante.window_handles[0])
