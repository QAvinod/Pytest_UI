from utilities import excelWrite
from Config import outputFile


class MassOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Mass_Interview_output']
        test_cases = 60
        excel_headers = ['Event', 'Status', 'Applicant (Change Status)', 'Status', 'Event (Slot Config)', 'Status',
                         'Configurations (Auto Allocation)', 'Status', 'Slot', 'Status']
        color_headers = ['Event', 'Applicant (Change Status)', 'Event (Slot Config)',
                         'Configurations (Auto Allocation)', 'Slot', 'Status']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='MASS INTERVIEW FLOW')

    def event_report(self, i_column, o_column, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Search Action', 'Search Button',
                            'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     i_column=i_column, o_column=o_column, path=self.__path)

    def event_applicant_report(self, event_app_coll):
        testdata_headers = ['Event Actions', 'View Applicant Action', 'Applicant Advance Search',
                            'Applicant Name Enter', 'Search Button', 'Select Applicant', 'Change Status Action',
                            'Stage Field', 'Status Field', 'Comment', 'Change Button', 'Applicant Name Click',
                            'Switch window', 'Applicant status Validate', 'Candidate Id Copied',
                            'Close window', 'Switch to original window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_app_coll,
                                     i_column=2, o_column=3, path=self.__path)

    def auto_allocation_report(self, auto_allocation_coll):
        testdata_headers = ['Configurations Tab', 'Allocation - On', 'Chat - Click', 'Search chat user', 'Enable chat',
                            'Save Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=auto_allocation_coll,
                                     i_column=6, o_column=7, path=self.__path)

    def slot_config_report(self, slot_config_coll):
        testdata_headers = ['Event Actions', 'Event Slot Action', 'Click to select stage', 'Entered Stage-Status',
                            'Go Button', 'Enter No.of Slots', 'Go Button', 'Date Field', 'Count Field',
                            'Clear time Field', 'Enter time Field', 'Assign slot button', 'Assign slot - Ok',
                            'Communicate slot - Ok', 'Search Id', 'Search Button', 'Link action', 'LoginLink - Copied',
                            'Cancel Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=slot_config_coll,
                                     i_column=8, o_column=9, path=self.__path)

    def create_room_report(self, room_coll):
        testdata_headers = ['Event Actions', 'Interview Lobby', 'Create room', 'Room Name Field', 'Select interviewers',
                            'Search Interviewers', 'Move all', 'Done', 'Select Participants', 'Search Participants',
                            'Move all', 'Done']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=room_coll,
                                     i_column=10, o_column=11, path=self.__path)
