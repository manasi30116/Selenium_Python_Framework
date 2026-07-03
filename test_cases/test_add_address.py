import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.customer_login import CustomerLogin
from page_objects.add_address import AddAddress


class TestAddAddress:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.add_address
    def test_add_address(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()

        time.sleep(10)
        # Add address logic here
        self.add_address_obj = AddAddress(self.driver)
        time.sleep(2)
        self.add_address_obj.click_dropdown()
        time.sleep(2)
        self.add_address_obj.click_address_book()
        time.sleep(2)
        self.add_address_obj.click_new_address()
        time.sleep(2)
        self.add_address_obj.enter_first_name("Neha")
        self.add_address_obj.enter_last_name("Singh")
        self.add_address_obj.enter_company("Example Inc.")
        self.add_address_obj.enter_address1("1234 Main St")
        self.add_address_obj.enter_city("New York")
        self.add_address_obj.select_country("United States")
        time.sleep(2)  # Wait for the state dropdown to populate
        self.add_address_obj.select_state("California")
        self.add_address_obj.enter_postcode("12345")
        self.add_address_obj.select_default_address_no()
        self.add_address_obj.click_continue_button()

        success_message = self.add_address_obj.get_success_message()

        assert "Your address has been successfully added" in success_message