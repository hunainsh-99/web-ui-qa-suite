from selenium.webdriver.common.by import By

class LoginPage:
    URL     = "{base_url}/pages/login.html"
    USER    = (By.ID, "user")
    PASS    = (By.ID, "pass")
    SUBMIT  = (By.CSS_SELECTOR, "#login-form button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.get(self.URL.format(base_url=self.base_url))

    def submit(self, username, password):
        el = self.driver.find_element
        el(*self.USER).clear()
        el(*self.USER).send_keys(username)
        el(*self.PASS).clear()
        el(*self.PASS).send_keys(password)
        el(*self.SUBMIT).click()

    def message_text(self):
        return self.driver.find_element(*self.MESSAGE).text

