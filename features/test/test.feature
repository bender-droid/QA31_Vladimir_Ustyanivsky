
Feature: Shop Bugred

  Scenario: Shop bugred.com
    Then Check method "CreateItem":
      | key    | value                                                                                                                                    |
      | color  | RED                                                                                                                                      |
      | size   | 20                                                                                                                                       |
      | price  | 200                                                                                                                                      |
      | params | Добро пожаловать! Подробности на сайте: https://yandex.ru/pogoda/maps/nowcast?lat=54.782634&lon=32.045288&le_Lightning=1 рады вас видеть |


    Then Enter item page with "ID"
    Then Find url in merch parameters