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
Difficulty: O(2n**3): 2n**3 + 4

"""

def activations(nam):       # Difficulty: n**3
    for i in users_activation:   # n
        if i == nam:             # n
            return True          # 1
        else:
            c = input("You need to activate your account!Do you want activate it now?(Enter 'Yes' or 'No') ")  # 1
            if c == "Yes":                                                                                     # n
                users_activation.append(nam)                                                                   # 1
            else:
                return False                                                                                   # 1

def authentication(nam, pas): # Difficulty: n**3
    for k, v in users_storage.items():
        if k == nam and v == pas:
            if activations(nam) == True:
                print("Welcome!")
                break
            else:
                print("Permission to our site denied!")
                break
        else:
            print("Your login or password incorrect!")

users_storage = {"Kostya": 111111, "Julia": 222222}  # 1
users_activation = ["Julia"]                         # 1


a = input("Enter your name: ")                       #1
b = int(input("Enter your password: "))              #1

authentication(a, b)

"""
Second
Difficulty: O(n**5): n**5 + 9 

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

"""
Summary
Первое решение эффективнее в связи с тем, что ресурсозатратные операции по перебору и сравнению элементов списка и 
словаря разделеные примерно по поплам через две разные функции, что уменьшает сложность как отдельной взятой функции, 
так и кода в целом
"""