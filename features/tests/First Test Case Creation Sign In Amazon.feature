# Created by Veronika at 2/15/2023
Feature: Sign In header visibility

  Scenario: User can see Sign In header
    Given Open amazon.com
    When User click Orders
    Then Verify Sign In page opened
    Then Verify Sign In header is visible
    Then Verify Email input field is present

