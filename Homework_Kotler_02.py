# 1 Создать список и заполнить его элементами различных типов данных.

something_list = [2, 'three', 3.5, (4, 5, 'six'), None]
for el in something_list:
    print(type(el))

# 2
# Нечетное
something_list01 = [2, 'three', 3.5, (4, 5, 'six'), None]
j = 0
for i in range(int(len(something_list01) / 2)):
    something_list01[j], something_list01[j + 1] = something_list01[j + 1], something_list01[j]
    j += 2
print(something_list01)

# Пустое
something_list02 = []
j1 = 0
for i1 in range(int(len(something_list02) / 2)):
    something_list02[j1], something_list02[j1 + 1] = something_list02[j1 + 1], something_list02[j1]
    j1 += 2
print(something_list02)

# 1 элемент
something_list03 = [1]
j2 = 0
for i2 in range(int(len(something_list03) / 2)):
    something_list03[j2], something_list03[j2 + 1] = something_list03[j2 + 1], something_list03[j2]
    j2 += 2
print(something_list03)

# Четное
something_list04 = [2, 'three', 3.5, (4, 5, 'six')]
j3 = 0
for i3 in range(int(len(something_list04) / 2)):
    something_list04[j3], something_list04[j3 + 1] = something_list04[j3 + 1], something_list04[j3]
    j3 += 2
print(something_list04)

# 3 Пользователь вводит месяц в виде целого числа от 1 до 12
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = {'Зима': winter,
           'Весна': spring,
           'Лето': summer,
           'Осень': autumn}

month = int(input('Введите месяц в числовом формате от 1 до 12: '))
for key in seasons.keys():
    if month in seasons[key]:
        print('Это: ', key)

# 4 Пользователь вводит строку из нескольких слов, разделённых пробелами
strings = (input('Введите словосочетание: '))
results = strings.split()
for q, result in enumerate(results, 1):
    print(q, result[:10])

# 5 Реализовать структуру «Рейтинг»
numbers = [10, 8, 7, 5, 4, 3, 3, 2, 1]
new_number = int(input('Введите элемент рейтинга в виде числа: '))
numbers.append(new_number)
numbers.sort()
numbers.reverse()
print(numbers)

# 6 Реализовать структуру данных «Товары»
# database = []
# database_01 = ()
# all_database = []
# inquiry = ()
# while inquiry != '':
#     inquiry = input('Введите наименование продукции, его цену, количество и ед. изм., если Вам больше ничего не нужно нажмити ENTER: ')
#     if inquiry != '':
#         inquiry_01 = inquiry.split()
#         database.append(inquiry_01)
#     database = {'название': database[0][0], 'цена': database[0][1], 'количество': database[0][2], 'ед изм': database[0][3]}
#     all_database.append(database)
# else:
#     print(all_database)
#
# print(all_database)
#
