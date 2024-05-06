class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def type(self,text,locator):