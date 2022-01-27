def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        dict_out[name[0]] = list(filter(lambda el: el[0] == name[0], args))
    return dict_out


def thesaurus_adv(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        start_letter = name[name.find(' ')+1]
        dict_out[start_letter] = thesaurus(*list(filter(lambda el: el[el.find(' ')+1] == start_letter, args)))
    return dict_out

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))