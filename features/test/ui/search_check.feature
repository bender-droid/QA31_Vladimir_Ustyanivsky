Feature: Shop Bugred

  Scenario: Search UI check

    Given Check method "CreateItem":
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | Платья                   |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 20                       |
      | price       | 200                      |
      | params      | Random merchandise       |

    Then Go to "Главная" page

    Then Searching for merchandise "NAME"

    Then Expect to see "1" merchandises on page