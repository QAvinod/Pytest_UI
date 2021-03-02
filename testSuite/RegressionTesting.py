from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.E2E_Regression.crpo_job_creation import CRPOJobCreation
from Scripts.E2E_Regression.crpo_job_configuration import CRPOJobConfiguration
from Scripts.Output_scripts import E2EReport


class CRPOE2ERegression:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        login = CRPOLogin(driver=driver, index=index)
        job = CRPOJobCreation(driver=driver, index=index, version=version)
        job_config = CRPOJobConfiguration(driver=driver, index=index, version=version)

        E2E_output = E2EReport.E2EOutputReport(version=version, job_result_keys=job.coll)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)

    def crpo_job(self):
        self.job.crpo_job_creation()

    def crpo_job_config(self):
        self.job_config.crpo_job_configurations()


Object = CRPOE2ERegression()
Object.crpo_login()

if Object.login_success:
    Object.crpo_job()
    # Object.crpo_job_config()
    # Object.E2E_output.dummy()
    Object.E2E_output.overall_status(start_date_time=Object.date_time, version=Object.version, server=Object.server)
    Object.environment.close()
