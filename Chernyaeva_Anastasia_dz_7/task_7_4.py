import os


def get_nearest_ten(value):
    if value == 0:
        return 0
    divider = 1
    while True:
        res = value // divider
        if not res:
            return divider
        divider *= 10

root_dir = 'C:\Windows\System32'
files_dict = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_name = os.path.join(root, file)
        tenned_file_size = get_nearest_ten(os.stat(file_name).st_size)
        if tenned_file_size not in files_dict:
            files_dict[tenned_file_size] = 1
        else:
            files_dict[tenned_file_size] += 1

print(f'File size statistics for {root_dir} :')
print(*sorted(files_dict.items()), sep='\n')
