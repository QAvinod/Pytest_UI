from utilities import ExcelIndexVersion
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport


class CRPOE2ERegression:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        Excel_Index_version = ExcelIndexVersion.IndexVersion()
        environment = Excel_Index_version.environment
        index = Excel_Index_version.index
        version = Excel_Index_version.version

        driver = environment.driver
        login = CRPOLogin(driver=driver, index=index)

        E2E_output = MassInterviewReport.MassInterviewOutputReport(version=version, mass_result_keys='')

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)


Object = CRPOE2ERegression()
Object.crpo_login()

if Object.login_success:
    Object.E2E_output.overall_status(start_date_time=Object.environment.start_date_time,
                                     version=Object.environment.sprint_version,
                                     server=Object.environment.server)
    Object.Excel_Index_version.environment.close()
