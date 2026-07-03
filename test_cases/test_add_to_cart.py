import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.customer_login import CustomerLogin
from selenium.webdriver.common.by import By
from page_objects.add_to_cart import AddToCart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestAddToCart:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()



    @pytest.mark.add_to_cart
    def test_add_to_cart(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        self.login_pg_obj = CustomerLogin(self.driver)
        self.login_pg_obj.enter_email(self.username)
        self.login_pg_obj.enter_password(self.password)
        self.login_pg_obj.click_login()

        time.sleep(10)
        # Add to cart logic here
        self.add_to_cart_obj = AddToCart(self.driver)
        time.sleep(2)
        self.add_to_cart_obj.click_desktop_dropdown()
        time.sleep(2)
        self.add_to_cart_obj.click_mac_select()
        time.sleep(2)
        self.add_to_cart_obj.click_imac_link_open()
        time.sleep(2)
        self.add_to_cart_obj.click_add_to_cart()
        time.sleep(2)
        success_message = self.add_to_cart_obj.get_success_message()
        assert "Success: You have added" in success_message, "Add to cart failed"
        self.driver.save_screenshot(r"C:\Users\dmana\OneDrive\Desktop\Selenium\My_Project_class_June\screenshots\add_to_cart_success.png")
        self.add_to_cart_obj.click_go_to_cart()

        self.view_cart_obj = AddToCart(self.driver)
        self.add_to_cart_obj.click_add_to_cart()
        time.sleep(2)
        self.add_to_cart_obj.click_view_cart()
        print(self.driver.current_url)
        print(self.driver.title)
        cart_text = self.add_to_cart_obj.get_view_cart_text()
        assert "Shopping Cart" in cart_text, "View cart failed"

