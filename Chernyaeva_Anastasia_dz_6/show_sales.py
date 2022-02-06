import sys

# get starting row number
if len(sys.argv) < 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 1:
    start_row = 1
else:
    start_row = int(sys.argv[1])
# get ending row number
if len(sys.argv) < 3 or not sys.argv[2].isdigit() or int(sys.argv[2]) < start_row:
    end_row = -1  # -1 indicates read untill the end of file
else:
    end_row = int(sys.argv[2])

with open('bakery.csv', 'r', encoding='utf-8') as file:
    line = file.readline()
    act_row = 1
    while line and (act_row <= end_row or end_row == -1):
        if act_row >= start_row:
            print(line.strip())
        line = file.readline()
        act_row += 1
