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
from pytest_harvest import saved_fixture
import os
import glob
from threading import Lock
from utilities.customLogger import LogGeneration
log = LogGeneration.loggen()


@pytest.fixture(autouse=True)
@saved_fixture  # to save all instances created. access using fixture_store
def setup(request):
    try:
        options = Options()
        bool_object = ReadConfig.get_headless()
        options.headless = bool_object
        browser_type = ReadConfig.get_browser_type()
        log.info(f'Opening {browser_type} browser')
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
        test_name = request.node.name # Get current test name
        _dir = os.getcwd()
        log_dir = _dir.replace('testCases', 'screenshots/*')

        # Delete files from screenshot folder
        files = glob.glob(log_dir)
        for f in files:
            os.remove(f)

        yield

        # Lock current thread execution
        lock = Lock()
        lock.acquire()
        test_exit_status = request.node.session.testsfailed
        if test_exit_status == 1:
            BaseClass.take_screenshot(test_name)
            allure.attach(driver.get_screenshot_as_png(), name=test_name, attachment_type=AttachmentType.PNG)
        lock.release()
        driver.quit()
        log.info(f'Closing {browser_type} browser')
    except Exception as error:
        log.error(error)
        raise error
