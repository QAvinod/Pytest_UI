from utilities import excelWrite
from Config import outputFile


class MassOutputReport:
    def __init__(self, version, event_coll, event_app_coll, slot_config_coll):
        self.__path = outputFile.OUTPUT_PATH['Mass_Interview_output']
        self.event = event_coll
        self.applicant = event_app_coll
        self.slot_config = slot_config_coll

        test_cases = 42
        excel_headers = ['Event', 'Status', 'Applicant (Change Status)', 'Status', 'Event (Slot Config)', 'Status',
                         'Slot', 'Status']
        color_headers = ['Event', 'Status', 'Applicant (Change Status)', 'Status', 'Event (Slot Config)', 'Status',
                         'Slot', 'Status']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def overall_status(self, start_date_time, version, server):
        self.xlw.status(start_date_time=start_date_time, version=version, server=server,
                        path=self.__path, excel_save_name='MASS INTERVIEW FLOW')

    def event_report(self, i_column, o_column):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Search Action', 'Search Button',
                            'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=self.event,
                                     i_column=i_column, o_column=o_column, path=self.__path)

    def event_applicant_report(self):
        testdata_headers = ['Event Actions', 'View Applicant Action', 'Applicant Advance Search',
                            'Applicant Name Enter', 'Search Button', 'Select Applicant', 'Change Status Action',
                            'Stage Field', 'Status Field', 'Comment', 'Change Button', 'Applicant Name Click',
                            'Switch window', 'Applicant status Validate', 'Candidate Id Copied',
                            'Close window', 'Switch to original window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=self.applicant,
                                     i_column=2, o_column=3, path=self.__path)

    def slot_config_report(self):
        testdata_headers = ['Event Actions', 'Event Slot Action', 'Click to select stage', 'Entered Stage-Status',
                            'Go Button', 'Enter No.of Slots', 'Go Button', 'Date Field', 'Count Field',
                            'Clear time Field', 'Enter time Field', 'Assign slot button', 'Assign slot - Ok',
                            'Communicate slot - Ok']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=self.slot_config,
                                     i_column=6, o_column=7, path=self.__path)
