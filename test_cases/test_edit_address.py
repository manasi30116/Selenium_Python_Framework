import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.customer_login import CustomerLogin
from page_objects.add_address import AddAddress
from page_objects.edit_address import EditAddress

class TestEditAddress:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.edit_address
    def test_edit_address(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()

        time.sleep(10)
        # Edit address logic here
        self.edit_address_obj = EditAddress(self.driver)
        time.sleep(2)
        self.edit_address_obj.click_dropdown()
        time.sleep(2)
        self.edit_address_obj.click_address_book()
        time.sleep(2)
        self.edit_address_obj.click_edit_button()
        time.sleep(2)
        self.edit_address_obj.enter_first_name("Jane")
        self.edit_address_obj.enter_last_name("Smith")

        success_message = self.edit_address_obj.get_success_message()