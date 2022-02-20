class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        qnt_numbers = self.cells // number
        one_cell = '*'
        cells_in_one_number = one_cell * number
        rem = self.cells % number
        if rem != 0:
            return (f'{cells_in_one_number}\n') * qnt_numbers + (f'{one_cell * rem}\n')
        else:
            return (f'{cells_in_one_number}\n') * qnt_numbers

    def check_if_cells(object_1, object_2):
        if type(object_1) != type(object_2):
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def __add__(self, other):
        self.check_if_cells(other)
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        self.check_if_cells(other)
        difference = self.cells - other.cells
        if difference <= 0:
            raise ValueError("недопустимая операция")
        return Cell(difference)

    def __mul__(self, other):
        self.check_if_cells(other)
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        self.check_if_cells(other)
        return Cell(int(self.cells / other.cells))

    def __floordiv__(self, other):
        return self.__truediv__(other)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
