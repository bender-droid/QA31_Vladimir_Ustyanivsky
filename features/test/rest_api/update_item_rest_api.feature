Feature: Shop Bugred

  Scenario Outline: Update item at shop.bugred.com

    Given Check method "CreateItem":
      | key    | value                                                                                                                                    |
      | color  | RED                                                                                                                                      |
      | size   | 20                                                                                                                                       |
      | price  | 200                                                                                                                                      |
      | params | Добро пожаловать! Подробности на сайте: https://yandex.ru/pogoda/maps/nowcast?lat=54.782634&lon=32.045288&le_Lightning=1 рады вас видеть |

    Then Enter item page with "ID"

    Then Check method "UpdateItem":
      | key    | value                          |
      | color  | BLUE                           |
      | size   | <size>                         |
      | price  | <price>                        |
      | params | Информация о товаре обновлена! |

    Then Enter item page with "ID"

    And Check updated info

    Examples:
      | size | price |
      | 20   | 2000  |
      | 30   | 3000  |
      | 40   | 4000  |
      | 50   | 50000 |