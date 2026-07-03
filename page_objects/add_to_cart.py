from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desktop_dropdown_xpath='//*[@id="menu"]/div[2]/ul/li[1]/a'
mac_select_xpath='//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'
imac_link_open_xpath='//*[@id="content"]/div[2]/div/div/div[2]/div[1]/h4/a'
add_to_cart_id='button-cart'
success_msg_xpath='//*[@id="product-product"]/div[1]'
go_to_cart_xpath='//*[@id="cart-total"]'
view_cart_xpath='//*[@id="cart"]/ul/li[2]/div/p/a[1]/strong'


class AddToCart:

    def __init__(self, driver):
        self.driver=driver

    def click_desktop_dropdown(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, desktop_dropdown_xpath)
            )
        )
        element.click()

    def click_mac_select(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, mac_select_xpath)
            )
        )
        element.click()

    def click_imac_link_open(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, imac_link_open_xpath)
            )
        )
        element.click()

    def click_add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.ID, add_to_cart_id)
            )
        )
        element.click()

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, success_msg_xpath)
            )
        )
        return element.text

    def click_go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, go_to_cart_xpath)
            )
        )
        element.click()

    def click_view_cart(self):
        print(self.driver.current_url)
        wait = WebDriverWait(self.driver, 20)

        element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href,'checkout/cart')]")
            )
        )

        element.click()

    def get_view_cart_text(self):
        wait = WebDriverWait(self.driver, 20)

        element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Shopping Cart')]")
            )
        )

        return element.text