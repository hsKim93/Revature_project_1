from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ManagerPendingPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reject_comment_field(self):
        element: WebElement = self.driver.find_element(By.ID, "9998t")
        return element

    def select_approve_comment_field(self):
        element: WebElement = self.driver.find_element(By.ID, "9999t")
        return element

    def select_approve_button(self):
        element: WebElement = self.driver.find_element(By.ID, "9999a")
        return element

    def select_reject_button(self):
        element: WebElement = self.driver.find_element(By.ID, "9998r")
        return element

    def select_message(self):
        element: WebElement = self.driver.find_element(By.ID, "success")
        return element
