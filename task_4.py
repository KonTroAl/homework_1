"""
Задание 4.

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
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

"""
First
Difficulty: 

"""

# def activations(nam):
#     for i in users_activation:
#         if i == nam:
#             return True
#         else:
#             c = input("You need to activate your account!Do you want activate it now?(Enter 'Yes' or 'No') ")
#             if c == "Yes":
#                 users_activation.append(nam)
#             else:
#                 return False
#
# def authentication(nam, pas):
#     for k, v in users_storage.items():
#         if k == nam and v == pas:
#             if activations(nam) == True:
#                 print("Welcome!")
#                 break
#             else:
#                 print("Permission to our site denied!")
#                 break
#         else:
#             print("Your login or password incorrect!")
#
# users_storage = {"Kostya": 111111, "Julia": 222222}
# users_activation = ["Julia"]
#
# a = input("Enter your name: ")
# b = int(input("Enter your password: "))
#
# authentication(a, b)

"""
Second
Difficulty: 

"""

def authentication(nam, pas):
    for k, v in users_storage.items():
        if k == nam and v == pas:
            for i in users_activation:
                if i == nam:
                    print("Welcome!")
                    break
                else:
                    c = input("You need to activate your account!Do you want activate it now?(Enter 'Yes' or 'No') ")
                    if c == "Yes":
                        users_activation.append(nam)
                    else:
                        print("Permission to our site denied!")
                        break
            break
        else:
            print("Your login or password incorrect!")

users_storage = {"Kostya": 111111, "Julia": 222222}
users_activation = ["Julia"]

a = input("Enter your name: ")
b = int(input("Enter your password: "))

authentication(a, b)

