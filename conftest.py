import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.readProperties import ReadConfig
import pytest
from configurations.context import Context
from selenium.webdriver.chrome.options import Options
from configurations.baseClass import BaseClass
from allure_commons.types import AttachmentType


@pytest.fixture(autouse=True)
def setup(request):
    options = Options()
    options.headless = bool(ReadConfig.get_headless())
    browser_type = ReadConfig.get_browser_type()
    if browser_type == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_type == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.set_window_size(1024, 600)
    driver.maximize_window()
    Context.driver = driver
    url = ReadConfig.get_application_url()
    Context.driver.get(url)
    test_name = request.node.name

    yield
    if pytest.ExitCode.OK:
        BaseClass.take_screenshot(test_name)
        allure.attach(driver.get_screenshot_as_png(), name=test_name, attachment_type=AttachmentType.PNG)

    driver.quit()
