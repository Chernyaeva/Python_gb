import random
random_number = random.randint(0,101)
#print(random_number)
user_number = int(input("Я хочу сыграть с тобой в игру. Я загадала число. Попробуй угадать его."))
trials_number = []
while len(trials_number) < 10:
    if user_number == random_number:
        print('Я вся горю!')
    if (user_number > random_number):
        d = user_number - random_number
        if d < 5:
            print("Горячо!")
        elif d < 25:
            print("Тепло!")
        elif d < 50:
            print("Прохладно!")
        elif d > 50:
            print("Холодно!")
    if (user_number < random_number):
        d = random_number - user_number
        if d < 5:
            print("Горячо!")
        elif d < 25:
            print("Тепло!")
        elif d < 50:
            print("Прохладно!")
        elif d > 50:
            print("Холодно!")