import random
random_number = random.randint(0,101)
#print(random_number)
print("Я хочу сыграть с тобой в игру.")
trials_number = 0
while True:
    user_number = int(input("Какое число я загадала?."))
    if user_number == random_number:
        print('Я вся горю!')
        break
    else:
        trials_number += 1
        d = abs(user_number - random_number)
        if d < 5:
            print("Горячо!")
        elif d < 25:
            print("Тепло!")
        elif d <= 50:
            print("Прохладно!")
        elif d > 50:
            print("Холодно!")

    if trials_number == 10:
        print("Я совсем замёрзла!")
        break


