from selenium.webdriver.common.by import By
from behave import given, when, then

@when('User navigate to Search Amazon and enter Teddy bear toy')
def search_for_teddy_bear_toy(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('teddy_bear_toy')
@when('User clicks enter')
def click_enter(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
@when('User selects WENMOTDY Teddy Bear Plush Toy Stuffed Animal')
def select_wenmotdy_teddy_bear(context):
    context.driver.find_element(By.CSS_SELECTOR, "//a[contains(span, 'WENMOTDY Teddy Bear Plush Toy Stuffed Animal')]").click()
@when('User navigates and clicks add to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
@when('User navigates to cart and clicks on cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()
@then('Verify item WENMOTDY Teddy Bear Plush Toy Stuffed Animal is inside the Shopping Cart')
def verify_item_in_cart(context):
    expected_result = 'WENMOTDY Teddy Bear Plush Toy Stuffed Animal Giant Teddy Bear with Footprints Big Bear for Girlfriend Kids Baby Shower Christmas Day 39 inch Tan'
    actual_result =   context.driver.find_element(By.CSS_SELECTOR, "//a[contains(span, 'WENMOTDY Teddy Bear Plush Toy Stuffed Animal')]").text()
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
