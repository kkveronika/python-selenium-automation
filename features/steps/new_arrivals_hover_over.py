from selenium.webdriver.common.by import By
from behave import given, when, then

@given ('Open product link')
def open_product_link(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')


@when ('User hovers over NewArrivals')
def hover_over_new_arrivals(context):
    context.app.header.hover_over_options()

@then ('Verify deals for women shown')
def verify_women_deals_shown(context):
    context.app.header.verify_women_deals_shown()