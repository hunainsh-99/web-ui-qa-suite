import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("user, pwd, expected", [
    ("",      "",        "both fields required"),
    ("admin", "",        "both fields required"),
    ("",      "secret",  "both fields required"),
    ("foo",   "bar",     "invalid credentials"),
    ("admin", "wrong",   "invalid credentials"),
    ("admin", "secret",  "welcome, admin"),
])
def test_login_messages(driver, base, user, pwd, expected):
    page = LoginPage(driver, base_url=base)
    page.load()
    page.submit(user, pwd)
    assert page.message_text() == expected