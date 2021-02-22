from utilities import ExcelIndexVersion
from Scripts.LoginPage.crpo_login_page import CRPOLogin
from Scripts.JobCreation.crpo_job_creation import CRPOJobCreation
from Scripts.JobCreation.crpo_job_configuration import CRPOJobConfiguration


class CRPOE2ERegression:

    Excel_Index_version = ExcelIndexVersion.IndexVersion()
    environment = Excel_Index_version.environment
    index = Excel_Index_version.index
    version = Excel_Index_version.version

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
if o.crpo_login():
    o.crpo_job()
    o.crpo_job_config()
    o.Excel_Index_version.environment.close()
