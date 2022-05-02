"""
4. (МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]


"""
l_numbers = []

while True:
    answer = input('Введите количество элементов: ')
    if answer.isdigit(): break

items_num = int(answer)
#print('answer =', items_num)

for i in range(1, items_num + 1):
    while True:
        s_input = 'Введите ' + str(i) + ' элемент: '
        s_num = input(s_input)
        if s_num.isdigit(): break
    i_num = int(s_num)
    #print('i_num=', i_num)
    l_numbers.append(i_num)


#print(type(l_numbers), l_numbers)
l_numbers.sort()
print(l_numbers)
