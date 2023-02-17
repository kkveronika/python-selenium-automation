#Amazon logo - By CSS, using class
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

#Create account - By CSS, using tag and class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small' )

#Your name - By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Mobile number or email - By CSS, using multiple classes
driver.find_element(By.CSS_SELECTOR, '.a-input-text.a-span12.a-spacing-micro')

#Password - By CSS,using multiple attributes
driver.find_element(By.CSS_SELECTOR, "input[type='password'][placeholder='At least 6 characters']")

#Password must be at least 6 characters -


#Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#Continue- By CSS, using class+attribute
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input[type="submit"]')

#Conditions of use- I have a question here: I wanted to use partial match using asterisk*,
# I did and copied a part of the link, it showed me 5 results. Only the link and after the text is there.
# What is the way to search for that using partial match? It looks like I should use the whole link
# to narrow the search...
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref']")
# this way showed me 5 results.

#PrivacyNotice
#same question is for this one. It also has only has onl tag name, attribute and link as a value.
# I know that using id inside the link is not a good way because the numbers can be changed
# Lana, may you please help with these two sections. Спасибоо!!! :)

#Sign In - By CSS, using class and partial match
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="/ap/signin?openid.pape.max_auth_age=0&openid."]')



