from pageObjects.Pages import ChangeApplicantStatusPage

class EventApplicant:

    def __init__(self, driver):
        self.driver = driver
        self.c_a_s = ChangeApplicantStatusPage.ApplicantStatus(driver)

    def change_status(self):
        self.c_a_s.event_tab()
        self.c_a_s.name_field()
