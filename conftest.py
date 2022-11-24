from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
import pytest
from configurations.context import Context
from pytest import ExitCode
from configurations.baseClass import BaseClass


@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    Context.driver = driver
    url = ReadConfig.get_application_url()
    Context.driver.get(url)
    test_name = request.node.name

    yield
    if pytest.ExitCode.OK:
        BaseClass.take_screenshot(test_name)

    driver.quit()
