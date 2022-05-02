"""
6. (МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""

def input_list_number():
    answer = input('Enter multiple numbers separated by comma, semicolon or slash: ')
    #print(answer)
    if ',' in answer:
        l_strings = answer.split(',')
    elif ';' in answer:
        l_strings = answer.split(';')
    elif '/' in answer:
        l_strings = answer.split('/')

    #print(l_strings)
    l_digits = []
    for s in l_strings:
        l_digits.append(int(s))

    #print(l_digits)
    return l_digits

l_1 = input_list_number()
print(l_1)
l_2 = input_list_number()
print(l_2)

l_new=[]
for item in l_1:
    if l_2.count(item) == 0: l_new.append(item)

print(l_new)