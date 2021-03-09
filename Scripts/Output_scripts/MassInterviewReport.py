from utilities import excelWrite
from Config import outputFile


class MassOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Mass_Interview_output']
        test_cases = 100
        excel_headers_1 = ['Event', 'Status', 'Applicant (Change Status)', 'Status', 'Event (Slot Config)', 'Status',
                           'Configurations (Auto Allocation)', 'Status', 'Slot', 'Status', 'Room Creation', 'Status',
                           'Candidate Login', 'Status']
        color_headers_1 = ['Status', 'Event', 'Applicant (Change Status)', 'Event (Slot Config)', 'Slot',
                           'Room Creation', 'Configurations (Auto Allocation)', 'Candidate Login']

        excel_headers_2 = ['Assign Room', 'Status']
        color_headers_2 = ['Status', 'Assign Room']

        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)
        self.xlw.excel_header_by_index(row=21, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='MASS INTERVIEW FLOW')

    def event_report(self, i_column, o_column, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Search Action', 'Search Button',
                            'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=i_column, o_column=o_column, path=self.__path)

    def event_applicant_report(self, event_app_coll):
        testdata_headers = ['Event Actions', 'View Applicant Action', 'Applicant Advance Search',
                            'Applicant Name Enter', 'Search Button', 'Select Applicant', 'Change Status Action',
                            'Stage Field', 'Status Field', 'Comment', 'Change Button', 'Applicant Name Click',
                            'Switch window', 'Applicant status Validate', 'Candidate Id Copied',
                            'Close window', 'Switch to original window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_app_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def auto_allocation_report(self, auto_allocation_coll):
        testdata_headers = ['Configurations Tab', 'Allocation - On', 'Chat - Click', 'Search chat user', 'Enable chat',
                            'Save Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=auto_allocation_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def slot_config_report(self, slot_config_coll):
        testdata_headers = ['Event Actions', 'Event Slot Action', 'Click to select stage', 'Entered Stage-Status',
                            'Go Button', 'Enter No.of Slots', 'Go Button', 'Date Field', 'Count Field',
                            'Clear time Field', 'Enter time Field', 'Assign slot button', 'Assign slot - Ok',
                            'Communicate slot - Ok', 'Search Id', 'Search Button', 'Link action', 'LoginLink - Copied',
                            'Cancel Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=slot_config_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def create_room_report(self, room_coll):
        testdata_headers = ['Event Actions', 'Interview Lobby', 'Create room', 'Room Name Field', 'Select interviewers',
                            'Search Interviewers', 'Move all', 'Done', 'Select Participants', 'Search Participants',
                            'Move all', 'Done', 'Created Room Button', 'Activate Room Action', 'Activated-Ok']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=room_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def candidate_login_report(self, candidate_login_coll):
        testdata_headers = ['Open Link-1st time', 'Enter Id', 'Enter Button', 'Name Validation',
                            'Almost there-Message', 'Close Tab', 'Switch to tab', 'Manage Candidate Tab',
                            'Un assign room action', 'Confirmation-Ok', 'Unassigned-Ok', 'Open Link-2nd time',
                            'Enter Id', 'Enter Button', 'Name Validation', 'wait to be queued-Message',
                            'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=candidate_login_coll,
                                     row=2, i_column=12, o_column=13, path=self.__path)

    def room_tag_report(self, room_tag_coll):
        testdata_headers = ['Advance Search', 'Room search Filed', 'Enter room name', 'Move all', 'Done',
                            'Search Button', 'No candidate message', 'Assign room Action',
                            'Room name filed', 'Assign room button', 'Confirmed-Ok', 'Advance Search',
                            'Room search Filed', 'Enter room name', 'Move all', 'Done', 'Search Button',
                            'Applicant name validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=room_tag_coll,
                                     row=22, i_column=0, o_column=1, path=self.__path)
