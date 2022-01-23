def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    list_out = []
    for num in list_in:
        split_list = num.split()
        name = split_list[-1].capitalize()
        list_out.append(f'Привет, {name}!')
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)