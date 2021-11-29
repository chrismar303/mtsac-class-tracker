from utility import get_browser, open_homepage, navigate_search_page, navigate_results_page, output_status

# selected class
CRN_LIST = ['25885', '22213', '22214']  # HOLD | WAITLISTED OPEN | OPEN
browser = get_browser()

# BEGIN FIRST PAGE
open_homepage(browser, url='https://prodssb.mtsac.edu/prod/pw_sigsched.p_Search')
navigate_search_page(browser, crn=CRN_LIST[0])
# STARTED SECOND PAGE
class_status, *class_info = navigate_results_page(browser)
# DISPLAY CLASS STATUS INFORMATION
output_status(class_status, class_info)
