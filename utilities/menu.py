import time
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class Menu:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def menu_collection(self, user_name):
        result = ''
        self.wait.web_elements_wait(By.TAG_NAME, 'a')
        for i in self.wait.perform:
            if i.text.strip() == user_name:
                i.click()
                break
        return result
