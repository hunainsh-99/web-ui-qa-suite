import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    # In CI we set BASE_URL, locally fall back to file://
    if os.getenv("BASE_URL"):
        return os.getenv("BASE_URL")
    local = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return f"file://{local}"

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # pick up custom Chrome binary if set in CI
    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin:
        options.binary_location = chrome_bin
    driver = webdriver.Chrome(options=options)
    # optional: set a fixed window size so local and CI behave identically
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

