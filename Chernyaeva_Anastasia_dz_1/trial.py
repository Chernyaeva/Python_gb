def convert_list_in_str(list_in: list):
    for i, element in enumerate(list_in):
        s = str(element)
        if element.isdigit():
            if int(element) < 10:
                list_in[i] = list_in[i].replace(element, ('0' + element))
            list_in[i] = '"' + list_in[i] + '"'
            continue
        if s[0] == '+' or s[0] == '-':
            print(6)
        if element.isalpha():
            continue
        else:
            if int(''.join(i for i in element if i.isdigit())) > 10:
                list_in[i] = '"' + list_in[i] + '"'
                continue
            for sym in element:
                if sym.isdigit() and int(element) < 10:
                    list_in[i] = '"' + list_in[i].replace(sym, ('0' +sym)) + '"'
    return(' '.join(list_in))

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)

print(result)