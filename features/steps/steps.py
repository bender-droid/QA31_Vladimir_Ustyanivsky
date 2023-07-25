import time
from behave import step
# from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# import json
import help_file as HP
import features.params.globals as GP



def open(context, *args):
    pass


@step('Enter site "{url}"')
def step_impl(context, url):
    context.driver.get('http://' + url)
    time.sleep(1)


@step('Check method "{method}"')
def step_impl(context, method):

    url = HP.http_methods(method)
    body = HP.date_doregister()

    response = requests.post(url, body)
    print(response.json())
    assert response.status_code == 200


@step('Search user with parameters')
def step_impl(context):
    values = HP.get_values_from_table(context.table)
    print(values)
    data = HP.parser_params(values)
    print(data)
    xpath = f'//tr/td[contains(text(), "{data["email"]}")]/../td[contains(text(), "{data["name"]}")]/../td/a[contains(text(), "Посмотреть")]'
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(5)