"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self):
        self.elems = []
        self.num = 10
        self.count = 1

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) < self.num:
            self.elems.append(el)
        else:
            self.count += 1
            self.elems.clear()
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def stack_size(self):
        return len(self.elems)

    def current_stack(self):
        return self.count

    def number_plates(self):
        return len(self.elems) + (self.num * self.count - 10)



plateStack = StackClass()

i = 568
val = 1
while val <= i:
    val += 1
    plateStack.push_in("plate")

print(plateStack.stack_size())
print(plateStack.current_stack())
print(plateStack.number_plates())
