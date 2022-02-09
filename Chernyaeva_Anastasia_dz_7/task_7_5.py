import os
import json


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
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        if tenned_file_size not in files_dict:
            files_dict[tenned_file_size] = (1, [ext])
        else:
            _temp_file_num, _temp_list = files_dict[tenned_file_size]
            if ext not in _temp_list:
                _temp_list.append(ext)
            files_dict[tenned_file_size] = _temp_file_num + 1, _temp_list

file_name = root_dir.rsplit('\\', maxsplit=1)[-1] + '_summary.json'
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(files_dict, file)

# print(f'File size statistics for {root_dir} :')
# print(*sorted(files_dict.items()), sep='\n')
