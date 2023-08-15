import time
from behave import step
from selenium.webdriver.common.by import By
import requests
import help_file_rest as hp
import features.params.globals as gp
import features.params.xpath_helper as xh
import re
import json
from selenium import webdriver





@step('Enter index page')
def step_impl(context):
    context.driver.get(gp.URL)
    time.sleep(1)


@step('Check method "{method}"')
def step_impl(context, method):
    url = hp.http_methods(method)
    response = None
    match method:
        case 'CreateItem':
            table = hp.get_values_from_table(context.table)
            body = hp.date_create_item(table)
            response = requests.post(url, body)
            gp.DICT = response.json()
            gp.ID = gp.DICT['result']['id']
        case 'UpdateItem':
            new_item_info = hp.get_values_from_table(context.table)
            body = hp.update_item(new_item_info)
            print(body)
            response = requests.post(url, body)
        case 'doRegister':
            # body = hp.date_doregister()
            # assert response.status_code == 200
            pass
        case 'UploadPhoto':
            photo, data = hp.form_request_body_for_upload()
            response = requests.post(url, data=data, files=photo)
    print(response.json())
    hp.show_message(response)



@step('Enter item page with "{item_id}"')
def step_impl(context, item_id):
    item = hp.glob_params(item_id)
    full_url = f'{gp.URL}shop/item/{item}'
    context.driver.get(full_url)
    print(f'Item ID: {gp.ID}')
    time.sleep(5)
    # print(values)
    # data = hp.glob_params_table(values)
    # print(data)
    # xpath = (f'//tr/td[contains(text(), "{data["email"]}")]/../td[contains(text(), "{data["name"]}")]'
    #          f'/../td/a[contains(text(), "Посмотреть")]')
    # element = context.driver.find_element(By.XPATH, xpath)
    # element.click()
    # time.sleep(5)


@step('Find url in merch parameters')
def step_impl(context):
    xpath = xh.xpath_parser('xpath_param_item')
    text = context.driver.find_element(By.XPATH, xpath).text
    link = re.search('http\S+', text)
    if link:
        print(f'В параметрах найдена ссылка: {link[0]}')
        context.driver.get(link[0])
    else:
        raise ValueError('Ссылка не найдена!')
    # print(link)


@step('Check updated info')
def step_impl(context):
    item_name = context.driver.find_element(By.XPATH, xh.xpath_parser('item_name')).text
    item_section = context.driver.find_element(By.XPATH, xh.xpath_parser('item_section')).text
    item_size = context.driver.find_element(By.XPATH, xh.xpath_parser('item_size')).text
    item_size = re.search('[0-9]{2}', item_size)
    item_price = context.driver.find_element(By.XPATH, xh.xpath_parser('item_price')).text
    item_price = re.search('[0-9]*', item_price)
    item_color = context.driver.find_element(By.XPATH, xh.xpath_parser('item_color'))
    color = item_color.get_dom_attribute('style')
    color = color.split(':')[1]
    hp.comparing_colors(color, gp.TABLE['color'])
    match item_name:
        case gp.NAME:
            print('Item name updated successfully!')
    match item_section:
        case gp.CURRENT_SECTION:
            print('Item section updated successfully!')
    if item_size[0] == gp.DICT.get("size"):
        print('Item size updated successfully!')
    if item_price[0] == gp.DICT.get("price"):
        print('Item price updated successfully!')
    print(gp.DICT.get("params"))


@step('Get item info "{item_id}"')
def step_impl(context, item_id):
    body = {
        'id': f'{hp.glob_params(item_id)}'
    }
    url = f'{gp.URL}api/items/get/'
    response = requests.post(url, body)
    print(response.json())


@step('Create item with "{api}"')
def step_impl(context, api):
    match api:
        case "REST":
            url = hp.http_methods('CreateItem')
            table = hp.get_values_from_table(context.table)
            body = hp.date_create_item(table)
            response = requests.post(url, body)
            gp.RESPONSE = response.json()
            gp.ID = gp.DICT["result"]["id"]
        case "SOAP":
            pass


@step('Create "{quantity}" of merchandise')
def step_impl(context, quantity):
    gp.TABLE = hp.get_values_from_table(context.table)
    item = hp.glob_params_table(gp.TABLE)
    gp.NAME = item["name"]
    body = json.dumps(item)
    url = hp.http_methods("CreateItem")
    for _ in range(int(quantity)):
        response = requests.post(url, body)
        gp.RESPONSES.append(response.json()['result'])
        hp.show_message(response)


@step('Find merchandise with "{name}" name')
def step_impl(context, name):
    url = hp.http_methods('Search')
    if name == 'RAND_NAME':
        name = gp.NAME
    body = {
        'query': name
    }
    response = requests.post(url, body)
    print(response.json()['result'])


@step('Delete item "{item_id}"')
def step_impl(context, item_id):
    url = hp.http_methods('Delete')
    if item_id == 'ID':
        item_id = gp.ID
    body = {
        "id": hp.glob_params(item_id)
    }
    response = requests.post(url, body)
    hp.show_message(response)


@step('Go to "{page_name}" page')
def step_impl(context, page_name):
    context.driver.get(gp.URL)
    registration_link = context.driver.find_element(
        By.XPATH, f"//li[contains(@class, 'nav-item')]/a[contains(text(), '{page_name}')]"
    )
    registration_link.click()
    time.sleep(2)


@step('Fill in the "{field_name}" field "{value}"')
def step_impl(context, field_name, value):
    pass
