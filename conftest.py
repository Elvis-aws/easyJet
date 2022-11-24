from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configurations import constant
import pytest
from configurations.context import context


@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    context.driver = driver
    context.driver.get(constant.baseURL)

    yield
    driver.quit()
