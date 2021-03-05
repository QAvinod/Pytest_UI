from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport
from Scripts.MassInterview.crpo_enable_auto_assign import EnableAutoAssign
from Scripts.MassInterview.crpo_event_change_applicant_status import EventApplicant
from Scripts.MassInterview.crpo_event_slot_configuration import SlotConfiguration
from Scripts.MassInterview.crpo_candidate_login import CandidateLobbyLogin
from Scripts.MassInterview.crpo_room_create import Room


class MassInterviewFlow:
    """
        Required class Objects are created
    """
    time = input('slot time (ex:- 10:10 AM) ::')
    environment = ''
    login_success = ''
    login_link = ''
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
        allocation = EnableAutoAssign(driver=driver, index=index)
        room = Room(driver=driver, index=index, version=version)
        candidate = CandidateLobbyLogin(driver=driver)

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

    def auto_allocation_configuration(self):
        self.status.event()
        self.MASS_OUTPUT.event_report(4, 5, self.status.event_collection)

        self.allocation.auto_allocation_user_chat()
        self.MASS_OUTPUT.auto_allocation_report(self.allocation.event_config_collection)

    def slot_configuration(self):
        self.slot.slot_configurations(self.id)
        self.login_link = self.slot.slot_config.candidate_login_link
        self.MASS_OUTPUT.slot_config_report(self.slot.event_slot_collection)

    def room_creation(self):
        self.room.create_room()
        self.MASS_OUTPUT.create_room_report(self.room.room_collection)

    def candidate_lobby(self):
        self.candidate.candidate_lobby_login(self.id)


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.applicant_status_change()
    Object.auto_allocation_configuration()
    Object.slot_configuration()
    Object.room_creation()
    Object.MASS_OUTPUT.overall_status()
    Object.environment.close()
