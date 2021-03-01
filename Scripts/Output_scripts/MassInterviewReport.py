from utilities import excelWrite
from Config import outputFile


class MassInterviewOutputReport:
    def __init__(self, version, event_coll, event_action_coll,
                 event_app_coll, slot_coll, slot_config_coll):
        self.__path = outputFile.OUTPUT_PATH['Mass_Interview_output']
        self.event = event_coll
        self.event_action = event_action_coll
        self.applicant = event_app_coll
        self.slot_action = slot_coll
        self.slot_config = slot_config_coll

        test_cases = 50
        excel_headers = ['Event (Change Status)', 'Status', 'Applicant', 'Status', 'Event (Slot Config)', 'Status',
                         'Slot', 'Status']
        color_headers = ['Event (Change Status)', 'Status', 'Applicant', 'Status', 'Event (Slot Config)', 'Status',
                         'Slot', 'Status']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases,
                                               excel_headers_list=excel_headers,
                                               color_headers_list=color_headers)

    def overall_status(self, start_date_time, version, server):
        self.xlw.status(start_date_time=start_date_time, version=version, server=server,
                        path=self.__path, excel_save_name='MASS INTERVIEW FLOW')

    def event_report(self, i_column, o_column):
        self.xlw.input_data_verification(row=2, column=i_column, input_key='Event Tab')
        self.xlw.input_data_verification(row=3, column=i_column, input_key='Advance Search Action')
        self.xlw.input_data_verification(row=4, column=i_column, input_key='Event Name Enter')
        self.xlw.input_data_verification(row=5, column=i_column, input_key='Search Button')
        self.xlw.input_data_verification(row=6, column=i_column, input_key='Event Card Click')
        self.xlw.input_data_verification(row=7, column=i_column, input_key='Event validate')

        self.xlw.common_result_pass(row=2, column=o_column, result_key=self.event[0], path=self.__path)
        self.xlw.common_result_pass(row=3, column=o_column, result_key=self.event[1], path=self.__path)
        self.xlw.common_result_pass(row=4, column=o_column, result_key=self.event[2], path=self.__path)
        self.xlw.common_result_pass(row=5, column=o_column, result_key=self.event[3], path=self.__path)
        self.xlw.common_result_pass(row=6, column=o_column, result_key=self.event[4], path=self.__path)
        self.xlw.common_result_pass(row=7, column=o_column, result_key=self.event[5], path=self.__path)

    def event_actions_report(self):
        self.xlw.input_data_verification(row=8, column=0, input_key='Event Actions')
        self.xlw.input_data_verification(row=9, column=0, input_key='View Applicant Action')

        self.xlw.common_result_pass(row=8, column=1, result_key=self.event_action[0], path=self.__path)
        self.xlw.common_result_pass(row=9, column=1, result_key=self.event_action[1], path=self.__path)

    def event_applicant_report(self):
        self.xlw.input_data_verification(row=2, column=2, input_key='Applicant Advance Search')
        self.xlw.input_data_verification(row=3, column=2, input_key='Applicant Name Enter')
        self.xlw.input_data_verification(row=4, column=2, input_key='Search Button')
        self.xlw.input_data_verification(row=5, column=2, input_key='Select Applicant')
        self.xlw.input_data_verification(row=6, column=2, input_key='Change Status Action')
        self.xlw.input_data_verification(row=7, column=2, input_key='Stage Field')
        self.xlw.input_data_verification(row=8, column=2, input_key='Status Field')
        self.xlw.input_data_verification(row=9, column=2, input_key='Comment')
        self.xlw.input_data_verification(row=10, column=2, input_key='Change Button')
        self.xlw.input_data_verification(row=11, column=2, input_key='Applicant Name Click')
        self.xlw.input_data_verification(row=12, column=2, input_key='Applicant status Validate')

        self.xlw.common_result_pass(row=2, column=3, result_key=self.applicant[0], path=self.__path)
        self.xlw.common_result_pass(row=3, column=3, result_key=self.applicant[1], path=self.__path)
        self.xlw.common_result_pass(row=4, column=3, result_key=self.applicant[2], path=self.__path)
        self.xlw.common_result_pass(row=5, column=3, result_key=self.applicant[3], path=self.__path)
        self.xlw.common_result_pass(row=6, column=3, result_key=self.applicant[4], path=self.__path)
        self.xlw.common_result_pass(row=7, column=3, result_key=self.applicant[5], path=self.__path)
        self.xlw.common_result_pass(row=8, column=3, result_key=self.applicant[6], path=self.__path)
        self.xlw.common_result_pass(row=9, column=3, result_key=self.applicant[7], path=self.__path)
        self.xlw.common_result_pass(row=10, column=3, result_key=self.applicant[8], path=self.__path)
        self.xlw.common_result_pass(row=11, column=3, result_key=self.applicant[9], path=self.__path)
        self.xlw.common_result_pass(row=12, column=3, result_key=self.applicant[10], path=self.__path)

    def slot_action_report(self):
        self.xlw.input_data_verification(row=2, column=6, input_key='Event Actions')
        self.xlw.input_data_verification(row=3, column=6, input_key='Event Slot Action')

        self.xlw.common_result_pass(row=2, column=7, result_key=self.slot_action[0], path=self.__path)
        self.xlw.common_result_pass(row=3, column=7, result_key=self.slot_action[1], path=self.__path)

    def slot_config_report(self):
        self.xlw.input_data_verification(row=4, column=6, input_key='Click to select stage')
        self.xlw.input_data_verification(row=5, column=6, input_key='Entered Stage-Status')
        self.xlw.input_data_verification(row=6, column=6, input_key='Go Button')
        self.xlw.input_data_verification(row=7, column=6, input_key='Enter No.of Slots')
        self.xlw.input_data_verification(row=8, column=6, input_key='Go Button')

        self.xlw.common_result_pass(row=4, column=7, result_key=self.slot_config[0], path=self.__path)
        self.xlw.common_result_pass(row=5, column=7, result_key=self.slot_config[1], path=self.__path)
        self.xlw.common_result_pass(row=6, column=7, result_key=self.slot_config[2], path=self.__path)
        self.xlw.common_result_pass(row=7, column=7, result_key=self.slot_config[3], path=self.__path)
        self.xlw.common_result_pass(row=8, column=7, result_key=self.slot_config[4], path=self.__path)
