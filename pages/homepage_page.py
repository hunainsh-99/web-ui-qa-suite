from selenium.webdriver.common.by import By

class HomepagePage:
    URL = "file://{base}/pages/homepage.html"
    HEADING = (By.TAG_NAME, "h1")

    def __init__(self, driver, base):
        self.driver = driver
        self.base = base

    def load(self):
        self.driver.get(self.URL.format(base=self.base))

    def heading_text(self):
        return self.driver.find_element(*self.HEADING).text
