from selenium.webdriver.common.by import By

class HomepagePage:
    URL = "http://127.0.0.1:8000/pages/homepage.html"
    HEADING = (By.TAG_NAME, "h1")

    def __init__(self, driver, base=None):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def heading_text(self):
        return self.driver.find_element(*self.HEADING).text
