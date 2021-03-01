from utilities import ExcelIndexVersion
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport
from Scripts.MassInterview.crpo_event_change_applicant_status import EventApplicant
from Scripts.MassInterview.crpo_event_slot_configuration import SlotConfiguration


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
        slot = SlotConfiguration(driver=driver, index=index)

        MASS_output = MassInterviewReport.MassInterviewOutputReport(version=version, event_coll=status.event_collection,
                                                                    event_action_coll=status.event_action_collection,
                                                                    event_app_coll=status.applicant_collection,
                                                                    slot_coll=slot.event_slot_action_collection,
                                                                    slot_config_coll=slot.event_slot_collection)

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
        self.status.event()
        self.MASS_output.event_report(0, 1)

        self.status.event_actions()
        self.MASS_output.event_actions_report()

        self.status.event_applicant_grid()
        self.MASS_output.event_applicant_report()

    def slot_configuration(self):
        self.status.event()
        self.MASS_output.event_report(4, 5)

        self.slot.slot_action()
        self.MASS_output.slot_action_report()

        self.slot.slot_configurations()
        self.MASS_output.slot_config_report()


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.applicant_status_change()
    Object.slot_configuration()
    Object.MASS_output.overall_status(start_date_time=Object.environment.start_date_time,
                                      version=Object.environment.sprint_version,
                                      server=Object.environment.server)
    Object.Excel_Index_version.environment.close()
