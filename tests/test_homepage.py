import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.homepage_page import HomepagePage

@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_homepage_heading(driver, base):
    page = HomepagePage(driver, base)
    page.load()
    assert page.heading_text() == "Welcome to Example Domain"
