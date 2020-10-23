"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""



company = {"LG": 20000, "HP": 300000, "MSI": 80000, "ProDuction": 100000, "GasLight": 150000}

"""First
Difficulty:O(n**3) """

lst = list(company.values())
max_val = []
count = 3

# while len(max_val) != count:
#     val = 0
#     i = 1
#     for a in lst:
#         if a > val:
#             i += 1
#             val = a
#     max_val.append(val)
#     lst.remove(val)
#
# company_max = []
# for k, v in company.items():
#     for c in max_val:
#         if v == c:
#             company_max.append(k)
#
# print(max_val)
# print(company_max)

"""Second"""

# while len(max_val) != count:
#     max_val.append(max(lst))
#     lst.remove(max(lst))
#
# company_max = []
# for k, v in company.items():
#     for c in max_val:
#         if v == c:
#             company_max.append(k)
#
# print(max_val)
# print(company_max)

"""Third"""
max_company = []
for k, v in company.items():
    max_company.append(m)