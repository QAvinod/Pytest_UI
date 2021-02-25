from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from selenium.webdriver.common.by import By


class Search:
    __e_search_id = Locators.SEARCH['advance_search']
    __e_name_name = Locators.SEARCH['name']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def advance_search(self):
        self.wait.web_element_wait_click(By.XPATH, self.__e_search_id)

    def name_search(self, name_input):
        self.wait.web_element_wait_send_keys(By.NAME, self.__e_name_name, name_input)
