
def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    rem = number % 10
    if number in range(11, 20) or rem in range(5, 10) or rem == 0:
        return (f'{number} процентов')
    elif rem == 1:
        return (f'{number} процент')
    elif rem in range(2, 5):
        return (f'{number} процента')


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
    #test3