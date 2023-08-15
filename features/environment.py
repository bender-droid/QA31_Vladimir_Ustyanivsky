from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    print('Test begun')


def after_feature(context, feature):
    context.driver.quit()
    print('Test finished')
