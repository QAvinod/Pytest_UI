from Config import outputFile
from utilities import excelWrite


class E2EOutputReport:
    def __init__(self, version, job_result_keys):
        self.__path = outputFile.OUTPUT_PATH['Mass_Interview_output']
        self.job_create = job_result_keys
        test_cases = 13
        excel_headers = ['E2E_Regression Creation', 'Status']
        color_headers = []
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def overall_status(self, start_date_time, version, server):
        self.xlw.status(start_date_time=start_date_time, version=version, server=server, path=self.__path)

    def dummy(self):
        self.xlw.input_data_verification(row=2, column=0, input_key='E2E_Regression Tab')
        self.xlw.input_data_verification(row=3, column=0, input_key='Create Button')
        self.xlw.input_data_verification(row=4, column=0, input_key='Name')
        self.xlw.input_data_verification(row=5, column=0, input_key='Attachment')
        self.xlw.input_data_verification(row=6, column=0, input_key='Description')

        self.xlw.common_result_pass(row=2, column=1, result_key=self.job_create[0], path=self.__path)
        self.xlw.common_result_pass(row=3, column=1, result_key=self.job_create[1], path=self.__path)
        self.xlw.common_result_pass(row=4, column=1, result_key=self.job_create[2], path=self.__path)
        self.xlw.common_result_pass(row=5, column=1, result_key=self.job_create[3], path=self.__path)
        self.xlw.common_result_pass(row=6, column=1, result_key=self.job_create[4], path=self.__path)
        self.xlw.common_result_pass(row=7, column=1, result_key=self.job_create[5], path=self.__path)
        self.xlw.common_result_pass(row=8, column=1, result_key=self.job_create[6], path=self.__path)
        self.xlw.common_result_pass(row=9, column=1, result_key=self.job_create[7], path=self.__path)
        self.xlw.common_result_pass(row=10, column=1, result_key=self.job_create[8], path=self.__path)
        self.xlw.common_result_pass(row=11, column=1, result_key=self.job_create[9], path=self.__path)
        self.xlw.common_result_pass(row=12, column=1, result_key=self.job_create[10], path=self.__path)
        self.xlw.common_result_pass(row=13, column=1, result_key=self.job_create[12], path=self.__path)
        self.xlw.common_result_pass(row=14, column=1, result_key=self.job_create[12], path=self.__path)
        self.xlw.common_result_pass(row=15, column=1, result_key=self.job_create[13], path=self.__path)
