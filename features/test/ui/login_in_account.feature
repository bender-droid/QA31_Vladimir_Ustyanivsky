Feature: Shop Bugred

  Scenario: Registration and login into account

    Given Go to "Вход" page

    Then Fill in the "exampleInputEmail1" field "TEST_EMAIL"

    Then Fill in the "exampleInputPassword1" field "TEST_PASSWORD"

    Then Click "Войти" button
#
#    Then Expect to see "Теперь вы можете войти используя свой email и пароль!" message in window