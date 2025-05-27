from selenium.webdriver.common.by import By

class LoginPage:
    URL = "{base_url}/pages/login.html"
    USER = (By.ID, "user")
    PASS = (By.ID, "pass")
    SUBMIT = (By.CSS_SELECTOR, "#login-form button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.get(self.URL.format(base_url=self.base_url))

    def submit(self, username, password):
        elem_user = self.driver.find_element(*self.USER)
        elem_user.clear()
        elem_user.send_keys(username)
        elem_pass = self.driver.find_element(*self.PASS)
        elem_pass.clear()
        elem_pass.send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def message_text(self):
        return self.driver.find_element(*self.MESSAGE).text
