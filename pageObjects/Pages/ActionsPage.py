from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class Actions:
    __e_action_dropdown_click = Locators.ACTIONS['actions_click']

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)

    def actions_click(self):
        self.wait.web_element_wait_click(By.ID, self.__e_action_dropdown_click)

    def actions_name(self, action_name):
        self.wait.web_element_wait_click(By.ID, action_name)

    def float_click(self, action_name):
        self.wait.web_element_wait_click(By.ID, action_name)

    def floating_action(self, action_name):
        self.wait.web_element_wait_click(By.ID, action_name)
