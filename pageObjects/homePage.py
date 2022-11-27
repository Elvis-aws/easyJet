from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class HomePage:
    __football_locator = "ul>li:nth-child(2)>[href='/sport/football']>span"

    def click_on_football_link(self):
        BaseClass.element_wait(By.CSS_SELECTOR, self.__football_locator)
        BaseClass.element_click(By.CSS_SELECTOR, self.__football_locator)


