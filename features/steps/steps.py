import time
from behave import step
# from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# import json
import help_file as hp
import features.params.globals as gp


# def open(context, *args):
#     pass


@step('Enter index page')
def step_impl(context):
    context.driver.get(gp.URL)
    time.sleep(1)


@step('Check method "{method}"')
def step_impl(context, method):
    table = hp.get_values_from_table(context.table)
    # body = hp.date_doregister()
    if method == 'CreateItem':
        body = hp.date_create_item(table)
    url = hp.http_methods(method)
    response = requests.post(url, body)
    print(response.json())
    gp.DICT = response.json()
    gp.ID = gp.DICT['result']['id']
    # assert response.status_code == 200


# @step('Search user with parameters')
# def step_impl(context):
#     values = hp.get_values_from_table(context.table)
#     print(values)
#     data = hp.parser_params(values)
#     print(data)
#     xpath = (f'//tr/td[contains(text(), "{data["email"]}")]/../td[contains(text(), "{data["name"]}")]'
#              f'/../td/a[contains(text(), "Посмотреть")]')
#     element = context.driver.find_element(By.XPATH, xpath)
#     element.click()
#     time.sleep(5)


@step('Enter item page with "{id}"')
def step_impl(context, id):
    item = hp.glob_params(id)
    full_url = f'{gp.URL}shop/item/{item}'
    context.driver.get(full_url)
    time.sleep(5)
    # print(values)
    # data = hp.glob_params_table(values)
    # print(data)
    # xpath = (f'//tr/td[contains(text(), "{data["email"]}")]/../td[contains(text(), "{data["name"]}")]'
    #          f'/../td/a[contains(text(), "Посмотреть")]')
    # element = context.driver.find_element(By.XPATH, xpath)
    # element.click()
    # time.sleep(5)