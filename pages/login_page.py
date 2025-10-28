from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USER = (By.ID, "username")
    PASS = (By.ID, "password")
    SUBMIT = (By.ID, "loginBtn")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.type(self.USER, username)
        self.type(self.PASS, password)
        self.click(self.SUBMIT)
