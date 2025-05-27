from pages.homepage_page import HomepagePage

def test_homepage_heading(driver, base):
    page = HomepagePage(driver, base_url=base)
    page.load()
    assert page.heading_text() == "Welcome"
