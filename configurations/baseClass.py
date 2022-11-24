from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from configurations.context import context
import logging
log = logging.getLogger(__name__)


class BaseClass:

    @staticmethod
    def take_screenshot():
        context.driver.save_screenshot("image.png")

    @staticmethod
    def find_elements(by, web_element):
        try:
            elements = context.driver.find_elements(by, web_element)
            return elements
        except Exception as error:
            raise error

    @staticmethod
    def find_element(by, web_element):
        try:
            element = context.driver.find_element(by, web_element)
            return element
        except Exception as error:
            raise error

    @staticmethod
    def element_hover_over(by, web_element):
        try:
            element_to_hover = context.driver.find_element(by, web_element)
            hover = ActionChains(context.driver).move_to_element(element_to_hover)
            hover.perform()
        except Exception as error:
            raise error

    @staticmethod
    def element_click(by, web_element):
        try:
            element_to_click = context.driver.find_element(by, web_element)
            element_to_click.click()
        except Exception as error:
            if NoSuchElementException in error:
                element_to_hover = context.driver.find_element(by, web_element)
                hover = ActionChains(context.driver).move_to_element(element_to_hover)
                hover.perform()

                element_to_click = context.driver.find_element(by, web_element)
                element_to_click.click()
            else:
                log.error(error.msg)
                raise error

    @staticmethod
    def element_wait(by, web_element):
        try:
            WebDriverWait(context.driver, 10).until(wait.presence_of_element_located((by, web_element)))
        except TimeoutException as error:
            log.error('Timed out waiting for page to load', error.msg)
            raise error

    @staticmethod
    def clear_text(by, web_element):
        try:
            element_to_clear = context.driver.find_element(by, web_element)
            element_to_clear.clear()
        except TimeoutException as error:
            log.error('Unable to clear text', error.msg)
            raise error

    @staticmethod
    def set_text(by, web_element, text):
        try:
            element_to_set = context.driver.find_element(by, web_element)
            element_to_set.send_keys(text)
        except TimeoutException as error:
            log.error('Unable to set text', error.msg)
            raise error

    @staticmethod
    def element_is_visible(by, web_element):
        try:
            element = context.driver.find_element(by, web_element)
            presence_of_value = element.is_displayed()
            return presence_of_value

        except TimeoutException as error:
            log.error('Unable to clear text', error.msg)
            raise error

    @staticmethod
    def is_element_clickable(by, web_element):
        try:
            WebDriverWait(context.driver, 10).until(wait.element_to_be_clickable((by, web_element)))
        except TimeoutException as error:
            log.error('Unable to click on element', error.msg)
            raise error

    @staticmethod
    def get_element_text(by, web_element):
        try:
            element = context.driver.find_element(by, web_element)
            text = element.text
            return text
        except TimeoutException as error:
            log.error('Unable to get text', error.msg)
            raise error

    @staticmethod
    def navigate_to_link(url):
        try:
            context.driver.get(url)
        except TimeoutException as error:
            log.error(f'Unable to navigate to url :{url}', error.msg)
            raise error
