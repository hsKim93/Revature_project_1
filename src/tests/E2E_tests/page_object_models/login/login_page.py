from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_user_id(self):
        element: WebElement = self.driver.find_element(By.ID, "userId")
        return element

    def select_user_pw(self):
        element: WebElement = self.driver.find_element(By.ID, "userPw")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitBtn")
        return element

    def select_message(self):
        element: WebElement = self.driver.find_element(By.ID, "loginFailed")
        return element
