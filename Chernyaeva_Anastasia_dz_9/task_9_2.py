class Road:
    def __init__(self, length: int, width: int):
        """конструктор класса
        :param length: длина в метрах
        :param width: ширина в метрах
        """
        # опишите конструктор в соответствии с заданием
        self._length: int = length
        self._width: int = width

    def calculate(self, hight: int = 5, mass_m_2: int = 25) -> int:
        """
        считает масу массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param hight: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: int значение тонн, дробная часть если есть НЕ учитывается
        """
        # Ваш код для рассчёта массы в тоннах
        self.hight = hight
        self.mass_m_2 = mass_m_2
        return int((self._length * self._width * self.hight * self.mass_m_2)/1000)

if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')
