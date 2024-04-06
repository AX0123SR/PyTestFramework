import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common data", "baseUrl")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common data", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password
