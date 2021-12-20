from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class EmployeeSubmitPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "reasonInput")
        return element

    def select_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "amountInput")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitBtn")
        return element

    def select_success_message(self):
        element: WebElement = self.driver.find_element(By.ID, "success")
        return element

    def select_fail_message(self):
        element: WebElement = self.driver.find_element(By.ID, "fail")
        return element
