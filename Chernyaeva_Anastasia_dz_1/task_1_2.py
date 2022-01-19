# a
def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    sum_1 = 0
    for num in dataset:
        sum = 0
        num_saved = num
        while (num != 0):
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_1 = sum_1 + num_saved

    return sum_1  # Верните значение полученной суммы


# b
def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    for i in range(len(dataset)):
        dataset[i] += 17
    return sum_list_1(dataset)  # Верните значение полученной суммы

# c
def sum_list_3(dataset: list) -> int:
    sum_1 = 0
    for num in dataset:
        num += 17
        sum = 0
        num_saved = num
        while (num != 0):
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_1 = sum_1 + num_saved

    return sum_1

# Соберите нужный список по заданию
my_list = list(range(1, 1000, 2))
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 3

result_1 = sum_list_1(my_list) # a
print(result_1)

result_3 = sum_list_3(my_list) # c
print(result_3)

result_2 = sum_list_2(my_list) # b
print(result_2)

