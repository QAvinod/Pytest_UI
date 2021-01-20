from selenium.webdriver.common.by import By

from pageObjects import Locators


class LoginPage:
    # Login Page
    tenant_name = Locators.LOGIN['alias']
    next_button_css = Locators.LOGIN['next']
    username_name = Locators.LOGIN['login_name']
    password_xpath = Locators.LOGIN['password']
    login_button_css = Locators.LOGIN['login']

    def __init__(self, driver):
        self.driver = driver

    def tenant(self, tenant_name):
        self.driver.find_element(By.NAME, self.tenant_name).send_keys(tenant_name)

    def next_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.next_button_css).click()

    def user_name(self, username):
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css).click()
