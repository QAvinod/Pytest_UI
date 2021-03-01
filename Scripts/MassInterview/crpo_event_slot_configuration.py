from Config import inputFile
from pageObjects.Pages.EventPages import EventActionsPage, EventSlotConfigurationPage
from utilities import excelRead


class SlotConfiguration:
    def __init__(self, driver, index):
        self.driver = driver
        self.slot = EventActionsPage.Actions(self.driver)
        self.slot_config = EventSlotConfigurationPage.EventSlot(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['event_slot_config'], index=index)
        xl = slot_excel.excel_dict
        self.xl_stage_status = xl['stage_status'][0]
        self.xl_number_of_slots = xl['number_of_slots'][0]

        self.event_slot_action_collection = []
        self.event_slot_collection = []

    def slot_action(self):
        __list = [self.slot.event_actions_click(),
                  self.slot.event_slot_configuration()
                  ]
        for func in __list:
            if func:
                self.event_slot_action_collection.append(func)
            else:
                self.event_slot_action_collection.append(func)

    def slot_configurations(self):
        __list = [self.slot_config.current_applicant_status_choose(),
                  self.slot_config.search_status_select(self.xl_stage_status),
                  self.slot_config.go_button(),
                  self.slot_config.slot_number(self.xl_number_of_slots),
                  self.slot_config.go_button()
                  ]
        for func in __list:
            if func:
                self.event_slot_collection.append(func)
            else:
                self.event_slot_collection.append(func)
