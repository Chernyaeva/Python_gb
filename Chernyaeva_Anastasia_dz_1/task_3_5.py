from random import randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count : int = 1, unique = False) -> list:
    """
    Возвращает список шуток в количестве count.
    Флаг uniqe делает так, что слова в шутках не повторяются.
    Если unique == True, то количество шуток ограничено минимальным количеством слов в списках nouns, adverbs и adjectives!
    """
    jokes_made = 0
    list_out = []   #здесь собранные шутки
    if unique:
        words_used_idx = [[],[],[]] #Создаём список для списков номеров слов уже использованных в шутках
        max_jokes = min(len(nouns),len(adverbs),len(adjectives),count)
    else:
        max_jokes = count
    while jokes_made < max_jokes:    #Создаём count шуток
        while True:     #генерируем случайное существительное
            random_noun_idx = randrange(len(nouns))
            if unique:  #проверяем использовалось ли оно уже, если требуется
                if random_noun_idx not in words_used_idx[0]:
                    words_used_idx[0].append(random_noun_idx)   #добавляем индекс в список использованных существительных
                    break
            else:
                break
        while True:     #генерируем случайное наречие
            random_adverb_idx = randrange(len(adverbs))
            if unique:  #проверяем использовалось ли оно уже, если требуется
                if random_adverb_idx not in words_used_idx[1]:
                    words_used_idx[1].append(random_adverb_idx) #добавляем индекс в список использованных наречий
                    break
            else:
                break
        while True:     #генерируем случайное прилагательное
            random_adjective_idx = randrange(len(adjectives))   #добавляем индекс в список использованных прилагательных
            if unique:  #проверяем использовалось ли оно уже, если требуется
                if random_adjective_idx not in words_used_idx[2]:
                    words_used_idx[2].append(random_adjective_idx)
                    break
            else:
                break
        list_out.append(f"{nouns[random_noun_idx]} {adverbs[random_adverb_idx]} {adjectives[random_adjective_idx]}")
        jokes_made += 1
    return list_out
print(get_jokes(3))
print(get_jokes()) #вызываем функцию, используя аргумент по умолчанию
print(get_jokes(unique=True, count=32)) #вызываем функцию, используя именованные аргументы