import time
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json


def open(context, *args):
    pass


@step('Enter site "{url}"')
def step_impl(context, url):
    context.driver.get('http://' + url)
    time.sleep(1)


@step('Find area with email "{email}" and click button "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f'//tr/td[contains(text(), "{email}")]/..//a[text()="{value}"]')
    element.click()
    time.sleep(5)


@step('Register new user with "{email}" email, "{name}" name, "{password}" password')
def step_impl(context, email, name, password):
    date = """
    {
    "email": "email",
    "name": "name",
    "password": "password"
    }
    """
    body = json.loads(date)
    body['email'] = email
    body['name'] = name
    body['password'] = password

    response = requests.post('http://users.bugred.ru/tasks/rest/doregister', body)
    assert response.status_code == 200

