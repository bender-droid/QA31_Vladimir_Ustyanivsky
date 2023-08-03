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
    return result
