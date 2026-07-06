from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_box_name='search'
search_button_xpath='//*[@id="search"]/span/button'
success_search__msg_xpath='//*[@id="content"]/h2'

class SearchForProducts:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_query(self, query):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(
            EC.visibility_of_element_located((By.NAME, search_box_name))
        )
        search_box.clear()
        search_box.send_keys(query)

    def click_search_button(self):
        wait = WebDriverWait(self.driver, 10)
        search_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, search_button_xpath))
        )
        search_button.click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, success_search__msg_xpath))
        )
        return success_message.text


