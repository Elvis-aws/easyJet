from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class LeaguesCupPage:
    __premier_league_link_locator = "[href*='.uk/sport/football/premier-league']"

    def click_on_premier_league_link(self):
        BaseClass.element_wait(By.CSS_SELECTOR, self.__premier_league_link_locator)
        BaseClass.element_click(By.CSS_SELECTOR, self.__premier_league_link_locator)


