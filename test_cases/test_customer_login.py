import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.customer_login import CustomerLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestLoginPage:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    username_12 = ReadConfig.get_invalid_username()
    password = ReadConfig.get_password()
    password_12 = ReadConfig.get_invalid_password()
    #
    @pytest.mark.title
    def test_page_title(self, set_up):
        self.driver = set_up
        print("url:",self.base_url)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        page_title = self.driver.title
        print("Actual title:", page_title)
        time.sleep(3)
        print("Actual title from Selenium:", page_title)
        if "Account Login" in page_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "test_page_title.png")
            self.driver.save_screenshot("screenshots/test_page_title.png")
            #self.driver.close()
            assert False

    @pytest.mark.valid_login
    def test_login(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()


        time.sleep(10)
        page_title = self.driver.title
        print("Current page title:", page_title)
        if page_title == "My Account":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(r"C:\Users\dmana\OneDrive\Desktop\Selenium\My_Project_class_June\screenshots\test_valid_login.png")
            self.driver.close()
            assert False

    @pytest.mark.invalid_username
    def test_invalid_username(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)
        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.invalid_username()
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()

        error_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="account-login"]/div[1]')
            )
        )

        error_text = error_element.text
        print("Error message displayed:", error_text)

        assert error_text == "Warning: No match for E-Mail Address and/or Password."

        result = self.driver.save_screenshot(
            r"C:\Users\dmana\OneDrive\Desktop\Selenium\My_Project_class_June\screenshots\invalid_username_failed.png"
        )
        print(result)

        self.driver.close()

    @pytest.mark.invalid_password
    def test_invalid_password(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.invalid_password(


        )
        self.login_pg_obj.click_login()

        # Correct WebDriverWait usage
        error_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="account-login"]/div[1]')
            )
        )
        error_text = error_element.text
        print("Error message displayed:", error_text)

        assert error_text == "Warning: No match for E-Mail Address and/or Password."

        result = self.driver.save_screenshot(
            r"C:\Users\dmana\OneDrive\Desktop\Selenium\My_Project_class_June\screenshots\invalid_password_failed.png"
        )
        print(result)

