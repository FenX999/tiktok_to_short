import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from API.sele.behavior import get_bottom_page
from API.sele.navigation import expand_shadow_element

'''
series of function utilizing selenium modules to navigate through TikTok
'''


def check_for_capcha(selenium_instance):
    try:
        capcha = selenium_instance.find_element(By.ID, 'tiktok-verify-ele')
        if capcha:
            checked_capcha = input('Have you gone throught the capcha? ')
            if capcha == "y":
                pass
    except NoSuchElementException:
        pass

def page_up(driver):
    try:
        driver.find_element(By.CLASS_NAME, "tiktok-sv88au-ButtonIconContainer").click()
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "tiktok-1uc6di1-ButtonIconContainer").click()
    print("page up ...")

def wait_for_tiktok_cookie(selenium_instance):
    """
        selenium function that leverage the python input module to wait for the user to resolve the capcha on the screen
        the function resume once the user anwser the input's question'
    """
    awaiting = input('Have you gone throught the capcha? ')
    if awaiting == "y":
        banner = selenium_instance.find_element(By.TAG_NAME, "tiktok-cookie-banner")
        shadowRoot = expand_shadow_element(selenium_instance, banner)
        shadowbtn = shadowRoot.find_elements(By.CSS_SELECTOR, "button")
        for btn in shadowbtn:
            if btn.text == 'Accept all':
                WebDriverWait(selenium_instance, 20).until(EC.element_to_be_clickable(btn)).click()
    print("passing cookie...")

def tiktok_login(selenium_instance, username, password):    
    selenium_instance.find_element(By.XPATH, '//button[@data-e2e = "top-login-button"]').click()
    popup = browser.find_element(By.CLASS_NAME, 'tiktok-1dw2wty-DivCenterWrapper.e1gjoq3k7')
    login_options = popup.find_elements(By.CLASS_NAME, 'tiktok-2pt368-DivBoxContainer')
    for option in login_options:
        time.sleep(1)

        if option.text == 'Use phone / email / username':
            option.click()
            break
    time.sleep(3)
    popup.find_element(By.CLASS_NAME, 'tiktok-1mgli76-ALink-StyledLink').click()
    time.sleep(2)
    popup.find_element(By.XPATH, '//input[@placeholder = "Email or username"]').send_keys(username)
    time.sleep(2)
    popup.find_element(By.XPATH, '//input[@placeholder = "Password"]').send_keys(password)
    time.sleep(2)
    popup.find_element(By.XPATH, '//button[@data-e2e= "login-button"]').click()
    time.sleep(2)


def fetch_results(selenium_instance, class_name):
    return selenium_instance.find_elements(By.CLASS_NAME, class_name)



def scroll_for_new_results(selenium_instance, class_name, total, ntotal, debug= False):
    while len(total) < len(ntotal):
        time.sleep(1)
        total = ntotal
        if debug == True:
            print(f'total at {len(total)}')
        get_bottom_page(selenium_instance)
        time.sleep(1)
        get_bottom_page(selenium_instance)
        check_for_capcha(selenium_instance)
        ntotal = fetch_results(selenium_instance, class_name)
        if debug == True:
            print(f'new total at {len(ntotal)}')
        if len(total) == len(ntotal):
            return total





