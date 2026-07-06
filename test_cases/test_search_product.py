import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.customer_login import CustomerLogin
from page_objects.add_address import AddAddress
from page_objects.search_for_products import SearchForProducts

class TestSearchProduct:
    base_url = ReadConfig.get_base_url()
    email = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.search_product
    def test_search_product(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Login to the application
        login_page = CustomerLogin(self.driver)
        login_page.enter_email(self.email)
        login_page.enter_password(self.password)
        login_page.click_login()

        # Search for a product
        self.search_page = SearchForProducts(self.driver)
        self.search_page.enter_search_query("iphone")
        self.search_page.click_search_button()

        # Verify success message
        success_message = self.search_page.get_success_message()
        assert 'Products meeting the search criteria' == success_message

