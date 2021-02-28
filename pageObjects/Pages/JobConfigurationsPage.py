from selenium.webdriver.common.by import By

from pageObjects import Locators
from utilities.appTitle import Title
from pageObjects.Pages.ActionsPage import Actions
from utilities.WebDriver_Wait import WebElementWait


class JobConfigurationPage:

    __e_job_name_title = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.tab = Title(self.driver)
        self.action = Actions(self.driver)

    def job_getbyid_validate(self, job_name):
        self.driver.execute_script("window.scrollTo(0,200);")
        self.wait.web_element_wait_text(By.XPATH, self.__e_job_name_title.format(job_name))
        if self.wait.text_value == job_name:
            print('job validated')

# -- TODO


