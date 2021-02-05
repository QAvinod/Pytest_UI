from Config import inputFile
from utilities import appTitle, excelRead
from Scripts.LoginPage.crpo_login_page import CRPOLogin
from pageObjects.Pages.CreateJobPage import JobCreationPage


class JobCreation:
    def __init__(self):
        self.login = CRPOLogin()
        self.login.crpo_login()
        self.job = JobCreationPage(self.login.driver)
        self.tab_title = appTitle.Title(self.login.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['job_excel'], index=0)
        xl = excel.excel_dict
        self.xl_job_name = xl['job_name'][0]
        self.xl_job_desc = xl['job_description'][0]
        self.xl_job_loc = xl['job_location'][0]
        self.xl_job_hm = xl['job_hm'][0]
        self.xl_job_bu = xl['job_bu'][0]
        self.xl_job_openings = xl['job_openings'][0]
        self.xl_job_male = xl['job_male'][0]
        self.xl_job_female = xl['job_female'][0]

        # ---- Attachment from local machine
        self.job_attachment_file = inputFile.INPUT_PATH['job_attachment']

    def crpo_job_creation(self):
        self.job.job_tab('Job Roles')
        assert self.tab_title.tab_title('CRPO - Job Roles') == 'CRPO - Job Roles', 'Webdriver is in wrong tab'
        self.job.create_button()
        self.job.job_name(self.xl_job_name)
        self.job.job_attachment(self.job_attachment_file)
        self.job.file_upload_notifier()
        self.job.job_description(self.xl_job_desc)
        self.job.job_location(self.xl_job_loc)
        self.job.job_hiring_manager(self.xl_job_hm)
        self.job.job_business_unit(self.xl_job_bu)
        self.job.job_openings(self.xl_job_openings)
        self.job.job_male_diversity(self.xl_job_male)
        self.job.job_female_diversity(self.xl_job_female)


o = JobCreation()
o.crpo_job_creation()
