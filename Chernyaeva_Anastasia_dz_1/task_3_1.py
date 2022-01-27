def num_translate(value: str) -> str:
    """переводит числительное с английского на русский"""
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
    str_out = eng_rus_trans.get(value.lower())
    return str_out


print(num_translate("one"))
print(num_translate("Eight"))
print(num_translate("eleven"))