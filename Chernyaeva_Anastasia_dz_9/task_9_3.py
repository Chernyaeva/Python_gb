class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        # Ваш код здесь
        self.name: str = name
        self.surname: str = surname
        self.position: str = position
        self._income: dict = income


class Position(Worker):

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        # Ваш код здесь
        return f'{self.name} {self.surname}'.title()

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        sum = self._income['wage'] + self._income['bonus']
        return sum  # Ваш код здесь

if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())  # Иван Васильев 65000
    print(driver.get_full_name(), driver.get_total_income())  # Петр Николаев 37500
    print(scientist.get_full_name(), scientist.get_total_income())  # Геннадий Разумов 175000
