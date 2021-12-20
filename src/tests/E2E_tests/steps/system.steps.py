from behave import Given, Then, When
import time

@Given(u'The system is on login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")


@When(u'The system enters incorrect credentials')
def step_impl(context):
    context.login_page.select_user_id().send_keys("b_test")
    context.login_page.select_user_pw().send_keys("444")


@When(u'The system presses enter')
def step_impl(context):
    context.login_page.select_submit_button().click()
    time.sleep(1)


@Then(u'The system should see a message with the id=loginFailed')
def step_impl(context):
    assert context.login_page.select_message()


@Given(u'The system is on submit page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("b_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)
    context.employee_homepage.select_submit_button().click()
    time.sleep(1)


@When(u'The system enters negative amount and other fields')
def step_impl(context):
    context.employee_submit_page.select_reason_input().send_keys("System test for behave")
    context.employee_submit_page.select_amount_input().send_keys("-0.01")


@When(u'The system clicks submit')
def step_impl(context):
    context.employee_submit_page.select_submit_button().click()
    time.sleep(1)


@Then(u'The system should see a message with the id=fail')
def step_impl(context):
    assert context.employee_submit_page.select_fail_message()


@When(u'The system enters non-numeric amount and other fields')
def step_impl(context):
    context.employee_submit_page.select_reason_input().send_keys("System test for behave")
    context.employee_submit_page.select_amount_input().send_keys("hello there")
