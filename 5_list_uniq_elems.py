#4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random
print('Введите количество элементов списка')
n = int(input())
lst = []
for i in range(n):
    element = random.randint(1, 10)
    lst.append(element)
print(lst)
print(len(set(lst)))
