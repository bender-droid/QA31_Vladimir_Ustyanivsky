import json
import random
import string
import features.params.globals as gp


def date_doregister():
    date = """
        {
        "email": "email",
        "name": "name",
        "password": "password"
        }
        """
    body = json.loads(date)
    gp.EMAIL = f'{randomword(8)}@test.com'
    gp.NAME = f'{randomword(10)}'
    body['email'] = gp.EMAIL
    body['name'] = gp.NAME
    body['password'] = '123123'
    return body


def date_create_item(values=None):
    date = """
    {
    "name": "",
    "section": "",
    "description": ""
    }"""
    body = json.loads(date)
    if values:
        body.update(values)
    gp.NAME = f'test_{randomword(5)}'
    gp.SECTION = random.choice(gp.SECTION)
    gp.DESCRIPTION = f'{randomword(25)}'
    body['name'] = gp.NAME
    body['section'] = gp.SECTION
    body['description'] = gp.DESCRIPTION
    return body


def update_item(values=None):
    data = """
    {
    "id" = "",
    "name": "",
    "section": "",
    "description": ""
    }"""
    request_body = json.loads(data)
    if values:
        request_body.update(values)
    request_body["id"] = gp.ID
    request_body["name"] = f'test_{randomword(5)}'
    request_body["section"] = random.choice(gp.SECTION)
    request_body["description"] = f'{randomword(25)}'
    return request_body


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def http_methods(method):
    url = None
    match method:
        case 'CreateItem':
            url = 'http://shop.bugred.ru/api/items/create/'
        case 'doRegister':
            url = 'http://users.bugred.ru/tasks/rest/doregister'
        case 'CreateCompany':
            url = 'http://users.bugred.ru/tasks/rest/createcompany'
        case 'UpdateItem':
            url = 'http://shop.bugred.ru/api/items/update/'
    return url


def get_values_from_table(table):
    parameters = {}
    for item in table:
        parameters.setdefault(f'{item[0]}', f'{item[1]}')
    return parameters


def glob_params_table(dictionary):
    for key, value in dictionary.items():
        match value:
            case 'EMAIL':
                dictionary[key] = gp.EMAIL
            case 'NAME':
                dictionary[key] = gp.NAME
            case 'ID':
                dictionary[key] = gp.ID
    return dictionary


def glob_params(param):
    if param == 'EMAIL':
        param = gp.EMAIL
    elif param == 'ID':
        param = gp.ID
    return param
