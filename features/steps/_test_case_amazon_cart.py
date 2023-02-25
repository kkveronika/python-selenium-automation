from selenium.webdriver.common.by import By
from behave import given, when, then

#@given('Open amazon.com')
#def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')

@when('User clicks the cart icon')
def user_clicks_the_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()

@then('Verify that Your Amazon cart is empty')
def verify_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element (By.CSS_SELECTOR,"div.a-row.sc-your-amazon-cart-is-empty h2").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


