from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from configurations.context import Context
from utilities.customLogger import LogGeneration
import os
log = LogGeneration.loggen()


class BaseClass:

    @staticmethod
    def take_screenshot(name):
        working_dir = os.getcwd()
        screenshots_dir = working_dir.replace('testCases', 'screenshots/')
        try:
            Context.driver.save_screenshot(f'{screenshots_dir}' + f'{name}.png')
            log.info('Screen shot successfully taken')
        except Exception as error:
            log.error(error)

    @staticmethod
    def find_elements(by, web_element):
        try:
            elements = Context.driver.find_elements(by, web_element)
            log.info(f'Web-elements successfully returned: {web_element}')
            return elements
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def find_element(by, web_element):
        try:
            element = Context.driver.find_element(by, web_element)
            log.info(f'Web-element successfully returned: {web_element}')
            return element
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def element_hover_over(by, web_element):
        try:
            element_to_hover = Context.driver.find_element(by, web_element)
            hover = ActionChains(Context.driver).move_to_element(element_to_hover)
            hover.perform()
            log.info(f'Web-element hover-over successful: {web_element}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def element_click(by, web_element):
        try:
            element_to_click = Context.driver.find_element(by, web_element)
            element_to_click.click()
            log.info(f'Successfully clicked on web-element: {web_element}')
        except Exception as error:
            if NoSuchElementException in error:
                element_to_hover = Context.driver.find_element(by, web_element)
                hover = ActionChains(Context.driver).move_to_element(element_to_hover)
                hover.perform()

                element_to_click = Context.driver.find_element(by, web_element)
                element_to_click.click()
                log.info(f'Successfully clicked on web-element: {web_element}')
            else:
                log.error(error)
                raise error

    @staticmethod
    def element_wait(by, web_element):
        try:
            WebDriverWait(Context.driver, 10).until(wait.presence_of_element_located((by, web_element)))
            log.info(f'Successfully waited for web-element: {web_element}')
        except TimeoutException as error:
            log.error('Timed out waiting for page to load', error.msg)
            raise error

    @staticmethod
    def clear_text(by, web_element):
        try:
            element_to_clear = Context.driver.find_element(by, web_element)
            element_to_clear.clear()
            log.info(f'Successfully cleared text on web-element: {web_element}')
        except Exception as error:
            log.error('Unable to clear text', error)
            raise error

    @staticmethod
    def set_text(by, web_element, text):
        try:
            element_to_set = Context.driver.find_element(by, web_element)
            element_to_set.send_keys(text)
            log.info(f'Successfully set text on web-element: {web_element}')
        except Exception as error:
            log.error('Unable to set text', error)
            raise error

    @staticmethod
    def element_is_visible(by, web_element):
        try:
            element = Context.driver.find_element(by, web_element)
            presence_of_value = element.is_displayed()
            log.info(f'Successfully checked web-element visibility: {web_element}')
            return presence_of_value
        except Exception as error:
            log.error('Unable to clear text', error)
            raise error

    @staticmethod
    def is_element_clickable(by, web_element):
        try:
            WebDriverWait(Context.driver, 10).until(wait.element_to_be_clickable((by, web_element)))
            log.info(f'Successfully checked web-element clickable: {web_element}')
        except Exception as error:
            log.error('Unable to click on element', error)
            raise error

    @staticmethod
    def get_element_text(by, web_element):
        try:
            element = Context.driver.find_element(by, web_element)
            text = element.text
            log.info(f'Successfully returned web-element text: {web_element}')
            return text
        except Exception as error:
            log.error('Unable to get text', error)
            raise error

    @staticmethod
    def navigate_to_link(url):
        try:
            Context.driver.get(url)
            log.info(f'Successfully navigated to URL: {url}')
        except Exception as error:
            log.error(f'Unable to navigate to url :{url}', error)
            raise error
