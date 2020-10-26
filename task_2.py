"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

"""Second O()"""

def my_min(lst):
    for i in lst:
        is_min = True
        for val in lst:
            if i > val:
                is_min = False
        if is_min:
            return i


a = [2, 4, 1, 5, 10]

print(my_min(a))

"""Second O(n)"""

def my_min(lst):

    count = lst[0]
    for i in lst:
        if i < count:
            count = i
    return count


a = [2, 4, 1, 5, 0]

print(my_min(a))


