from Config import Enviroment
from Scripts.LoginPage.crpo_login_page import CRPOLogin
from Scripts.JobCreation.crpo_job_creation import CRPOJobCreation
from Scripts.JobCreation.crpo_job_configuration import CRPOJobConfiguration


class CRPOE2ERegression:

    environment = Enviroment.EnvironmentSetup()
    driver = environment.driver

    login = CRPOLogin(driver)

    job = CRPOJobCreation(driver)
    job_config = CRPOJobConfiguration(driver)

    def crpo_login(self):
        self.login.crpo_login()

    def crpo_job(self):
        self.job.crpo_job_creation()
        self.job_config.crpo_job_configurations()


o = CRPOE2ERegression()
o.crpo_login()
o.crpo_job()
