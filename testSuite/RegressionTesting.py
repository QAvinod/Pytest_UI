from Config import Enviroment
from Scripts.LoginPage.crpo_login_page import CRPOLogin
from Scripts.JobCreation.crpo_job_creation import CRPOJobCreation
from Scripts.JobCreation.crpo_job_configuration import CRPOJobConfiguration


class CRPOE2ERegression:

    """ Environment setup object with index / version instances
    """
    environment = Enviroment.EnvironmentSetup()
    if environment.server == 'amsin':
        index = 0
        version = environment.sprint_version
    else:
        index = 1
        version = environment.sprint_version

    """ Required class Objects are created 
    """
    driver = environment.driver
    login = CRPOLogin(driver, index)
    job = CRPOJobCreation(driver, index, version)
    job_config = CRPOJobConfiguration(driver, index, version)

    def crpo_login(self):
        self.login.crpo_login()

    def crpo_job(self):
        self.job.crpo_job_creation()

    def crpo_job_config(self):
        self.job_config.crpo_job_configurations()


o = CRPOE2ERegression()
o.crpo_login()
o.crpo_job()
o.crpo_job_config()
