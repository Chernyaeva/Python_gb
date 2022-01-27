nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for joke in range(count):
        from random import randrange
        random_idx_noun = randrange(len(nouns))
        random_noun = nouns[random_idx_noun]

        random_idx_adverb = randrange(len(adverbs))
        random_adverb = adverbs[random_idx_adverb]

        random_idx_adjective = randrange(len(adjectives))
        random_adjective = adjectives[random_idx_adjective]

        joke = (f"{random_noun} {random_adverb} {random_adjective}")
        list_out.append(joke)



    return list_out


print(get_jokes(2))
print(get_jokes(10))

