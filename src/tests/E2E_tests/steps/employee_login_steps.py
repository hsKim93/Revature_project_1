from behave import Given, When, Then
import time

# *********** Login ***********
@Given(u'The employee is on login page')
def get_login_page(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")


@When(u'The employee enters their credentials')
def type_employee_credentials(context):
    context.login_page.select_user_id().send_keys("employee_test")
    context.login_page.select_user_pw().send_keys("123123")


@When(u'The employee clicks submit login button')
def click_submit_button(context):
    context.login_page.select_submit_button().click()
    time.sleep(1)


@Then(u'The employee should be redirected to the employee homepage with the title Employee Homepage')
def check_employee_title(context):
    assert context.driver.title == "Employee Homepage"

# *********** Logout ***********
@Given(u'The employee is on employee homepage after logging in')
def get_employee_homepage(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("employee_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)


@When(u'The employee clicks logout')
def click_logout_button(context):
    context.employee_homepage.select_logout_button().click()
    time.sleep(1)


@Then(u'The employee should be redirected to the login page with the title Log in')
def check_login_title(context):
    assert context.driver.title == "Log in"
