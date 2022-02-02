def get_numbers(src: list):
    pass
    sorted = [src[i] for i in range(1, len(src), 1) if src[i] > src[i - 1]]

    return sorted


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 60]
print(*get_numbers(src))


