from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name ul li")
CURRENT_COLOR = (By.CSS_SELECTOR, '.selection')

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    # context.driver.find_element(*COLOR_OPTIONS).click()   # click on 1
    context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS)).click()


    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage','Dark Indigo/Rinsed', 'Dark Khaki Brown','Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash', 'Washed Black', 'Washed Grey']

    # actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        assert current_color in expected_colors, f'The current color {current_color} is not inside the list of color'
        # actual_colors.append(current_color)

    # assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'