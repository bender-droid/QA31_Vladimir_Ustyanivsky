Feature: Shop Bugred

  Scenario: Create and delete item

    Given Check method "CreateItem":
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | Платья                   |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 20                       |
      | price       | 200                      |
      | params      | Random merchandise       |

    Then Get item info "ID"

    Then Delete item "ID"

    And Get item info "ID"