import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class EventSlot:

    __e_current_status_xpath = Locators.TITLE['title'].format('Current Status')
    __e_search_status_xpath = Locators.TITLE['title'].format('Type here to search')
    __e_select_search_item_xpath = Locators.MULTI_SELECTIONS['moveAllItemsRight']
    __e_done_button_xpath = Locators.BUTTONS['done']
    __e_slot_number_xpath = Locators.PLACEHOLDER['num_ph'].format('No. Of Slots')
    __e_go_button_xpath = Locators.BUTTONS['button'].format('Go')
    __e_date_field_xpath = Locators.PLACEHOLDER['place_holder'].format('From Date')
    __e_time_field_xpath = Locators.PLACEHOLDER['place_holder'].format('From Time')
    __e_count_field_xpath = Locators.PLACEHOLDER['num_ph'].format('Count')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def current_applicant_status_choose(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_current_status_xpath,
                                             'Slot_applicant_current_status_click')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_status_select(self, stage_status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_search_status_xpath, stage_status, 'Entered_status')
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_search_item_xpath, 'Move_all_items')
            self.wait.web_element_wait_click(By.XPATH, self.__e_done_button_xpath, 'Done_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def slot_number(self, number_of_slots):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_slot_number_xpath, number_of_slots,
                                                 'Entered_status')
            return True
        except Exception as error:
            ui_logger.error(error)

    def go_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_go_button_xpath, 'Go_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def date_field(self, date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_date_field_xpath, date, 'date_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def time_field(self, clock):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_time_field_xpath, clock, 'time_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def count_field(self, count):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_count_field_xpath, count, 'count_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def clear_time_field(self):
        try:
            self.wait.clear(By.XPATH, self.__e_time_field_xpath, 'clear_time_field')
            return True
        except Exception as error:
            ui_logger.error(error)
