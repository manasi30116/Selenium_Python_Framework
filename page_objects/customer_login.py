
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

enter_email_id='input-email'
password_id='input-password'
confirm_xpath='//*[@id="content"]/div/div[2]/div/form/input'

class CustomerLogin:

    def __init__(self, driver):
        self.driver=driver

    def enter_email(self,email):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, enter_email_id)
            )
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self,password):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, password_id)
            )
        )
        element.clear()
        element.send_keys(password)


    def invalid_username(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, enter_email_id)
            )
        )
        element.clear()
        element.send_keys('invalid@gmail.com')

    def invalid_password(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, password_id)
            )
        )
        element.clear()
        element.send_keys('invalid123')



    def click_login(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, confirm_xpath)
            )
        )
        element.click()
