from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class PremierLeaguePage:
    __view_all_premier_league_fixtures_link_locator = "(//span[text()='Premier League fixtures'])[2]"

    def click_on_view_all_premier_league_fixtures_link(self):
        BaseClass.element_wait(By.XPATH, self.__view_all_premier_league_fixtures_link_locator)
        BaseClass.element_click(By.XPATH, self.__view_all_premier_league_fixtures_link_locator)


