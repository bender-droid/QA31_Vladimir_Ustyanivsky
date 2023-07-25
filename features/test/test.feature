
Feature: Users Bugred

  Scenario: Click Lookup button
    Given Check method "doRegister":
      | key   | value |
      | email | EMAIL |
      | name  | NAME  |

    Then Enter site "users.bugred.ru"
    Then Search user with parameters:
      | key   | value |
      | email | EMAIL |
      | name  | NAME  |
