from selenium.webdriver.common.by import By

class LoginPage:
    URL = "http://127.0.0.1:8000/pages/login.html"
    USER = (By.ID, "user")
    PASS = (By.ID, "pass")
    SUBMIT = (By.CSS_SELECTOR, "#login-form button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver, base):
        self.driver = driver
        self.base = base

    def load(self):
        self.driver.get(self.URL.format(base=self.base))

    def submit(self, username, password):
        self.driver.find_element(*self.USER).clear()
        self.driver.find_element(*self.USER).send_keys(username)
        self.driver.find_element(*self.PASS).clear()
        self.driver.find_element(*self.PASS).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def message_text(self):
        return self.driver.find_element(*self.MESSAGE).text
