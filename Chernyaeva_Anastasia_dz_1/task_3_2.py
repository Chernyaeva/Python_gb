def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский сохраняя регистр первой буквы"""
    value_lower = value.lower()
    eng_rus_trans = {'one':'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пыть',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девяить',
        'ten':'десять',
        'zero':'ноль'
    }
    str_out = eng_rus_trans.get(value_lower)
    if type(str_out) != 'None' and value[0].isupper():
        str_out = str_out.capitalize()
    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
print(num_translate_adv("eleven"))