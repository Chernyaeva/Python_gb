class ComplexNumber:

    def __init__(self, real_part, imaginary_part=0):
        self.re = real_part
        self.im = imaginary_part

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)

    def __str__(self):
        if self.re < 0:
            return f'{self.re}{self.im}i'
        else:
            return f'{self.re}+{self.im}i'


a = ComplexNumber(1, 1)
print(a)
b = ComplexNumber(2, 2)
print(b)
print(a + b)
print(a * b)