from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

click_dropdown_xpath='//*[@id="top-links"]/ul/li[2]'
click_my_account='//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
click_address_book_xpath='//*[@id="column-right"]/div/a[4]'
edit_button_xpath='//*[@id="content"]/div[1]/table/tbody/tr[1]/td[2]/a[1]'
first_name_name='firstname'
last_name_name='lastname'

class EditAddress:
    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, click_dropdown_xpath).click()

    def click_my_account(self):
        self.driver.find_element(By.XPATH, click_my_account).click()

    def click_address_book(self):
        self.driver.find_element(By.XPATH, click_address_book_xpath).click()

    def click_edit_button(self):
        self.driver.find_element(By.XPATH, edit_button_xpath).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.NAME, first_name_name).clear()
        self.driver.find_element(By.NAME, first_name_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.NAME, last_name_name).clear()
        self.driver.find_element(By.NAME, last_name_name).send_keys(last_name)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div[2]/input').click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        success_message_element = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="account-address"]/div[1]')))
        return success_message_element.text
