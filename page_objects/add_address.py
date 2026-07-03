from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

click_dropdown_xpath='//*[@id="top-links"]/ul/li[2]'
click_my_account='//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
click_address_book_xpath='//*[@id="column-right"]/div/a[4]'
click_new_address_xpath='//*[@id="content"]/div/div[2]/a'
first_name_name='firstname'
last_name_name='lastname'
company_xpath='input-company'
address1_name='address_1'
address2_name='address_2'
city_name='city'
postcode_name='postcode'
country_name='country_id'
state_name='zone_id'
default_address_yes='default'
default_address_no='default'
continue_btn_xpath='//*[@id="content"]/form/div/div[2]/input'

class AddAddress:
    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, click_dropdown_xpath).click()

    def click_my_account(self):
        self.driver.find_element(By.XPATH, click_my_account).click()

    def click_address_book(self):
        self.driver.find_element(By.XPATH, click_address_book_xpath).click()

    def click_new_address(self):
        self.driver.find_element(By.XPATH, click_new_address_xpath).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.NAME, first_name_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.NAME, last_name_name).send_keys(last_name)

    def enter_company(self, company):
        wait = WebDriverWait(self.driver, 20)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-company")
            )
        )

        element.send_keys(company)

    def enter_address1(self, address1):
        self.driver.find_element(By.NAME, address1_name).send_keys(address1)

    def enter_address2(self, address2):
        self.driver.find_element(By.NAME, address2_name).send_keys(address2)

    def enter_city(self, city):
        self.driver.find_element(By.NAME, city_name).send_keys(city)

    def enter_postcode(self, postcode):
        self.driver.find_element(By.NAME, postcode_name).send_keys(postcode)

    def select_country(self, country):
        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, country_name))
        )
        country_dropdown.send_keys(country)

    def select_state(self, state):
        state_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, state_name))
        )
        state_dropdown.send_keys(state)

    def select_default_address_yes(self):
        wait = WebDriverWait(self.driver, 20)

        yes_radio = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@name='default' and @value='1']")
            )
        )

        yes_radio.click()

    def select_default_address_no(self):
        wait = WebDriverWait(self.driver, 20)

        no_radio = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@name='default' and @value='0']")
            )
        )

        no_radio.click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, continue_btn_xpath).click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 20)

        message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'alert-success')]")
            )
        )

        return message.text


