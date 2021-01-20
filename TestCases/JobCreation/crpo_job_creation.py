# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class CRPO:
#     driver = ''
#
#     def setup(self):
#         self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         self.driver.maximize_window()
#         print("Launching chrome browser.........")
#
#     def login_method(self):
#         self.driver.find_element(By.NAME, 'alias').send_keys('accenturetest')
#         self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()
#         time.sleep(2)
#         self.driver.find_element(By.NAME, 'loginName').send_keys('admin')
#         self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('Sqa@2021')
#         self.driver.find_element(By.CSS_SELECTOR, '.button_style.login').click()
#         time.sleep(2)
#
#     def tear_down(self):
#         self.driver.quit()