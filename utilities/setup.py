import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    ser = webdriver.ChromeService(executable_path=".\\assets\\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt, service=ser)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()
