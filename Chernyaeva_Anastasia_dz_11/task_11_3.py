class OwnError(Exception):
    """Класс-исключение, проверяющий содержимое списка на наличие только чисел."""

    inp_list = []
    inp_data = 0

    while inp_data != 'stop':
        inp_data = input("Введите число или команду stop для завершения работы программы: ")
        if not inp_data == 'stop':
            try:
                inp_data = int(inp_data)
            except ValueError:
                print("Вы ввели не число")
            else:
                inp_list.append(inp_data)
        else:
            print(inp_list)
