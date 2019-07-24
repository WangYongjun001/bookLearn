# coding: utf-8
# python内置函数等
from functools import reduce

# map, filter, reduce, 快速创建列表
list_a = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, list_a)))
print([x ** 2 for x in list_a])
print(list(map(lambda x: x >= 2, list_a)))
print([x >= 2 for x in list_a])
print(list(filter(lambda x: x >= 2, list_a)))
print(reduce(lambda x, y: x + y, list_a))
print(reduce(lambda x, y: x < y, list_a))
