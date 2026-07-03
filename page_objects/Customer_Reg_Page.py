
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

first_name_locator= "firstname"
last_name_locator='lastname'
email_locator='vinput-email'
your_password_locator='vinput-password'
confirm_password_locator='input-confirm'
confirm_password='confirm_password'
privacy_policy_locator='agree'
continue_btn_locator="//input[@value='Continue']"




class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, firstname):

        wait = WebDriverWait(self.driver, 80)

        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, first_name_locator)
            )
        )

        first_name.clear()
        first_name.send_keys(firstname)

    def enter_last_name(self, lastname):
        """Enter last name in the last name field"""
        self.driver.find_element(By.NAME, last_name_locator).clear()
        self.driver.find_element(By.NAME, last_name_locator).send_keys(lastname)

    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "email")
            )
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, your_password):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "password")
            )
        )
        element.clear()
        element.send_keys(your_password)

    def enter_confirm_password(self, confirm_password):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, confirm_password_locator)
            )
        )
        element.clear()
        element.send_keys(confirm_password)

    def click_privacy_policy(self):
        """Click on the privacy policy checkbox"""
        self.driver.find_element(By.NAME, privacy_policy_locator).click()

    def click_continue(self):
        print("Current URL:", self.driver.current_url)
        print("Page title:", self.driver.title)

        buttons = self.driver.find_elements(By.XPATH, "//input[@value='Continue']")
        print("Continue button count:", len(buttons))

        wait = WebDriverWait(self.driver, 20)

        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Continue']")
            )
        )

        button.click()
