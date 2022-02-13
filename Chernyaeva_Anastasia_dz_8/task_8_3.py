from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_list = []
        kwarg_list = []
        for arg in args:
            value_arg = str(arg)
            value_type_arg = type(arg)
            value_united_arg = f'{value_arg}: {value_type_arg}'
            arg_list.append(value_united_arg)
        for key, value in kwargs.items():
            value_kwarg = str(value)
            value_type_kwarg = type(value)
            value_united_kwarg = f'{key} - {value_kwarg}: {value_type_kwarg}'
            kwarg_list.append(value_united_kwarg)
        list_common = arg_list + kwarg_list
        result = func(*args, **kwargs)
        result_str = str(result)
        result_type = type(result)
        print(f'{result_str}: {result_type} = {func.__name__}({list_common}')

        return result
    return wrapper


@decorator
def calc_power(*args, **kwargs):
    mult = 1
    mult_kwargs = 1
    for arg in args:
        mult = mult * arg
    for key, value in kwargs.items():
        mult_kwargs = mult_kwargs * value
    mult_common = mult * mult_kwargs




    return mult_common

calc_power(8, 6, b = 9, a = 8)
