import time
from utilities.menu import Menu
from pageObjects import Locators
from utilities.uiNotifier import Notifier
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class JobCreationPage:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS VARIABLES TO EASY ACCESS ------>>>>
    """
    e_job_names = Locators.JOB['job_name']
    e_anchor_tag = Locators.TAG['anchor']
    e_file_path = Locators.ATTACHMENT['file']
    e_description = Locators.JOB['description']
    e_location = Locators.PLACEHOLDER['text_ph'].format('Location')
    e_hm = Locators.PLACEHOLDER['text_ph'].format('Hiring Manager')
    e_bu = Locators.PLACEHOLDER['text_ph'].format('Business Unit')
    e_openings = Locators.JOB['openings']
    e_male = Locators.PLACEHOLDER['num_ph'].format('Male')
    e_female = Locators.PLACEHOLDER['num_ph'].format('Female')
    create_job_button_name = 'New Job Role'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.notifier = Notifier(self.driver)

    def job_tab(self, tab_name):
        self.tab.menu_collection(tab_name)
        self.wait.loading()

    def create_button(self):
        assert self.wait.web_elements_wait_click(By.TAG_NAME,
                                                 self.e_anchor_tag,
                                                 self.create_job_button_name) == self.create_job_button_name
        print('***--------->>> Clicked on job created button')
        self.wait.loading()

    def job_name(self, name):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_job_names, name)

    def job_attachment(self, file_path):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_file_path, file_path)
        time.sleep(0.5)
        self.wait.uploading()

    def file_upload_notifier(self):
        self.notifier.glowing_messages('File uploaded successfully')
        self.notifier.dismiss_message()

    def job_description(self, description):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_description, description)
        self.wait.drop_down_selection()

    def job_location(self, location):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_location, location)
        self.wait.drop_down_selection()

    def job_hiring_manager(self, hm):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_hm, hm)
        self.wait.drop_down_selection()

    def job_business_unit(self, bu):
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_bu, bu)
        self.wait.drop_down_selection()

    def job_openings(self, openings):
        self.wait.clear(By.NAME, self.e_openings)
        self.wait.web_element_wait_send_keys(By.NAME, self.e_openings, openings)

    def job_male_diversity(self, male_diversity):
        self.wait.clear(By.XPATH, self.e_male)
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_male, male_diversity)

    def job_female_diversity(self, female_diversity):
        self.wait.clear(By.XPATH, self.e_female)
        self.wait.web_element_wait_send_keys(By.XPATH, self.e_female, female_diversity)
