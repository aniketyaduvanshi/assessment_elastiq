import pytest
from pages import entries_page
from utilities.setup import setup_and_teardown


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Page:

    def test_url(self):
        pg = entries_page.Entries(self.driver)
        pg.url()
        pg.interaction()
        pg.entries()
