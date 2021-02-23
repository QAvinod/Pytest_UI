from utilities import excelWrite


class E2EOutputReport:
    def __init__(self, version):

        test_cases = 88
        excel_headers = ['vinod', 'sree']
        color_headers = ['sree']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def dummy(self):
        self.xlw.input_data_verification(row=2, column=0, input_key='vinnod')
        self.xlw.input_data_verification(row=3, column=0, input_key='sreee')

        self.xlw.common_result_pass(row=2, column=1, result_key='Pass')
        self.xlw.common_result_pass(row=3, column=1, result_key='Pass')

    def overall_status(self, start_date_time, version, server):
        self.xlw.status(start_date_time=start_date_time, version=version, server=server)
