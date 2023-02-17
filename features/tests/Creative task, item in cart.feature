# Created by Veronika at 2/16/2023
Feature: Amazon Cart functionality
  Scenario: Check if item was added into the cart
     Given Open amazon.com
     When User navigate to Search Amazon and enter teddy bear toy
     When User clicks enter
     When User selects WENMOTDY Teddy Bear Plush Toy Stuffed Animal
     When User navigates and clicks add to cart
     When User navigates to cart and clicks on cart
     Then Verify item WENMOTDY Teddy Bear Plush Toy Stuffed Animal is inside the Shopping Cart

I was trying to do my best but Nik said it is not correct way
to identify the item name because item can be removed from the page.
He said that we will talk about that on Saturday, if no- may
you please explain how to deal with specific item.
Thanks a lot!!! :)