import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
        print("Launching default browser.........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): 
    return request.config.getoption("--browser")



######Pytest HTML report######
def pytest_configure(config):
    config._metadata['Project name'] = 'E-commerce'
    config._metadata['Module name'] = 'Login'
    config._metadata['Tester'] = 'Ekanto'
    
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    
    