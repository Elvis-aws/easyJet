from pageObjects.homePage import HomePage
from pageObjects.irelandPage import IrelandPage
from pageObjects.bestLiveCasinoSitsPage import BestLiveCasinoSitsPage
from configurations.httpRequest import SiteMapRequest


class TestGambling:
    home_page = HomePage()
    ireland_page = IrelandPage()
    bestLiveCasinoSits_page = BestLiveCasinoSitsPage()

    def test_verify_h1_tag(self):
        self.home_page.expand_countries_dropdown()
        self.home_page.select_country_ireland()
        boolean_result = self.ireland_page.h1_tag_exists()
        h1_text = self.ireland_page.get_h1_text()
        print('Text to print is:', h1_text)
        assert boolean_result is True

    def test_store_links(self):
        self.home_page.expand_countries_dropdown()
        self.home_page.select_country_ireland()
        self.ireland_page.enter_text_in_search_field()
        self.bestLiveCasinoSits_page.get_href_value()
        self.bestLiveCasinoSits_page.navigate_to_href_links()
