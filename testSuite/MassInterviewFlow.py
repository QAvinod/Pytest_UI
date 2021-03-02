from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport
from Scripts.MassInterview.crpo_event_change_applicant_status import EventApplicant
from Scripts.MassInterview.crpo_event_slot_configuration import SlotConfiguration


class MassInterviewFlow:
    """
        Required class Objects are created
    """
    time = input('slot time (ex:- 10:10 AM) ::')
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
        status = EventApplicant(driver=driver, index=index, version=version)
        slot = SlotConfiguration(driver=driver, index=index, time=time)

        MASS_output = MassInterviewReport.MassOutputReport(version=version, event_coll=status.event_collection,
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
    Object.MASS_output.overall_status(start_date_time=Object.date_time, version=Object.version, server=Object.server)
    Object.environment.close()
