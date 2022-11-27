from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class FootballPage:
    __leagues_and_cup_link_locator = "[href='/sport/football/leagues-cups']"

    def click_on_leagues_and_cup_link(self):
        BaseClass.element_wait(By.CSS_SELECTOR, self.__leagues_and_cup_link_locator)
        BaseClass.element_click(By.CSS_SELECTOR, self.__leagues_and_cup_link_locator)


