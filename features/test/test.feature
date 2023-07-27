
Feature: Shop Bugred

  Scenario: Shop bugred.com
    Then Check method "CreateItem":
      | key    | value       |
      | color  | RED         |
      | size   | 20          |
      | price  | 200         |
      | params | test_testov |


    Then Enter item page with "ID"
    Then Find merchandise "name"