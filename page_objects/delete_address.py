from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.read_properties import ReadConfig

delete_button_xpath='//*[@id="content"]/div[1]/table/tbody/tr[1]/td[2]/a[2]'
click_dropdown_xpath='//*[@id="top-links"]/ul/li[2]'
click_my_account='//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
click_address_book_xpath='//*[@id="column-right"]/div/a[4]'


class DeleteAddress:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()


    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, click_dropdown_xpath).click()

    def click_my_account(self):
        self.driver.find_element(By.XPATH, click_my_account).click()

    def click_address_book(self):
        self.driver.find_element(By.XPATH, click_address_book_xpath).click()

    def click_delete_button(self):
        wait = WebDriverWait(self.driver, 10)
        delete_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[2]/td[2]/a[2]'))
        )
        delete_button.click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 20)

        message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'alert-success')]")
            )
        )

        return message.text

