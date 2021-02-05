from Config import inputFile, Enviroment
from utilities import excelRead, appTitle
from pageObjects.Pages.Loginpage import Login


class CRPOLogin:
    def __init__(self):

        setup = Enviroment.EnvironmentSetup()
        self.driver = setup.driver
        self.LoginPage = Login(self.driver)
        self.title = appTitle.Title(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['login_excel'], index=0)
        xl = excel.excel_dict
        self.xl_title = xl['c_title'][0]
        self.xl_tenant = xl['c_tenant'][0]
        self.xl_login = xl['c_login_name'][0]
        self.xl_user = xl['c_user_name'][0]
        self.xl_password = xl['c_password'][0]
        self.xl_logged_in_title = xl['c_logged_in_title'][0]

    def crpo_login(self):
        assert self.title.tab_title(self.xl_title) == self.xl_title
        self.LoginPage.tenant(self.xl_tenant)
        self.LoginPage.next_button()
        self.LoginPage.login_name(self.xl_login)
        self.LoginPage.password(self.xl_password)
        self.LoginPage.login_button()

        self.LoginPage.login_account_name_verification(self.xl_user)
        print(f'{self.xl_user} logged in successfully')
        self.title.tab_title(self.xl_title)
