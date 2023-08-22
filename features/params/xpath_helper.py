"""Здесь содержатся xpath'ы"""


def xpath_parser(xpath):
    result = ''
    match xpath:
        case 'xpath_param_item':
            result = "//div/p[contains(text(), 'Парам')]"
        case 'item_name':
            result = "//h2"
        case 'item_section':
            result = "//li[@class='breadcrumb-item'][2]/a"
        case "item_size":
            result = "//p[2]"
        case 'item_price':
            result = "//span[@class='label label-primary']"
        case 'item_color':
            result = "//div//span[@class='label']"
        case 'button':
            result = "//button[contains(text(), '%s')]"
        case 'message_in_window':
            result = "//section[@id='alertify']//p[contains(text(), '%s')]"
        case 'dropdown_button':
            result = "//div[contains(@class, 'dropdown-menu')]/a[contains(text(), '%s')]"
        case 'items_amount':
            result = "//div/label[contains(text(), '%s')]/../input"
        case 'cart':
            result = "//div[contains(@class, 'float')]/a[contains(@class, 'nav')]"
        case 'search':
            result = "//form[contains(@class, 'form-inline')]/input"
        case 'search_button':
            result = "//form[contains(@class, 'form-inline')]/button"
        case 'item_row':
            result = "//div[contains(@class, 'row')]/div[contains(@class, 'col-md-4')]/a"
    return result
