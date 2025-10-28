from pages.login_page import LoginPage

def test_login_page_open(driver):
    page = LoginPage(driver)
    page.open("https://example.com/login")  # change this to your target site
    assert "login" in driver.current_url
