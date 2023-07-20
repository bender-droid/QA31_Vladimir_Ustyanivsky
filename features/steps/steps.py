import time
from behave import step
# from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# import json
import help_file as HP


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
    assert response.status_code == 200


@step('Find area with email "{email}" and click button "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f'//tr/td[contains(text(), "{email}")]/..//a[text()="{value}"]')
    element.click()
    time.sleep(5)