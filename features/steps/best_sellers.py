from selenium.webdriver.common.by import By
from behave import given, when, then

BEST_SELLERS = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
BEST_SELLERS_LINKS = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")

@given('Open amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
@when('User navigate to Best Sellers')
def user_click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()

@then('Verify {expected_count} link related to Best Sellers section present')
def user_see_5_links(context, expected_count):
      best_seller_links = context.driver.find_elements(*BEST_SELLERS_LINKS)
      print(best_seller_links)
      print('link count: ', len(best_seller_links))
      assert len(best_seller_links) == int(expected_count), f'Expected {expected_count} links, but got {(len(best_seller_links))}'

