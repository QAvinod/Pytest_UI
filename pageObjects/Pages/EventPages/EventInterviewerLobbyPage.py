import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class InterviewerLobbyPage:

    __e_select_candidate_xpath = Locators.BUTTONS['button'].format('Select Candidate')
    __e_provide_feedback_xpath = Locators.BUTTONS['actionClicked'].format("'", 'provideFeedBack', "'")
    __e_provide_select_drop_css = Locators.FEEDBACK['select_drop_down']
    __e_provide_comment_xpath = Locators.FEEDBACK['comments']
    __e_provide_overall_css = Locators.FEEDBACK['overall']
    __e_invite_video_xpath = Locators.BUTTONS['actionClicked'].format("'", 'markAsCurrentCandidate', "'")
    __e_invite_check_xpath = Locators.CHECK_BOX['check_box']
    __e_proceed_xpath = Locators.BUTTONS['button'].format('Proceed To Interview')
    __e_finish_interview_xpath = Locators.BUTTONS['button'].format('Interview is Finished')
    __e_decision_button_xpath = Locators.FEEDBACK['decision_button']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def select_candidate(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_candidate_xpath, 'select_candidate')
            return True
        except Exception as error:
            ui_logger.error(error)

    def provide_feedback(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_provide_feedback_xpath, 'provide_feedback')
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_decision(self, decision):
        try:
            self.wait.web_elements_wait_click(By.XPATH, self.__e_decision_button_xpath, decision)
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_comments(self, comment):
        try:
            self.wait.web_elements_wait_send_keys(By.XPATH, self.__e_provide_comment_xpath, comment)
            return True
        except Exception as error:
            ui_logger.error(error)

    def overall_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.CSS_SELECTOR, self.__e_provide_overall_css, comment,
                                                 'overall_comment')
            return True
        except Exception as error:
            ui_logger.error(error)

    def invite_video_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_invite_video_xpath, 'invite_video_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def check_box(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_invite_check_xpath, 'invite_check_box')
            return True
        except Exception as error:
            ui_logger.error(error)

    def proceed_video_link(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_proceed_xpath, 'proceed_video_link')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def finish_interview(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_finish_interview_xpath, 'finish_interview')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_select_drop_down(self, value):
        try:
            self.wait.web_elements_wait_send_keys(By.XPATH, self.__e_provide_select_drop_css, value)
            return True
        except Exception as error:
            ui_logger.error(error)
