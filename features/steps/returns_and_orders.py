from selenium.webdriver.common.by import By
from behave import given, when, then

RETURNS_AND_ORDERS = (By.ID, 'nav-orders')
SING_IN_TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('User click Returns and Orders')
def click_returns_and_orders(context):
    #context.driver.find_element(*RETURNS_AND_ORDERS).click()
    context.app.header.returns_and_orders()


@then('Verify Sign In page is opened and {expected_text} is shown')
def verify_sign_in_page(context, expected_text):
    # actual_result = context.driver.find_element(*SING_IN_TEXT).text
    # assert expected_text == actual_result, f'Expected {expected_text} but got actual {actual_result}'
    # context.app.sign_in_page.verify_sign_in_page(expected_text)
    context.app.sign_in_page.verify_sing_in_page_is_opened(expected_text)