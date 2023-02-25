# Created by Veronika at 2/24/2023
Feature: Amazon Best Sellers link count
  Scenario: User open Best Sellers page and observe 5 links are displayed
    Given Open amazon.com
    When User navigate to Best Sellers
    Then Verify 5 link related to Best Sellers section present