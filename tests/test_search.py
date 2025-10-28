from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    # Setup Chrome options
    chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI (needed for CI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--user-data-dir=/tmp/unique_user_data_dir")

    # Setup Chrome driver using Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Google
    driver.get("https://www.google.com")

    # Perform search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("DevOps automation")
    search_box.submit()

    # ✅ Wait for title to contain 'DevOps'
    WebDriverWait(driver, 10).until(EC.title_contains("DevOps"))

    # ✅ Now assert
    assert "DevOps" in driver.title

    # Close browser
    driver.quit()


