from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import conftest
import logging
log = logging.getLogger(__name__)


class BaseClass:

    def __int__(self):
        self.driver = conftest.setup

    def take_screenshot(self):
        self.driver.save_screenshot("image.png")

    def element_hover_over(self, web_element):
        try:
            element_to_hover = self.driver.find_element(web_element)
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
        except Exception as error:
            raise error

    def element_click(self, web_element):
        try:
            element_to_click = self.driver.find_element(web_element)
            element_to_click.click()
        except Exception as error:
            if NoSuchElementException in error:
                element_to_hover = self.driver.find_element(web_element)
                hover = ActionChains(self.driver).move_to_element(element_to_hover)
                hover.perform()

                element_to_click = self.driver.find_element(web_element)
                element_to_click.click()
            else:
                log.error(error.msg)
                raise error

    def element_wait(self, web_element):
        try:
            WebDriverWait(self.driver, 10).until(wait.presence_of_element_located(web_element))
        except TimeoutException as error:
            log.error('Timed out waiting for page to load', error.msg)
            raise error

    def clear_text(self, web_element):
        try:
            element_to_clear = self.driver.find_element(web_element)
            element_to_clear.clear()
        except TimeoutException as error:
            log.error('Unable to clear text', error.msg)
            raise error

    def set_text(self, web_element, text):
        try:
            element_to_set = self.driver.find_element(web_element)
            element_to_set.send_keys(text)
        except TimeoutException as error:
            log.error('Unable to set text', error.msg)
            raise error
