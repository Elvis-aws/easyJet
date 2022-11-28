from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass
from utilities.yearMonth import YearMonth
import json
import os


class ScoresAndFixturesPage:

    __fixture_section_locator = "[aria-live='polite']>div>div"
    __test_data = ''

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
        self.__test_data = _dir.replace('testCases', 'testData')
        tottenham = 'Tottenham Hotspur'
        fixture_list = []
        month_count = 1
        BaseClass.element_wait(By.CSS_SELECTOR, self.__fixture_section_locator)
        while len(fixture_list) < 6:
            year_month = YearMonth.get_year_month(self, month_count)
            self.__click_on_date_picker(year_month)
            BaseClass.element_wait(By.CSS_SELECTOR, self.__fixture_section_locator)
            elements = BaseClass.find_elements(By.CSS_SELECTOR, self.__fixture_section_locator)
            length_of_elements = len(elements)
            month_count += 1
            for index in range(length_of_elements):
                text = BaseClass.get_element_text(By.CSS_SELECTOR, (self.__date_section_locator(index + 1)))
                if tottenham in text:
                    text_list = text.split("\n")
                    tottenham_index = text_list.index(tottenham)
                    last_index = len(text_list) - 1
                    if last_index != tottenham_index:
                        if '0' in text_list[tottenham_index + 1]:
                            time_index = tottenham_index + 1
                            opponent_index = time_index + 1
                            fixture_text = f'{text_list[0]}: {text_list[tottenham_index]} {text_list[time_index]} {text_list[opponent_index]}'
                            fixture_list.append(fixture_text)
            json_date_fixtures = json.dumps(fixture_list, indent=4)
            with open(f"{self.__test_data}/date_fixtures.json", "w") as outfile:
                outfile.write(json_date_fixtures)
        return fixture_list

    def get_easy_games(self):
        list_of_bottom_teams = ['Southampton', 'Wolverhampton Wanderers', 'Nottingham Forest']
        list_of_easy_games = []
        f = open(f"{self.__test_data}/date_fixtures.json")
        json_data = json.load(f)
        for teams in list_of_bottom_teams:
            for fixture in json_data:
                if teams in fixture:
                    list_of_easy_games.append(fixture)
        f.close()

        json_date_fixtures = json.dumps(list_of_easy_games, indent=4)
        with open(f"{self.__test_data}/easy_games.json", "w") as outfile:
            outfile.write(json_date_fixtures)
        return list_of_easy_games


