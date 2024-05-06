
import pytest

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.conftest import setup_teardown

@pytest.mark.usefixtures("setup_teardown")
class TestSearch():

    def test_search_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("selenium")
        search_page = home_page.clicking_on_search_button()
        assert search_page.compare_search_result_with_valid_prod().__eq__('"selenium"')

    def test_search_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("abcd")
        search_page = home_page.clicking_on_search_button()
        assert search_page.compare_search_result_with_invalid_prod().__eq__("0 results")

