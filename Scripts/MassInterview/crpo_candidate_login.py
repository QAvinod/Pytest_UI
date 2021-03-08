from Config import inputFile
from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CandidateLobbyLogin:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.candidate_login = LoginPage(self.driver)
        self.new_tab = SwitchWindowClose(self.driver)
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['candidate_lobby'], index=index)
        xl = status_excel.excel_dict
        self.xl_candidate_name = xl['name'][0].format(version)

        self.candidate_lobby_collection = []

    def candidate_lobby_login(self, candidate_id, candidate_login_link):

        self.candidate_lobby_collection = []
        __list = [self.candidate_login.open_link(candidate_login_link),
                  self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room(),
                  self.candidate_login.candidate_name_validate(self.xl_candidate_name),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.candidate_lobby_collection.append(func)
            else:
                self.candidate_lobby_collection.append(func)
