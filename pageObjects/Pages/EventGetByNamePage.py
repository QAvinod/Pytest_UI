import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class EventGetByName:

    __e_click_name_xpath = Locators.TITLE['title'].format('Click to view full details')
    __e_event_name_xpath = Locators.TITLE['title']
    __e_event_actions_xpath = Locators.ACTIONS['actions_click']
    __e_event_candidates_id = Locators.ACTIONS['view_candidates']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def event_name_click(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_click_name_xpath, 'Event_name_click')
            time.sleep(3)
            self.wait.loading()

            return True
        except Exception as error:
            ui_logger.error(error)

    def event_name_validation(self, event_name):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_event_name_xpath.format(event_name),
                                            'Event_name_validation')
            print('MassInterview Name -', self.wait.text_value)
            time.sleep(2)
            self.wait.web_element_wait_click(By.XPATH,
                                             self.__e_event_name_xpath.format(event_name),
                                             'Event_name_validation')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_actions_click(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_actions_xpath, 'Event_actions_click')
            print('MassInterview Actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_view_candidates(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_event_candidates_id, 'Event_candidates_action')
            self.wait.loading()
            print('MassInterview View Applicant - Screen')
            return True
        except Exception as error:
            ui_logger.error(error)
