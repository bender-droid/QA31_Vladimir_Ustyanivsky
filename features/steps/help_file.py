import json
import random, string
import features.params.globals as GP

def date_doregister():
    date = """
        {
        "email": "email",
        "name": "name",
        "password": "password"
        }
        """
    body = json.loads(date)
    GP.EMAIL = f'{randomword(8)}@test.com'
    GP.NAME = f'{randomword(10)}'
    body['email'] = GP.EMAIL
    body['name'] = GP.NAME
    body['password'] = '123123'
    return body


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def http_methods(method):
    url = None

    match method:
        case 'doRegister':
            url = 'http://users.bugred.ru/tasks/rest/doregister'
        case 'CreateCompany':
            url = 'http://users.bugred.ru/tasks/rest/createcompany'
    return url


def get_values_from_table(table):
    parameters = {}
    for item in table:
        parameters.setdefault(f'{item[0]}', f'{item[1]}')
    return parameters


def parser_params(dictionary):
    for key, value in dictionary.items():
        if value == 'EMAIL':
            dictionary[key] = GP.EMAIL
        elif value == 'NAME':
            dictionary[key] = GP.NAME

    return dictionary