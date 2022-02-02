def get_uniq_numbers(src: list):
    uniq_set = set()
    for el in src:
        if el not in uniq_set:
            uniq_set.add(el)
        else:
            uniq_set.discard(el)
    return [el for el in src if el in uniq_set]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))