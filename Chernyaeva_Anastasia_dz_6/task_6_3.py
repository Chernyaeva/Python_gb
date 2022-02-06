import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    dataset = {}
    with open(path_users_file, 'r', encoding='utf-8') as users_file:
        users = users_file.readlines()
        with open(path_hobby_file, 'r', encoding='utf-8') as hobbys_file:
            hobbys = hobbys_file.readlines()
            if len(hobbys) > len(users):
                sys.exit(1)
            for i in range(len(users)):
                if i < len(hobbys):
                    dataset[users[i].strip()] = hobbys[i].strip().split(',')
                else:
                    dataset[users[i].strip()] = None
    return  dataset


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
