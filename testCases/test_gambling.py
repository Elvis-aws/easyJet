import pytest
from pageObjects.homePage import HomePage


class GamblingTest:
    home_page = HomePage()

    def test_verify_h1_tag(self):
        self.home_page.expand_countries_dropdown()
        self.home_page.select_country_ireland()
