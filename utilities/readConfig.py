import configparser
import os
from pathlib import Path
config = configparser.RawConfigParser()

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common_data", "baseUrl")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common_data", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common_data", "password")
        return password
