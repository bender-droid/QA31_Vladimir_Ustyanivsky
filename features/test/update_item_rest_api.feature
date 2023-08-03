Feature: Shop Bugred

  Scenario: Update item at shop.bugred.com
    Given Check method "CreateItem":
      | key    | value                                                                                                                                    |
      | color  | RED                                                                                                                                      |
      | size   | 20                                                                                                                                       |
      | price  | 200                                                                                                                                      |
      | params | Добро пожаловать! Подробности на сайте: https://yandex.ru/pogoda/maps/nowcast?lat=54.782634&lon=32.045288&le_Lightning=1 рады вас видеть |

    Then Enter item page with "ID"
    Then Check how "UpdateItem" works:
      | key    | value                          |
      | color  | BLUE                           |
      | size   | 40                             |
      | price  | 99999                          |
      | params | Информация о товаре обновлена! |
    Then Enter item page with "ID"
    Then Check updated info