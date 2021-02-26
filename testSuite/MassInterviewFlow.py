from utilities import ExcelIndexVersion
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport
from Scripts.Event.crpo_event_transaction import EventApplicant


class MassInterviewFlow:
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
        status = EventApplicant(driver=driver, index=index, version=version)

        MASS_output = MassInterviewReport.MassInterviewOutputReport(version=version,
                                                                    event_coll=status.event_collection,
                                                                    event_app_coll=status.applicant_collection)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True
        except Exception as error:
            ui_logger.error(error)

    def applicant_status_change(self):
        self.status.event_transactions()
        self.status.event_applicant_grid()

        self.MASS_output.event_transactions_report()
        self.MASS_output.event_applicant_report()


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.applicant_status_change()
    Object.MASS_output.overall_status(start_date_time=Object.environment.start_date_time,
                                      version=Object.environment.sprint_version,
                                      server=Object.environment.server)
    # Object.Excel_Index_version.environment.close()
