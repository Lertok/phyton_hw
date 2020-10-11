# 1 script of salary

from sys import argv

script, output_in_our, rate_per_our, premium = argv
print('Name of script: ', script)


def zp():
    x = int(output_in_our)
    y = int(rate_per_our)
    z = int(premium)
    salary = ((x * y) + z)
    print('Salary of this employee:', salary, '$')


zp()

# 2 Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

original_list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
m = [j for i, j in zip(original_list_1, original_list_1[1:]) if j > i]
print(m)
zip()

# 3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21

my_number = [el for el in range(20, 240) if el % 20 == 0]
print(my_number)

# 4

from collections import Counter

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

counts = Counter(lst)
unic = [x for x, n in counts.items() if n == 1]

print(unic)

# 5

from functools import reduce

original_num = [num for num in range(100, 1001) if num % 2 == 0]


def factor(prev, now):
    return prev * now


print(reduce(factor, original_num))

# 6

from itertools import count
from itertools import cycle


def get_count(from_num, to_num):
    gen = count(from_num)
    next_num = next(gen)

    while next_num <= to_num:
        yield next_num

        next_num = next(gen)


print(list(get_count(3, 10)))


def get_cycle(sequence, cycle_count):
    cycle_len = len(sequence)
    max_count = cycle_len * cycle_count

    item_count = 0

    for next_item in cycle(sequence):
        item_count += 1
        yield next_item

        if item_count >= max_count:
            break


print(list(get_cycle('abc', 2)))


# 7

def gen_fact(max_n):
    current_fact = 1
    current_n = 1
    while current_n <= max_n:
        current_fact *= current_n
        yield current_fact

        current_n += 1


gen_f = gen_fact(4)
print(list(gen_f))
