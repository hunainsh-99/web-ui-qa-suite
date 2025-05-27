from selenium.webdriver.common.by import By

class HomepagePage:
    URL = "{base_url}/pages/homepage.html"
    HEADING = (By.TAG_NAME, "h1")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url.rstrip('/')

    def load(self):
        self.driver.get(self.URL.format(base_url=self.base_url))

    def heading_text(self):
        return self.driver.find_element(*self.HEADING).text
