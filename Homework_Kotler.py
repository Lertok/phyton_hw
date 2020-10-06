# 1
a = 2
b = 3
print(a + b)

name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = int(input('Введите свой возраст: '))
print(name, surname, age)

# 2 Время в секундах - необходимо чч.мм.сс
time_user = int(input('Введите время в секундах: '))
time_in_min = (time_user // 60) % 60
time_in_hour = (time_user // 60) // 60
time_in_sec = time_user % 60
print(f'Время {time_in_hour}:{time_in_min}:{time_in_sec}')

# 3 узнать у пользователя число
number = input('Введите число: ')
x = int(number)
y = int(number + number)
z = int(number + number + number)
print(x + y + z)

# 4 Найти самую большую цифру в водимом числе
number_1 = list(input('Введите целое положительное число: '))
number_max = max(number_1)
print(number_max)


# 5 Выручка и прибыль
proceed = float(input('Введите сумму выручки вашей фирмы: '))
costs = float(input('Введите сумму издержек вашей фирмы: '))
if proceed > costs:
    profitability = float((proceed - costs) / proceed)
    num_of_people = float(input('Введите численность вашей фирмы: '))
    print('Поздравляем Ваша фирма прибыльна!!!')
    print('Рентабильность Вашей фирмы: ', profitability)
    print('Прибыль на одного сотрудника составляет: ', (proceed - costs) / num_of_people)
elif proceed == costs:
    print('Вы работаете в "НОЛЬ"!!!')
else:
    print('К сожалению Ваша фирма убыточна!')

# 6 Задачька про спортсмена
day = 2
day_win = 3
number_day = 1
while day < day_win:
    day *= 1.1
    number_day += 1
    if day >= day_win:
        print('На', number_day, 'день спортсмен пробежит больше 3 км')
