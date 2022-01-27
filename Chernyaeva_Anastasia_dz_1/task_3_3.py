def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        dict_out[name[0]] = list(filter(lambda el: el[0] == name[0], args))
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))