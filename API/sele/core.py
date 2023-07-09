from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from conf import sele_config

def SeleniumFullScreenIncognitoInstance():
    path = sele_config.WEBDRIVER_PATH
    selenium_instante_options = webdriver.ChromeOptions()
    options = [
        #'--disable-blink-features', 
        #'--no-sandbox', 
        '--disable-extensions',
        #'--ignore-certificate-errors', 
        '--incognito',
        #'--headless',
        '--window-size=1920,1080'
       ]
    for option in options:
        selenium_instante_options.add_argument(option)

    service = Service(path)
    selenium_instance = webdriver.Chrome(service=service, options=selenium_instante_options)
    return selenium_instance

def SeleniumHeadlessIncognitoInstance():
    path = sele_config.WEBDRIVER_PATH
    selenium_instante_options = webdriver.ChromeOptions()
    options = [
        #'--disable-blink-features', 
        #'--no-sandbox', 
        '--disable-extensions',
        #'--ignore-certificate-errors', 
        '--incognito',
        '--headless',
        '--window-size=1920,1080'
       ]
    for option in options:
        selenium_instante_options.add_argument(option)

    service = Service(path)
    selenium_instance = webdriver.Chrome(service=service, options=selenium_instante_options)
    return selenium_instance

def SeleniumFullScreenInstance():
    path = sele_config.WEBDRIVER_PATH
    selenium_instante_options = webdriver.ChromeOptions()
    options = [
        #'--disable-blink-features', 
        #'--no-sandbox', 
        '--disable-extensions',
        #'--ignore-certificate-errors', 
        #'--incognito',
        #'--headless',
        '--window-size=1920,1080'
       ]
    for option in options:
        selenium_instante_options.add_argument(option)

    service = Service(path)
    selenium_instance = webdriver.Chrome(service=service, options=selenium_instante_options)
    return selenium_instance
