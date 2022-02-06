import sys

if len(sys.argv) < 3:
    print('Please enter sale number and value.')
    exit(1)
if not sys.argv[1].isdigit():
    print('Sale number must be digit.')
    exit(1)

set_row = int(sys.argv[1].strip())
with open('bakery.csv', 'r+', encoding='utf-8') as file:
    act_row = 1
    while act_row < set_row:
        line = file.readline()
        if not line:
            break
        act_row += 1
    if not line:  # chcek if end of file was reached
        print('Number of sales is less than entered!')
        exit(1)
    else:

        # print(f'Set row = {set_row}, act_row = {act_row}, cursor position = {file.tell()}')    #debug
        file.seek(file.tell())  # crazy hack
        file.write(f'{sys.argv[2].strip()}\n')
