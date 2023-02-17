# Created by Veronika at 2/15/2023
Feature: Amazon Cart Functionality
  Scenario: User can verify that Amazon Cart is empty
    Given Open amazon.com
    When User clicks the cart icon
    Then Verify that Your Amazon cart is empty
