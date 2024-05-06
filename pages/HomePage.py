from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

    search_box_field_xpath = "//input[@id='searchInput']"
    search_button_xpath = "//button[@class='rounded-md h-38 bg-theme px-22 text-navbar-searchBg border border-l-none rounded rounded-l-none border-theme']"


    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_field_xpath).click()
        self.driver.find_element(By.XPATH, self.search_box_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_box_field_xpath).send_keys(product_name)

    def clicking_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)
