import json
import random, string

def date_doregister():
    date = """
        {
        "email": "email",
        "name": "name",
        "password": "password"
        }
        """
    body = json.loads(date)
    body['email'] = f'{randomword(8)}@test.com'
    body['name'] = f'{randomword(10)}'
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


