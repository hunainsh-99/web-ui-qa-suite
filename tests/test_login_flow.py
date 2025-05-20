import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

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

@pytest.mark.parametrize("user, pwd, expected", [
    ("",    "",        "both fields required"),  # both empty
    ("admin","",       "both fields required"),  # empty password
    ("",    "secret",  "both fields required"),  # empty username
    ("foo", "bar",     "invalid credentials"),   # wrong creds
    ("admin","wrong",  "invalid credentials"),   # wrong password
    ("admin","secret", "welcome, admin"),        # correct creds
])
def test_login_messages(driver, base, user, pwd, expected):
    page = LoginPage(driver, base)
    page.load()
    page.submit(user, pwd)
    assert page.message_text() == expected
