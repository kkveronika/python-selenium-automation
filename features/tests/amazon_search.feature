# Created by Veronika at 3/22/2023
Feature: Amazon Search Dropdown

  Scenario: User search for an item in different amazon dept using dropdown
    Given Open Amazon page
    When Select department baby
    When Input text toy
    When Click on search button
    Then Verify baby department is selected