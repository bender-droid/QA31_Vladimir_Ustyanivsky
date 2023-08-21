import json
import random
import features.params.globals as gp
import webcolors
import os
import colorama
from features.params import random_value as rv

colorama.init(autoreset=True)


def date_doregister():
    date = """
        {
        "email": "email",
        "name": "name",
        "password": "password"
        }
        """
    body = json.loads(date)
    gp.EMAIL = f'{rv.RAND_NAME}@test.com'
    gp.NAME = f'{rv.RAND_NAME}'
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
    gp.NAME = f'test_{rv.RAND_NAME}'
    gp.CURRENT_SECTION = random.choice(gp.SECTION_LIST)
    gp.DESCRIPTION = f'{rv.RAND_NAME}'
    body['name'] = gp.NAME
    body['section'] = gp.CURRENT_SECTION
    body['description'] = gp.DESCRIPTION
    return body


def update_item(values=None):
    data = """
    {
    "id": "",
    "name": "",
    "section": "",
    "description": ""
    }"""
    request_body = json.loads(data)
    if values:
        request_body.update(values)
    request_body["id"] = int(gp.ID)
    gp.NAME = f'test_{rv.RAND_NAME}'
    gp.CURRENT_SECTION = random.choice(gp.SECTION_LIST)
    gp.DESCRIPTION = f'{rv.RAND_NAME}'
    request_body["name"] = gp.NAME
    request_body["section"] = gp.CURRENT_SECTION
    request_body["description"] = gp.DESCRIPTION
    gp.DICT = request_body
    return request_body



def http_methods(method):
    url = None
    match method:
        case 'CreateItem':
            url = f'{gp.URL}api/items/create/'
        case 'doRegister':
            url = f'{gp.URL}tasks/rest/doregister'
        case 'CreateCompany':
            url = f'{gp.URL}tasks/rest/createcompany'
        case 'UpdateItem':
            url = f'{gp.URL}api/items/update/'
        case 'UploadPhoto':
            url = f'{gp.URL}api/items/upload_photo/'
        case 'Search':
            url = f'{gp.URL}api/items/search/'
        case 'Delete':
            url = f'{gp.URL}api/items/delete/'
    return url


def get_values_from_table(table):
    parameters = {}
    for item in table:
        parameters.setdefault(f'{item[0]}', f'{item[1]}')
    gp.TABLE = parameters
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
            case 'RAND_NAME':
                dictionary[key] = rv.RAND_NAME
    return dictionary


def glob_params(param):
    match param:
        case 'EMAIL':
            param = gp.EMAIL
        case 'ID':
            param = gp.ID
        case 'TEST_EMAIL':
            param = gp.TEST_EMAIL
        case 'TEST_PASSWORD':
            param = gp.TEST_PASSWORD
        case 'RAND_NAME':
            param = rv.RAND_NAME
        case 'RAND_EMAIL':
            param = rv.RAND_EMAIL
    return param


def comparing_colors(color_css, color_word):
    color_word = webcolors.name_to_hex(color_word)
    print(color_word)
    print(color_css)


def form_request_body_for_upload():
    image_dir = 'features/files/images'
    random_file = random.choice(os.listdir(image_dir))
    file = os.path.join(image_dir, random_file)

    photo = {
        'photo': open(file, 'rb')
    }
    data = {
        'id': gp.ID
    }
    return photo, data


def show_message(response):
    if response.status_code == 200:
        print(colorama.Fore.GREEN + f'Method completed successfully')
        print(colorama.Fore.YELLOW + f'{response.json()}')
    else:
        raise ValueError(colorama.Fore.RED + f'Method crashed with {response.status_code} code')


def get_full_url(page):
    url = ''
    match page:
        case 'Регистрация':
            url = gp.URL + 'user/register/index'
        case 'Главная':
            url = gp.URL
        case 'Вход':
            url = gp.URL + 'user/login/index'
    return url

