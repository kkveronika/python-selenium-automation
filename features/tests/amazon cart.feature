# Created by Veronika at 2/15/2023
Feature: Amazon Cart Functionality
  Scenario: User can verify that Amazon Cart is empty
    Given Open Amazon page
    When User clicks the cart icon
    Then Verify Your Amazon Cart is empty text present

