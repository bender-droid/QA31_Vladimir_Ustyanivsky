import time
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


def open(context, *args):
    pass


@step('Я захожу на "{url}"')
def step_impl(context, url):
    context.driver.get('http://' + url)
    time.sleep(1)


@step('Нахожу поле c e-mail "{email}" и нажимаю кнопку "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f'//tr/td[contains(text(), "{email}")]/..//a[text()="{value}"]')
    element.click()
    time.sleep(5)
