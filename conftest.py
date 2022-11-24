import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
import pytest
from configurations.context import Context
from pytest import ExitCode
from configurations.baseClass import BaseClass
from allure_commons.types import AttachmentType


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
    if not pytest.ExitCode.OK:
        BaseClass.take_screenshot(test_name)
        allure.attach(driver.get_screenshot_as_png(), name=test_name, attachment_type=AttachmentType.PNG)

    driver.quit()
