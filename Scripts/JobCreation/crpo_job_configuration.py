from Config import inputFile
from utilities import excelRead, appTitle
from pageObjects.Pages.JobConfigurations import JobConfigurationPage


class CRPOJobConfiguration:
    def __init__(self, driver):
        self.driver = driver

        self.job_config = JobConfigurationPage(self.driver)
        self.tab_title = appTitle.Title(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_config_excel'], index=0)  # -- TODO
        xl = job_config_excel.excel_dict
        self.xl_jon_name_config = xl['job_name_config'][0]  # -- TODO
        self.xl_job_getby_tab_title = xl['Job_getby_tab_title'][0]

    def crpo_job_configurations(self):
        assert self.tab_title.tab_title(self.xl_job_getby_tab_title) == self.xl_job_getby_tab_title, \
            'Webdriver is in wrong tab'
        self.job_config.job_getbyid_validate(self.xl_jon_name_config)
