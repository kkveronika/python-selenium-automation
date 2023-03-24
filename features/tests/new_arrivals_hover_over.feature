# Created by Veronika at 3/22/2023
Feature: NewArrivals Hover Over
  Scenario: User opens the product, hovers over New Arrivals and sees the deals
    Given Open product link
    When User hovers over NewArrivals
    Then Verify deals for women shown