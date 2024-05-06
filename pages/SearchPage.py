from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    search_result_for_valid_prod_xpath = '//div[@class="container mx-auto h-full flex items-center text-14" and @font-customisation="section-heading" and @color-customisation="page-heading"]/div/span[@class="italic"]'
    search_result_for_invalid_prod_xpath = "//div[contains(text(), '0 results')]"

    def compare_search_result_with_valid_prod(self):
        element = self.driver.find_element(By.XPATH, self.search_result_for_valid_prod_xpath)
        actual_result = element.text
        return actual_result

    def compare_search_result_with_invalid_prod(self):
        element = self.driver.find_element(By.XPATH, self.search_result_for_invalid_prod_xpath)
        actual_result = element.text
        return actual_result