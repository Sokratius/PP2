"""Для правильной работы программы ввод через консоль обязательно должен содержать пробелы между числами, а иначе программа вернет ошибку"""


def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list = input().split()
input_list = [int(item) for item in input_list]
print(unique_elements(input_list))