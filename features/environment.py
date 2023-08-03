from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    print('Test begun')


def after_feature(context, feature):
    context.driver.quit()
    print('Test finished')
