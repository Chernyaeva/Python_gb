from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line_list = line.split(' ')
    return (line_list[0], line_list[5][1:], line_list[6])


list_out = list()
clients_dict = {}
spamer = ['', 0]
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    line = fr.readline()
    while line:
        # parse a line from the log file
        line_parsed = get_parse_attrs(line)
        list_out.append(line_parsed)
        client_addr = line_parsed[0]
        # Check if client address is already in dictionary
        if client_addr in clients_dict:
            clients_dict[client_addr] += 1  # increment number of times clent sent a reqest
            if clients_dict[client_addr] > spamer[1]:  # check if this client is a spamer
                spamer[0] = client_addr
                spamer[1] = clients_dict[client_addr]
        else:
            clients_dict[line_parsed[0]] = 1  # Add clent address to the dictionary
        # read next line from the file
        line = fr.readline()

pprint(list_out)
print(f'Client {spamer[0]} is a spamer! It made {spamer[1]} requests')
