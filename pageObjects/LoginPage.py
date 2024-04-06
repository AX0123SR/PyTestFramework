from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    text_username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    text_password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login_button = "//button[@type='submit']"
    logout_drop_down = "//p[@class='oxd-userdropdown-name']"
    logout_button = "//a[text()='Logout']"


    def __init__(self,driver):
        self.driver =driver


    def setUsername(self,username):
        self.driver.find_element(By.XPATH, self.text_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button)

    def clickLogoutDropdown(self):
        self.driver.find_element(By.XPATH, self.logout_drop_down)

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button)

