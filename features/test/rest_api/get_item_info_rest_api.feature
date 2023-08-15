Feature: Shop Bugred

  Scenario: Get item information
    Then Check method "CreateItem":
      | key    | value              |
      | color  | RED                |
      | size   | 20                 |
      | price  | 200                |
      | params | Random merchandise |


    Then Get item info "ID"
