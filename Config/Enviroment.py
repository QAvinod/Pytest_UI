import datetime
from selenium import webdriver
from utilities import ReadConfigFile
from webdriver_manager.chrome import ChromeDriverManager


class EnvironmentSetup:
    def __init__(self):
        self.server = input('Please Enter testing Environment:: ')
        self.sprint_version = input('Please Enter Sprint version:: ')
        self.start_date_time = datetime.datetime.now()
        print("Run started at:: "+str(self.start_date_time))

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

        if self.server == 'qa':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
        elif self.server == 'dev':
            self.driver.get(ReadConfigFile.ReadConfig.get_production_url())
        elif self.server == 'beta':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_url())
        elif self.server == 'stage':
            self.driver.get(ReadConfigFile.ReadConfig.get_stage_url())
        elif self.server == 'india':
            self.driver.get(ReadConfigFile.ReadConfig.get_indiaams_url())

    def close(self):
        print("Run completed at:: " + str(datetime.datetime.now()))
        self.driver.close()
