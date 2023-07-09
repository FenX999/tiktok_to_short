'''
basic function to utilize script for selenium
'''

def open_newtab(selenium_instance):
    selenium_instance.execute_script("window.open('');")
    selenium_instance.switch_to.window(selenium_instance.window_handles[1])

def close_newtab(selenium_instance):
    selenium_instance.close()
    selenium_instance.switch_to.window(selenium_instance.window_handles[0])

def expand_shadow_element(selenium_instance, element):
    shadowRoot = selenium_instance.execute_script('return arguments[0].shadowRoot', element)
    return shadowRoot


    

