import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_homepage(window, url):
    """ Opens browser and loads given URL """
    window.get(url)


def navigate_search_page(window, crn):
    """ Completes all task necessary to reach results page """
    fill_search_info(window, crn)
    submit_search(window)


def fill_search_info(window, crn):
    """ Fill in all necessary form data relevant to search """
    # enter specified crn to search bar
    window.find_element_by_name('sel_crn').send_keys(crn)
    # set radio button to shows all classes
    window.find_element_by_css_selector("input[type='radio'][value='N'][name='aa']").click()


def submit_search(window):
    # submit specified information
    window.find_element_by_css_selector("input[type='submit']").click()


# TODO consider making class_info class
def navigate_results_page(window):
    """ Gathers all necessary about the desired class """
    try:
        info = get_class_info_element(window)
    finally:
        window.quit()
    return info


def get_class_info_element(window):
    """ Wait for page to load elements and select the row with the desired class info """
    info = WebDriverWait(window, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'default1')))
    return element_list_to_text(info)


def element_list_to_text(elems):
    """ Change html elements to its text contents and filter out empty strings """
    return list(filter(None, map(lambda x: x.text, elems)))  # TODO consider removing list conversion


def get_browser():
    """ Setup important program information """
    return webdriver.Chrome(config.DRIVER_PATH)


def output_status(status, info):
    """ Prints class status and other important information pertaining to class """
    print(status)
    print(*info)
    print('CLASS IS NOW OPEN!') if status.upper() == 'OPEN' else print('CLASS NOT AVAILABLE')
