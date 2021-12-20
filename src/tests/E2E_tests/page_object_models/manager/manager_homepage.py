from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ManagerHomepage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_pending_link(self):
        element: WebElement = self.driver.find_element(By.ID, "pending")
        return element

    def select_past_link(self):
        element: WebElement = self.driver.find_element(By.ID, "past")
        return element

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element
