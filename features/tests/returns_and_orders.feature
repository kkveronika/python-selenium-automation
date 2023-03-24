# Created by Veronika at 2/15/2023
Feature: Returns and Orders - Sign In


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When User click Returns and Orders
    Then Verify Sign In page is opened and Sign in is shown




#Scenario: User can see Sign In header
    #Given Open amazon.com
    #When User click Returns and Orders
    #Then Verify Sign In page opened
    #Then Verify Sign In header is visible
    #Then Verify Email input field is present
