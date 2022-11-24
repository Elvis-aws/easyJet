from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class HomePage:
    countries_locator = "[id*='nav-flag']>div>span"
    ireland_dropdown_locator = "[href='/ie']>div:nth-child(2)"
    text_irish_online_locator = "//*[contains(text(),'Gambling.com expertly reviews and compares all Irish online " \
                                "gambling operators')] "

    def expand_countries_dropdown(self):
        BaseClass.element_hover_over(By.CSS_SELECTOR, self.countries_locator)

    def select_country_ireland(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.ireland_dropdown_locator)
        BaseClass.element_wait(By.XPATH, self.text_irish_online_locator)
