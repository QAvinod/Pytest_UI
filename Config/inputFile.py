import os

PATH = os.getenv("HOME")
GENERIC_INPUT_PATH = "%s/PythonFrameWorkNew/Pytest_UI/testData/" % PATH

INPUT_PATH = {
    'login_excel': GENERIC_INPUT_PATH + 'Login_Details.xls',
    'job_excel': GENERIC_INPUT_PATH + 'Job_Details.xls',
    'job_attachment': GENERIC_INPUT_PATH + 'job-description.pdf',
    'job_config_excel': GENERIC_INPUT_PATH + 'Job_Configurations.xls'
}
