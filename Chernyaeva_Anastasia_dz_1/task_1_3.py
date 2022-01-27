
def thesaurus(*args) -> dict:
    dict_out = {}
    # пишите свою реализацию здесь
    for num in args:
        names = list(filter(lambda n: n[0]==num[0], args))
        dict_out.setdefault(num[0], names) # результирующий словарь значений
    return dict_out
print(thesaurus("Иван", "Мария", "Петр", "Илья"))