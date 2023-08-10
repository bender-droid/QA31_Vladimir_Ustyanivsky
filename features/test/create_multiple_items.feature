Feature: Shop Bugred

  Scenario: Create many items
    Given Create "2" of merchandise:
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | Платья                   |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 20                       |
      | price       | 200                      |
      | params      | Random merchandise       |
    Then Find all merchandise with "RAND_NAME" name