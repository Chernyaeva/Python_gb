
from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pass  # Ваша реализация здесь
    my_tuple = (line[: line.find(' ')], line[line.find(' "') + 2:line.find(' /')], line[line.find('downloads') :line.find(' H')])
    return my_tuple# верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    line = fr.readline()
    while line:
        list_out.append(get_parse_attrs (fr.readline()))
        line = fr.readline()
    pass  # передавайте данные в функцию и наполняйте список list_out кортежами


pprint(list_out)
