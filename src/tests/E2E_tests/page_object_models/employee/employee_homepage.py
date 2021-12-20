from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class EmployeeHomepage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element

    def select_past_button(self):
        element: WebElement = self.driver.find_element(By.ID, "past")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submit")
        return element
