from Config import inputFile
from datetime import datetime
from utilities import excelRead
from pageObjects.Pages.LoginPages.LoginPage import Login


class InterviewLogin:
    def __init__(self, driver, index):
        now = datetime.now()

        self.driver = driver
        self.login = Login(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = slot_excel.excel_dict
        self.xl_account_name = xl['account_name'][0]

        self.int_collection = []

    def interviewer_login(self):
        self.int_collection = []
        __list = [self.login.login_account_click(self.xl_account_name),
                  self.login.login_out(),
                  self.login.click_here_to_login()
                  ]
        for func in __list:
            if func:
                self.int_collection.append(func)
            else:
                self.int_collection.append(func)
