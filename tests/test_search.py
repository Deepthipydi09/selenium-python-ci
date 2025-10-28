from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without UI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-data-dir=/tmp/unique_user_data_dir")

    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Google and search
    driver.get("https://www.google.com")
    assert "Google" in driver.title

    # Close browser
    driver.quit()



