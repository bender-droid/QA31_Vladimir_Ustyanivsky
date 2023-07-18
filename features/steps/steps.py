import time
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


def open(context, *args):
    pass


@step('Enter site "{url}"')
def step_impl(context, url):
    context.driver.get('http://' + url)
    time.sleep(3)


@step('Find area with email "{email}" and click button "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f'//tr/td[contains(text(), "{email}")]/..//a[text()="{value}"]')
    element.click()
    time.sleep(5)
