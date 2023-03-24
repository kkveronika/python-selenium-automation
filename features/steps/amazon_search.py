from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
@when ('Select department baby')
def select_dept_baby(context):
    context.app.header.select_department_baby()

@when ('Input text {text}')
def input_search_text(context, text):
    #context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_text(text)
@when ('Click on search button')
def click_search_button(context):
    context.app.header.click_search()

@then ('Verify baby department is selected')
def verify_baby_dept_selected(context):
    context.app.search_results_page.verify_selected_department()