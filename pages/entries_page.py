from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import constants
from locators import ElementLocators


class Entries:
    def __init__(self, driver):
        self.driver = driver

    def url(self):
        self.driver.get(constants.URL)
        self.driver.find_element("xpath", ElementLocators.page_confirmation).is_displayed()
        print(constants.URL_NEVIGATION_MSG)

    def interaction(self):
        wait = WebDriverWait(driver=self.driver, timeout=constants.EXPLICIT_WAIT)
        textbox = wait.until(expected_conditions.visibility_of(self.driver.find_element("xpath", ElementLocators.search_box)))
        print(constants.SEARCHBOX_LOCATED_MSG)
        textbox.send_keys(constants.SEARCH_ITEM)

    def entries(self):
        entries = self.driver.find_element("xpath", ElementLocators.entries_result).text
        assert entries == constants.ENTRY_ASSERT, f"{constants.ASSERT_UNSUCCESSFUL}"
        print(constants.ASSERT_SECCESSFUL)
