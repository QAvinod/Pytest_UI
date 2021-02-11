import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class Login:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_tenant_name = Locators.LOGIN['alias']
    __e_next_button_css = Locators.LOGIN['next']
    __e_login_name_l = Locators.LOGIN['login_name']
    __e_password_xpath = Locators.LOGIN['password']
    __e_login_button_css = Locators.LOGIN['login']
    __e_anchor_tag = Locators.TAG['anchor']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def tenant(self, tenant_name):
        self.wait.web_element_wait_send_keys(By.NAME, self.__e_tenant_name, tenant_name)

    def next_button(self):
        self.wait.web_element_wait_click(By.CSS_SELECTOR, self.__e_next_button_css)

    def login_name(self, login_name):
        time.sleep(1.5)
        self.wait.web_element_wait_send_keys(By.NAME, self.__e_login_name_l, login_name)

    def password(self, password):
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_password_xpath, password)

    def login_button(self):
        self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_login_button_css)

    def login_account_name_verification(self, user_name):
        self.wait.loading()
        assert self.wait.web_elements_wait_text(By.TAG_NAME, self.__e_anchor_tag, user_name) == user_name, \
            'Logged in different account please check the details'
