import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():

    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    driver.maximize_window()
    yield driver
    driver.quit()