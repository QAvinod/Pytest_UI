from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from selenium.webdriver.common.by import By


class Search:
    __e_anchor_tag = Locators.TAG['anchor']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def advance_search(self):
        self.wait.web_elements_wait_click(By.XPATH, self.__e_anchor_tag, 'Filters')
