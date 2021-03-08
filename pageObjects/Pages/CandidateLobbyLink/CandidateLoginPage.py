import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.OpenNewTab import NewTab


class LoginPage:

    __e_candidate_id_xpath = Locators.PLACEHOLDER['text_ph'].format('Enter Candidate Id')
    __e_enter_button_xpath = Locators.BUTTONS['button'].format('Enter the room')
    __e_candidate_name_xpath = Locators.CANDIDATE_LOBBY_LOGIN['candidate_name']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.new_tab = NewTab(self.driver)

    def open_link(self, link_to_login):
        try:
            self.new_tab.open_new_tab(1, link_to_login)
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_screen(self, candidate_id):
        try:
            self.wait.loading()
            self.wait.web_element_wait_send_keys(By.XPATH,
                                                 self.__e_candidate_id_xpath, candidate_id, 'candidate_login_screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def enter_to_room(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_enter_button_xpath, 'enter_to_room_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_name_validate(self, candidate_name):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_candidate_name_xpath.format(candidate_name),
                                            'candidate_name_validation_lobby')
            if self.wait.text_value in self.wait.text_value:
                print(f'Lobby Candidate name - {self.wait.text_value}')
                return True
            return True
        except Exception as error:
            ui_logger.error(error)
