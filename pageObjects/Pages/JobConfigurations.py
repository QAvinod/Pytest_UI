from selenium.webdriver.common.by import By

from pageObjects import Locators
from utilities.appTitle import Title
from utilities.Actions import Actions
from utilities.WebDriver_Wait import WebElementWait


class JobConfigurationPage:

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.tab = Title(self.driver)
        self.action = Actions(self.driver)

    def job_getbyid_validate(self, job_name):
        self.wait.web_element_wait_text(By.XPATH, job_name)
        if self.wait.text_value == job_name:
            print('job validated')

# -- TODO


