import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base():
    # Use BASE_URL in CI, otherwise file:// fallback
    if os.getenv("BASE_URL"):
        return os.getenv("BASE_URL")
    here = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return f"file://{here}"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Point to Chrome binary if provided
    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin:
        options.binary_location = chrome_bin
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
