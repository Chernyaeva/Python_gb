from functools import wraps

def val_checker(cfunc):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if not cfunc(arg):
                    raise ValueError(f'Wrong value {arg}')
            return func(*args)
        return wrapper
    return _val_checker

@val_checker(lambda x: (type(x) is int or type(x) is float) and (x > 0))  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
