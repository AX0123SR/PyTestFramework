from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
     print("Launching Chrome browser.........")
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser.........")
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

# This will receive the value using command line
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the browser value to the setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_configure(config):
#     # Define custom metadata
#     metadata = {
#         'Project name': "OrangeHRM",
#         'Module': "Testing Site",
#         'Tester': "Ayush Srivastava"
#     }
#     # Add metadata to the pytest configuration
#     config.metadata = metadata
