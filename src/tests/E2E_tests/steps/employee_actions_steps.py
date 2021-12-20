import time
from behave import given, when, then


@given(u'The employee is on employee homepage')
def get_employee_homepage(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("employee_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)


@when(u'The employee clicks submit page')
def click_submit_page(context):
    context.employee_homepage.select_submit_button().click()
    time.sleep(1)


@when(u'The employee enters information')
def step_impl(context):
    context.employee_submit_page.select_reason_input().send_keys("This reimbursement was created from a behave test")
    context.employee_submit_page.select_amount_input().send_keys("0.01")


@when(u'The employee clicks submit reimbursement button')
def step_impl(context):
    context.employee_submit_page.select_submit_button().click()
    time.sleep(1)


@then(u'The employee should get a message with id=success')
def step_impl(context):
    assert context.employee_submit_page.select_success_message()


@when(u'The employee clicks past homepage')
def step_impl(context):
    context.employee_homepage.select_past_button().click()
    time.sleep(1)


@then(u'The employee should be redirected to the employee past page with the title Employee Past Page')
def step_impl(context):
    title = context.driver.title
    assert title == "Employee Past Page"
