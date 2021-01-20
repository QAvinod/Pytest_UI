import pytest
from selenium import webdriver
from utilities.ReadConfigFile import ReadConfig
from utilities.CustomLogger import LogGen
from pageObjects.Pages.Loginpage import LoginPage


class Test_001_Login:
    baseURL = ReadConfig.get_qa_url()
    logger = LogGen.logger()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "CRPO":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.tenant('accenturetest')
        self.lp.next_button()
        self.lp.user_name('admin')
        self.lp.password('Sqa@2021')
        self.lp.login_button()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
