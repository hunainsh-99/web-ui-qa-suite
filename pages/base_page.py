import os

class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        base = base_url or os.getenv("BASE_URL", "http://127.0.0.1:8000")
        self.base_url = base.rstrip('/')
