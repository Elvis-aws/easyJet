from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass
from utilities.yearMonth import YearMonth
import json
import os


class ScoresAndFixturesPage:

    __fixture_section_locator = "[aria-live='polite']>div>div"

    def __date_picker_locator(self, year_month):
        """

        :param year_month:
        :return:
        """
        date_picker_locator = f"[href='/sport/football/premier-league/scores-fixtures/{year_month}']"
        return date_picker_locator

    def __date_section_locator(self, index):
        """

        :param index:
        :return:
        """
        date_section_locator = f"[aria-live='polite']>div>div:nth-child({index})"
        return date_section_locator

    def __click_on_date_picker(self, year_month):
        BaseClass.element_wait(By.CSS_SELECTOR, (self.__date_picker_locator(year_month)))
        BaseClass.element_click(By.CSS_SELECTOR, (self.__date_picker_locator(year_month)))

    def get_fixtures(self):
        _dir = os.getcwd()
        test_data = _dir.replace('testCases', 'testData')
        tottenham = 'Tottenham Hotspur'
        fixture_list = []
        month_count = 1
        BaseClass.element_wait(By.CSS_SELECTOR, self.__fixture_section_locator)
        while len(fixture_list) < 5:
            year_month = YearMonth.get_year_month(self, month_count)
            self.__click_on_date_picker(year_month)
            BaseClass.element_wait(By.CSS_SELECTOR, self.__fixture_section_locator)
            elements = BaseClass.find_elements(By.CSS_SELECTOR, self.__fixture_section_locator)
            length_of_elements = len(elements)
            month_count += 1
            for index in range(length_of_elements):
                text = BaseClass.get_element_text(By.CSS_SELECTOR, (self.__date_section_locator(index + 1)))
                text_split = text.split("\n")
                if tottenham in text:
                    fixture_list.append(text_split)
            json_date_fixtures = json.dumps(fixture_list, indent=4)
            with open(f"{test_data}/date_fixtures.json", "w") as outfile:
                outfile.write(json_date_fixtures)
        return  fixture_list


