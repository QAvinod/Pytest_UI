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
    id = ''

    """
    Environment setup instance and other required function instances
    """
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

        MASS_OUTPUT = MassInterviewReport.MassOutputReport(version=version, server=server, start_date_time=date_time)

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
        self.MASS_OUTPUT.event_report(0, 1, self.status.event_collection)

        self.status.event_applicant_grid()
        self.id = self.status.candidate_details.candidate_id
        self.MASS_OUTPUT.event_applicant_report(self.status.applicant_collection)

    def slot_configuration(self):
        self.status.event()
        self.MASS_OUTPUT.event_report(4, 5,  self.status.event_collection)

        self.slot.slot_configurations(self.id)
        self.MASS_OUTPUT.slot_config_report(self.slot.event_slot_collection)


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.applicant_status_change()
    Object.slot_configuration()
    Object.MASS_OUTPUT.overall_status()
    Object.environment.close()
