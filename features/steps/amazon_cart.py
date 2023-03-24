from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.ID, 'nav-cart-count')
CART_EMPTY = (By.CSS_SELECTOR,"div.a-row.sc-your-amazon-cart-is-empty h2")



@when('User clicks the cart icon')
def user_clicks_the_cart_icon(context):
    #context.driver.find_element(*CART_ICON).click()
    context.app.amazon_cart.click_cart_icon()


@then('Verify {expected_text} text present')
def verify_text(context, expected_text):
   #  text = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element (*CART_EMPTY).text
    # assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    context.app.amazon_cart.verify_text_inside_shopping_cart(expected_text)

#expected text or just text as in pages file?
#what should be uncommented here?