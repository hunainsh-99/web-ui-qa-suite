import os
import sys
import pytest
from selenium import webdriver

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, repo_root)

@pytest.fixture(scope="session")
def base():
    # CI will set BASE_URL; locally we assume you ran `python3 -m http.server 8000 &`
    if os.getenv("BASE_URL"):
        return os.getenv("BASE_URL").rstrip("/")
    return "http://127.0.0.1:8000"

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # if you set CHROME_BIN, point at your chromium/chrome binary
    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin:
        options.binary_location = chrome_bin
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()