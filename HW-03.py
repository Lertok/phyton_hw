# 1 Реализовать функцию, принимающую два числа
def division():
    try:
        dividend = float(input('Введите делимое: '))
        divider = float(input('Введите делитель: '))
        div = dividend / divider
    except ZeroDivisionError:
        print('Делить на ноль нельзя!!!')
        return division()
    return div


print(division())


# 2 Реализовать функцию, принимающую несколько параметров
def bio(name, sername, birthday, city, email, phone):
    print(
        f'Имя - {name}, Фамилия - {sername}, год рождения - {birthday}, город проживания - {city}, email - {email}, телефон - {phone}')


sername = input('Введите свою фамилию: ')
name = input('Введите свое имя: ')
birthday = input('Введите свой год рождения: ')
city = input('Введите свой город проживания: ')
phone = input('Введите свой номер телефона: ')
email = input('Введите свой email: ')

bio(name, sername, birthday, city, email, phone)


# 3 Реализовать функцию my_func()
def summa():
    x = float(input('Введите любое число: '))
    y = float(input('Введите любое число: '))
    z = float(input('Введите любое число: '))
    numbers = [x, y, z]
    numbers.sort()
    addition = numbers[1] + numbers[2]
    return addition


print(summa())


# 4 Программа принимает действительное положительное число x и целое отрицательное число y.
def exponentiation(x1, y1):
    z1 = x1 ** y1
    return z1


x1 = float(input('Введите действительное положительное число: '))
while x1 < 0:
    x1 = float(input('Введите действительное положительное число: '))
y1 = int(input('Введите целое отрицательное число: '))
while y1 >= 0:
    y1 = int(input('Введите целое отрицательное число: '))

print(exponentiation(x1, y1))

# 5 Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
STOP = '!'

su = 0
to_exit = False
while not to_exit:
    next_input = input('Введите числа через пробел, для остановки сложения введите "!": ' '\n')
    numeral = next_input.split()
    for num in numeral:
        if num == STOP:
            to_exit = True
            break

        try:
            num = int(num)
        except ValueError:
            continue

        su += num
    print(f'Сумма - {su}')


# 6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func():
    bad = 'Повторите ввод латинскими маленькими буквами!!!!'
    word_lat = word.isascii()
    if word_lat == True:
        return (word.title())
        print('Good job!!!')
    else:
        return bad

while True:
    word = input('Введите словосочетание маленькими латинскими буквами через пробел: ')
    print(int_func())
