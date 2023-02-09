# Amazon logo - By Xpath
driver.find_element(By.XPATH, "//i[@role='img']")

#Continue button - By ID
driver.find_element(By.ID, 'continue')

#Need help link - By XPATH
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Create your Amazon account button - By ID
driver.find_element(By.ID, 'createAccountSubmit')

#*Conditions of use link - not sure if this way is correct..I think BY XPATH contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nodeId=508088']")

#*Privacy Notice link - same way is here - By XPATH contains because
# the link is too long but XPATh has to be short and accurate
driver.find_element(By.XPATH, "//a[contains(@href, 'nodeId=468496']")



