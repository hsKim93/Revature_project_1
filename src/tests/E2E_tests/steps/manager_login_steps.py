import time
from behave import Given, When, Then

@Given(u'The manager is on login page')
def get_login_page(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")


@When(u'The manager enters their credentials')
def step_impl(context):
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")


@When(u'The manager clicks submit login button')
def step_impl(context):
    context.login_page.select_submit_button().click()
    time.sleep(1)


@Then(u'The manager should be redirected to the manager homepage with the title Manager Homepage')
def step_impl(context):
    assert context.driver.title == "Manager Homepage"


@Given(u'The manager is on manager homepage after logging in')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)


@When(u'The manager clicks logout')
def step_impl(context):
    context.manager_homepage.select_logout_button().click()
    time.sleep(1)


@Then(u'The manager should be redirected to the login page with the title Log in')
def step_impl(context):
    assert context.driver.title == "Log in"
