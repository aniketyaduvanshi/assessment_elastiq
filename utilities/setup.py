import pytest
from selenium import webdriver
from library import constants


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    ser = webdriver.ChromeService(executable_path=constants.EXECUTABLE_PATH)
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt, service=ser)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()
