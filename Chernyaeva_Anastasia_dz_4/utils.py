import requests
import datetime


def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты code по отношению к рублю"""
    # ваша реализация здесь
    page = requests.get(
        'http://www.cbr.ru/scripts/XML_daily.asp').text
    start_date = page.find('Date="')
    date = (page[start_date + 6:start_date + 16])
    date_day = int(date[0:2])
    date_month = int(date[3:5])
    date_year = int(date[6:10])
    date = datetime.date(year=date_year, month=date_month, day=date_day)
    code = code.upper()
    start = page.find(code)
    if page[start + 5: start + 13] != "CharCode":
        result = ('None', date)
        return result
    end = page.find('</Valute>', start)
    str_value = page[start:end]
    start_1 = (str_value.find('<Value>'))
    end_1 = (str_value.find('</Value>'))
    str_value_digit = str_value[start_1 + 7:end_1]
    str_value_digit = str_value_digit.replace(',', '.')

    result_value = float(str_value_digit)  ## здесь должно оказаться результирующее значение float
    return result_value, date


# kurs, date_value = currency_rates_adv("USD")
#
# empty = bool(not kurs and not date_value)
# if not empty and not isinstance(kurs, float):
#     raise TypeError("Неверный тип данных у курса")
# if not empty and not isinstance(date_value, datetime.date):
#     raise TypeError("Неверный тип данных у даты")
