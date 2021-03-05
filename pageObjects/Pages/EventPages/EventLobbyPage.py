import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class LobbyPage:
    __e_create_button_xpath = Locators.BUTTONS['button'].format('Create Room')
    __e_room_name_xpath = Locators.PLACEHOLDER['text_ph'].format('Room Name')
    __e_interviewers_xpath = Locators.TITLE['title'].format('Select Interviewers')
    __e_participants_xpath = Locators.TITLE['title'].format('Select Participants')
    __e_search_xpath = Locators.TITLE['title'].format('Type here to search')
    __e_select_all_xpath = Locators.MULTI_SELECTIONS['moveAllItemsRight']
    __e_done_button = Locators.BUTTONS['all_buttons'].format('Done')

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)

    def create_room_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_create_button_xpath, 'room_create_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def room_name(self, room_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_room_name_xpath, room_name, 'room_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_interviewers_xpath, 'Interviewers_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_participants(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_participants_xpath, 'Participants_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search(self, key):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_participants_xpath, key, 'Search_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def move_all(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_all_xpath, 'Move_all_items')
            return True
        except Exception as error:
            ui_logger.error(error)

    def done(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_done_button, 'Done_button')
            return True
        except Exception as error:
            ui_logger.error(error)
