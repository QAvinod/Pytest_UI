import time
from utilities import appTitle
from utilities.menu import Menu
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class CandidateDetailsPage:
    __e_title_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def candidate_status(self, changed_status):
        try:
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.wait.loading()
            self.wait.web_element_wait_text(By.XPATH, self.__e_title_xpath.format(changed_status),
                                            f'Candidate_status_{changed_status}')
            if self.wait.text_value == changed_status:
                print(f'Candidate status changed - {self.wait.text_value}')

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return True
        except Exception as error:
            ui_logger.error(error)
