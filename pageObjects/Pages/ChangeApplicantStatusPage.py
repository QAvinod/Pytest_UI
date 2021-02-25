from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities import appTitle
from utilities.WebDriver_Wait import WebElementWait
from selenium.webdriver.common.by import By
from utilities.menu import Menu


class ApplicantStatus:
    __e_search_id = Locators.SEARCH['advance_search']
    __e_name_name = Locators.SEARCH['name']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.tab_title = appTitle.Title(self.driver)

    def event_tab(self, tab_name, tab_title):
        try:
            self.tab.event_tab(tab_name)
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True

        except Exception as error:
            ui_logger.error(error)

    def name_field(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_id)
            return True

        except Exception as error:
            ui_logger.error(error)