
Feature: Shop Bugred

  Scenario: Upload item photo
    Then Check method "CreateItem":
      | key    | value                                                                                                                                    |
      | color  | RED                                                                                                                                      |
      | size   | 20                                                                                                                                       |
      | price  | 200                                                                                                                                      |
      | params | Random merchandise |


    Then Enter item page with "ID"
    Then Check method "UploadPhoto"
    And Enter item page with "ID"