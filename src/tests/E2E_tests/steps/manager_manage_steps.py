import time

from behave import Given, Then, When


# POM done
@Given(u'The manager is on manager home page or past page')
def get_manager_homepage(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)

@When(u'The manager is clicks pending page')
def click_pending_page(context):
    context.manager_homepage.select_pending_link().click()
    time.sleep(1)

@Then(u'The manager should be redirected to the manager pending page with the title Manager Pending Page')
def check_title(context):
    assert context.driver.title == "Manager Pending Page"

@Given(u'The manager is on manager pending page')
def get_manager_pending_page(context):
    context.driver.get("http://127.0.0.1:5500/client_src/login/index.html")
    context.login_page.select_user_id().send_keys("manager_test")
    context.login_page.select_user_pw().send_keys("123123")
    context.login_page.select_submit_button().click()
    time.sleep(1)
    context.manager_homepage.select_pending_link().click()
    time.sleep(1)

@When(u'The manager enters comment for approval')
def enter_comment(context):
    context.manager_pending_page.select_approve_comment_field().send_keys("test")

@When(u'The manager enters comment for rejection')
def enter_comment(context):
    context.manager_pending_page.select_reject_comment_field().send_keys("test")

@When(u'The manager clicks approve button')
def click_approve_button(context):
    context.manager_pending_page.select_approve_button().click()
    time.sleep(1)

@Then(u'The manager will see a message')
def check_message(context):
    assert context.manager_pending_page.select_message()

@When(u'The manager clicks reject button')
def click_reject_button(context):
    context.manager_pending_page.select_reject_button().click()
    time.sleep(1)
