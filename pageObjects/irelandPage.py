from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class IrelandPage:
    __h1_locator = "[class*='gambling']>h1"
    __search_locator = "[placeholder='Search Gambling.com']"
    __dropdown_locator = "ul[class*='search']>li>a"

    def h1_tag_exists(self):
        boolean_result = BaseClass.element_is_visible(By.CSS_SELECTOR, self.__h1_locator)
        return boolean_result

    def get_h1_text(self):
        h1_text = BaseClass.get_element_text(By.CSS_SELECTOR, self.__h1_locator)
        return h1_text

    def enter_text_in_search_field(self):
        BaseClass.set_text(By.CSS_SELECTOR, self.__search_locator, 'Best Live Casinos Sites”')
        BaseClass.is_element_clickable(By.CSS_SELECTOR, self.__dropdown_locator)
        BaseClass.element_click(By.CSS_SELECTOR, self.__dropdown_locator)
