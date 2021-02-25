import time

from pytest import mark
from selenium.webdriver.common.by import By
import Scripts.Login.crpo_login_page
from utilities.ReadConfigFile import ReadConfig


# @mark.sanity
# def login_002_crpo(setup):
#     driver = setup
#     driver.find_element(By.XPATH, '//a[@ui-sref="crpo.events"]').click()
#     print('Event Tab')
