import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>[a-zA-Z0-9-_.]+)@(?P<domain>[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')
    result = RE_MAIL.match(email)
    if not result:
        raise ValueError(f'Wrong e-mail format for {email}')
    result_dict = result.groupdict()
    return result_dict


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
