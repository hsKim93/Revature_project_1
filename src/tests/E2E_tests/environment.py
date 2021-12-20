from behave.runner import Context
from selenium import webdriver

from src.tests.E2E_tests.page_object_models.employee.employee_homepage import EmployeeHomepage
from src.tests.E2E_tests.page_object_models.employee.employee_submit_page import EmployeeSubmitPage
from src.tests.E2E_tests.page_object_models.login.login_page import LoginPage
from src.tests.E2E_tests.page_object_models.manager.manager_homepage import ManagerHomepage
from src.tests.E2E_tests.page_object_models.manager.manager_past_page import ManagerPastPage
from src.tests.E2E_tests.page_object_models.manager.manager_pending_page import ManagerPendingPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.driver.set_window_size(1920, 1080)
    context.login_page = LoginPage(context.driver)
    context.employee_homepage = EmployeeHomepage(context.driver)
    context.employee_submit_page = EmployeeSubmitPage(context.driver)
    context.manager_homepage = ManagerHomepage(context.driver)
    context.manager_pending_page = ManagerPendingPage(context.driver)
    context.manager_past_page = ManagerPastPage(context.driver)


def after_tall(context: Context):
    context.driver.quit()
