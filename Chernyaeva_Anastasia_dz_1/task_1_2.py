dataset = list(range(1, 1000, 2))
for i in range(len(dataset)):
    dataset[i] = dataset[i]**3

for num in dataset:
    copy_num = num
    sum = 0
    num_saved = num
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
        if sum % 7 == 0:
            sum_1 = 0
            sum_1 = sum_1 + num

print (sum_1)