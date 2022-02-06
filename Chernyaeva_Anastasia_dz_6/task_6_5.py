import sys


def match_hobbys(path_users_file: str, path_hobby_file: str, path_output_file: str):
    """
    Считывает данные из файлов CSV файлов и сопоставляет строки в них
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :param path_output_file: путь до файла, куда будет сохранены прользрватели с хобби
    """
    with open(path_users_file, 'r', encoding='utf-8') as users_file:
        with open(path_hobby_file, 'r', encoding='utf-8') as hobbys_file:
            with open(path_output_file, 'w', encoding='utf-8') as output_file:
                user = users_file.readline()
                while user:
                    hobby = hobbys_file.readline()
                    if hobby:
                        hobby = hobby.strip()
                    output_file.write(f'{user.strip()}: {hobby}\n')
                    user = users_file.readline()


match_hobbys(sys.argv[1], sys.argv[2], sys.argv[3])
