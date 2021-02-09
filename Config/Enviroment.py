from selenium import webdriver
from utilities import ReadConfigFile
from webdriver_manager.chrome import ChromeDriverManager


class EnvironmentSetup:
    def __init__(self):
        self.server = input('Please Enter testing Environment:: ')
        self.sprint_version = input('Please Enter Sprint version:: ')

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

        if self.server == 'amsin':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
        elif self.server == 'ams':
            self.driver.get(ReadConfigFile.ReadConfig.get_production_url())
