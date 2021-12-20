from behave import Given, Then, When
import time

@Given(u'The manager is on manager homepage or pending page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)

@When(u'The manager clicks past page')
def step_impl(context):
    context.manager_homepage.select_past_link().click()
    time.sleep(1)


@Then(u'The manager should be redirected to the past page with the title Manager Past Page')
def step_impl(context):
    assert context.driver.title == "Manager Past Page"


@Given(u'The manager is on manager past page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)
    context.manager_homepage.select_past_link().click()
    time.sleep(1)

@When(u'The manager clicks home')
def step_impl(context):
    context.manager_past_page.select_home_link().click()
    time.sleep(1)


@Then(u'The manager should be redirected to the homepage with the title Manager Homepage')
def step_impl(context):
    assert context.driver.title == "Manager Homepage"
