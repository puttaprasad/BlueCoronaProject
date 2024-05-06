import pytest
from selenium import webdriver

from utilities import Read_configuration_file


@pytest.fixture()
def setup_teardown(request):
    browser = Read_configuration_file.read_configuration_file("basic info", "browser").lower()
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid brownser form this list chrome/firefox/edge")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.myinstamojo.com/")
    request.cls.driver = driver
    yield
    driver.quit()