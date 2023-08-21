Feature: Shop Bugred

  Scenario: Register new user

    Given Enter "Регистрация" page

    Then Fill in the "exampleInputName" field "RAND_NAME"

    Then Fill in the "exampleInputEmail1" field "RAND_EMAIL"

    Then Fill in the "exampleInputPassword1" field "12345"

    Then Fill in the "exampleInputPassword2" field "12345"

    Then Click "Зарегистрироваться" button

    Then Expect to see "Теперь вы можете войти используя свой email и пароль!" message in window
