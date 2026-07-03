import time
import pytest
from page_objects.Customer_Reg_Page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestRegister:

    @pytest.mark.register
    def test_register_page(self, set_up):

        driver = set_up

        register_page = RegisterPage(driver)
        register_page.enter_first_name("John")
        register_page.enter_last_name("Doe")
        register_page.enter_email("johndoe123@gmail.com")
        register_page.enter_password("Password@123")
        register_page.enter_confirm_password("Password@123")
        time.sleep(7)
        register_page.click_privacy_policy()
        register_page.click_continue()

        assert "success" in driver.page_source.lower()