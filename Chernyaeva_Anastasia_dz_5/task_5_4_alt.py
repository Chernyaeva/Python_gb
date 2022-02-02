def get_numbers(src: list):
    pass
    sorted = [i2 for i1, i2 in zip(src, src[1:]) if i2 > i1]
    return sorted

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))