from Config import inputFile
from pageObjects.Pages import ChangeApplicantStatusPage, EventGetByNamePage, EventApplicantPage
from utilities import excelRead


class EventApplicant:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.search = ChangeApplicantStatusPage.ApplicantStatus(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.applicant_grid = EventApplicantPage.EventApplicant(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_stage = xl['stage'][0]
        self.xl_status = xl['status'][0]
        self.xl_comment = xl['comment'][0]

        self.event_collection = []
        self.applicant_collection = []

    def event_transactions(self):
        __list = [self.search.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event_name),
                  self.getby.event_actions_click(),
                  self.getby.event_view_candidates()
                  ]
        for func in __list:
            if func:
                self.event_collection.append(func)
            else:
                self.event_collection.append(func)

    def event_applicant_grid(self):
        __list = [self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_event_name),
                  self.search.search_button(),
                  self.applicant_grid.select_applicant(),
                  self.applicant_grid.change_status_action(),
                  self.applicant_grid.applicant_stage(self.xl_stage),
                  self.applicant_grid.applicant_status(self.xl_status),
                  self.applicant_grid.comment(self.xl_comment),
                  self.applicant_grid.change_button()
                  ]
        for func in __list:
            if func:
                self.applicant_collection.append(func)
            else:
                self.applicant_collection.append(func)
