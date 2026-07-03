from page_objects.delete_address import DeleteAddress
import time
from page_objects.customer_login import CustomerLogin
from utility.read_properties import ReadConfig


class TestDeleteAddress:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_delete_address(self, set_up):
        self.driver = set_up
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
        time.sleep(3)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()

        time.sleep(3)

        self.delete_address_obj = DeleteAddress(self.driver)
        # self.delete_address_obj.click_dropdown()
        # time.sleep(2)
        self.delete_address_obj.click_address_book()
        time.sleep(2)
        self.delete_address_obj.click_delete_button()

        time.sleep(2)

        success_message = self.delete_address_obj.get_success_message()

        assert "successfully deleted" in success_message