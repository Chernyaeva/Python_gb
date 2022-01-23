# 2

def convert_list_in_str(list_in: list) -> str:
    list_out = []
    for num in list_in:
        if num.isdigit():
            list_out.append(f'"{int(num):02d}"')
        elif (num[0] == '+' or num[0] == '-') and num[1:].isdigit():
            if int(num) < 0:
                list_out.append(f'"-{int(num[1:]):02d}"')
            if int(num) > 0:
                list_out.append(f'"+{int(num[1:]):02d}"')
        else:
            list_out.append(num)
    return (' ').join(list_out)

# 3
def convert_list_in_str_2(list_in: list) -> str:
    for i, num in enumerate(list_in):
        if num.isdigit():
            list_in[i] = f'"{int(num):02d}"'
        elif (num[0] == '+' or num[0] == '-') and num[1:].isdigit():
            if int(num) < 0:
                list_in[i] = f'"-{int(num[1:]):02d}"'
            if int(num) > 0:
                list_in[i] = f'"+{int(num[1:]):02d}"'
    return (' ').join(list_in)


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
result2 = convert_list_in_str_2(my_list)
print(result)
print(result2)