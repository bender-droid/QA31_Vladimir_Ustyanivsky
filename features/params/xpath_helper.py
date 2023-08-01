"""Здесь содержатся xpath'ы"""


def xpath_parser(xpath):
    result = ''
    match xpath:
        case 'xpath_param_item':
            result = "//div/p[contains(text(), 'Парам')]"
    return result
