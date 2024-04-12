import pytest

from pageObjects.LoginPage import Login
from utilities.readConfig import ReadConfig
from utilities.customLogger import Log
import time
class Test_001_Login:
    baseUrl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Log.logGen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.log.info("****************** Test_001_Login ********************")
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        actual_title = "OrangeHRM"
        if actual_title == self.driver.title:
            assert True
            print(self.driver.title)
            self.log.info("***************** Title Matched *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.log.info("******************** Title not Matched ************************")
            assert False
