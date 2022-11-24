from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class HomePage:
    __base_class = BaseClass()
    __countries_locator = By.CSS_SELECTOR("[id*='nav-flag']>div>span")
    __ireland_dropdown_locator = By.CSS_SELECTOR("[href='/ie']>div:nth-child(2)")
    __text_irish_online_locator = By.XPATH("//*[contains(text(),'Gambling.com expertly reviews and compares all Irish "
                                           "online gambling operators')]")

    def expand_countries_dropdown(self):
        self.__base_class.element_hover_over(self.__countries_locator)

    def select_country_ireland(self):
        self.__base_class.element_click(self.__ireland_dropdown_locator)
        self.__base_class.element_wait(self.__text_irish_online_locator)
