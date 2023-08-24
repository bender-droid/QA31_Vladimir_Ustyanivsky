Feature: Shop Bugred

  Scenario: Checking item filter

    Given Create "1" of merchandise:
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | ＼(〇_ｏ)／                  |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 20                       |
      | price       | 200                      |
      | params      | Random merchandise       |

    Then Create "1" of merchandise:
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | ＼(〇_ｏ)／                  |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 30                       |
      | price       | 200                      |
      | params      | Random merchandise       |

    Then Go to "＼(〇_ｏ)／" page

    Then Press "RED" checkbox

    Then Expect to see "2" merchandises on page

    Then Delete items "RESPONSES"