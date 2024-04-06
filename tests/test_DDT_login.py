import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import Login
from utilities.readConfig import ReadConfig
from utilities.customLogger import Log
from utilities import XLutility

class Test_002_DDT_Login:

    baseUrl = ReadConfig.getBaseURL()
    path=".\\TestData\\LoginData.xlsx"
    log = Log.logGen()

    def test_ddt_login(self,setup):
        self.log.info("****************** Test_002_DDT_Login ********************")
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get(self.baseUrl)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.baseUrl))
        self.rows=XLutility.getRowCount(self.path,"Sheet1")
        print("Number of rows: ",self.rows)
        for r in range(2,self.rows+1):
            self.user = XLutility.readData(self.path,"Sheet1",r,1)
            self.password = XLutility.readData(self.path, "Sheet1", r, 2)
            self.status = XLutility.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            if self.status == "Pass":
                print("I am under the pass section")
                self.log.info("****** Test passed *****")
                self.lp.clickLogoutDropdown()
                self.lp.clickLogout()
                assert True
            else:
                self.log.info("****** Test Failed *****")
                assert False