import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class LoginPage:

    __e_candidate_id_xpath = Locators.PLACEHOLDER['text_ph'].format('Enter Candidate Id')
    __e_enter_button_xpath = Locators.BUTTONS['button'].format('Enter the room')
    __e_candidate_name_xpath = Locators.CANDIDATE_LOBBY_LOGIN['candidate_name']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def login_screen(self, candidate_id):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH,
                                                 self.__e_candidate_id_xpath, candidate_id, 'candidate_login_screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def enter_to_room(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_enter_button_xpath, 'enter_to_room_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_name_validate(self, candidate_name):
        try:
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_candidate_name_xpath.format(candidate_name),
                                            'enter_to_room_button')
            return True
        except Exception as error:
            ui_logger.error(error)
