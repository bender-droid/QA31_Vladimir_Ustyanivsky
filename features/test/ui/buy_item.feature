Feature: Shop Bugred

  Scenario: Buy random item

    Given Check method "CreateItem":
      | key         | value                    |
      | name        | RAND_NAME                |
      | section     | Платья                   |
      | description | Can't atomatize soap api |
      | color       | RED                      |
      | size        | 20                       |
      | price       | 200                      |
      | params      | Random merchandise       |

    Then Enter item page with "ID"

    Then Enter quantity "1" in area "Количество"

    Then Click "Добавить в корзину" button

    Then Press cart icon

    Then Fill in the "InputPhone" field "+79999999999"

    Then Fill in the "InputAddr" field "Smolensk, Fake street 123"

    Then Click "Оформить заказ" button

    Then Expect current url contains "finish"