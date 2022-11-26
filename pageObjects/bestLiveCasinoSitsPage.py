import json
import os
from selenium.webdriver.common.by import By
from configurations.baseClass import BaseClass


class BestLiveCasinoSitsPage:
    __play_now_locator = "a[class*='play-now-cta operator-item']"
    __href_value = dict()
    __count = 0
    __testData = ''

    def get_href_value(self):
        _dir = os.getcwd()
        self.__testData = _dir.replace('testCases', 'testData')
        list_of_element = BaseClass.find_elements(By.CSS_SELECTOR, self.__play_now_locator)
        for element in list_of_element:
            attribute_value = element.get_attribute('href')
            self.__count = self.__count + 1
            self.__href_value[self.__count] = attribute_value
            if len(self.__href_value) == 10:
                break
        json_href_value = json.dumps(self.__href_value, indent=4)
        with open(f"{self.__testData}/href_value.json", "w") as outfile:
            outfile.write(json_href_value)

    def navigate_to_href_links(self):
        f = open(f"{self.__testData}/href_value.json")
        json_data = json.load(f)
        for links in json_data:
            BaseClass.navigate_to_link(json_data[links])
        f.close()
