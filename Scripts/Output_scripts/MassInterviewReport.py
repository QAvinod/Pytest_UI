from utilities import excelWrite


class MassInterviewOutputReport:
    def __init__(self, version, mass_result_keys):
        self.mass = mass_result_keys
        test_cases = 13
        excel_headers = ['Job Creation', 'Status']
        color_headers = []
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def overall_status(self, start_date_time, version, server):
        self.xlw.status(start_date_time=start_date_time, version=version, server=server)

    def dummy(self):
        self.xlw.input_data_verification(row=2, column=0, input_key='Job Tab')
        self.xlw.input_data_verification(row=3, column=0, input_key='Create Button')

        self.xlw.common_result_pass(row=2, column=1, result_key=self.mass[0])
        self.xlw.common_result_pass(row=3, column=1, result_key=self.mass[1])


