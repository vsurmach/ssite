# a = {1, 'aaa', {1: 'a'}, [4, 5, 4]}
# a = {1:{1,2,3}}
# print(a)


# s = ['a', 'b', 'c']
# for i, v in enumerate(s):
#     print(f'{v} -> index {i}')


# def summa(a,b):
#     print(a+b)
#
#
# def multyply(a,b):
#     print(a*b)
#
#
# def fn(word):
#     if word == 's':
#         return summa
#     elif word == 'm':
#         return multyply
#
#
# res = fn('s')
# res(2,3)
# res2 = fn('m')
# res2(10,7)


# def counter_add(n):
#     def inner(k):
#         return n+k
#     return inner
#
#
# res=counter_add(7)
# print(res(5))


# def fn():
#     print('Я умная функция')
#
#
# def decorator(func):
#     print('Я красивая функция')
#     func()
#     print('Я успешная функция')
#
#
# decorator(fn)


# import requests
# import time
#
#
# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         res = time.time() - start
#         print('Время работы запроса--', res)
#     return wrapper
#
#
# @decorator
# def fn(url):
#     requests.get(url)
#
#
# # fn = decorator(fn())
# fn('http://google.com')


# def fn(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fn(n-1)
#
# print(fn(11))
#
#
# lst = [1, 3, 6, 8]
#
#
# def fn(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst.pop() + fn(lst)
# print(fn(lst))


# # Задача 1
# import copy
#
#
# def fn(lst):
#     def fn2(integer):
#         arr = []
#         for i in lst:
#             arr.append(i * integer)
#         return arr
#     return fn2
#
#
# # Задача 2
# a = [1, 2, 3, 4]
# a_copy = copy.copy(a)
# res = fn(a)
# print(res(3))
#
#
# def add(n):
#     def count(integer):
#         return n + integer
#     return count
#
#
# add_one = add(1)
# print(add_one(3))
# add_seven = add(7)
# print(add_seven(11))
#
#
# # Задача 3
# def _if(bul):
#     def func1():
#         print(True)
#
#     def func2():
#         print(False)
#     if bul == 1:
#         return func1
#     elif bul == 2:
#         return func2
#
#
# res = _if('''True or False or 1 or 2''')
# res()

#
# def rec(n):
#     if rec == 1:
#         return 1
#     else:
#         return n-1


# s = [1, 2, 3]
# res = map(lambda x: x * 2, s)
# print(list(res))
#
# """OR"""
#
# def fn(x):
#     return x * 2
#
# s = [1, 2, 3]
# res = map(fn, s)
# print(list(res))
#
# res_2 = filter(lambda x: x > 0, s)
# print(list(res_2))
#
# s_1 = ['Key', 'Johan', 'Oleg', 'Petya']
# res_3 = zip(s, s_1)
# print(dict(res_3))
#
#
# from functools import reduce
#
# res_4 = reduce(lambda x, y: x+y, s, 10)
# print(res_4)


# class Cat:
#     color = 'grey'
#     name = 'Barsik'

#     @classmethod
#     def say_miau(self):
#         print(f'Miau. I am {self.name}')
#
#     @classmethod
#     def set_color(cls, color):
#         cls.color = color
#
#     @staticmethod
#     def count(a, b):
#         return a + b
#     print(a + b)
#
# a = Cat()
# a.set_color = 'black'
# print(a.set_color)


# class Cat:
#     color = 'grey'
#     name = 'Barsik'
#     counter = 0
#
#     def __init__(self):
#         self.__class__.counter += 1
#
#
# a = Cat()
# print(Cat.counter)
# b = Cat()
# print(Cat.counter)
# c = Cat()
# print(Cat.counter)


# class Car():
#     ENGINE = 'Diesel' # public
#     _ENGINE = 'Diesel' # protected
#     __ENGINE = 'Diesel' # private
#
# print(Car.__dict__)
# print(Car._Car__ENGINE)


# class Car:
#     __ENGINE = 'Diesel'
#
#     @classmethod
#     def change_engine(cls, eng):
#         cls.__ENGINE = eng
#
#     @classmethod
#     def show_engine(cls):
#         return cls.__ENGINE
#
#
# Car.change_engine('Benzin')
# print(Car._Car__ENGINE)


# class Car:
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         self.age = age
#
#
# car = Car()
# car.age = 23
# print(car.age)


# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print('Say hi from A')
#
#
# class C(A):
#     def say_hi(self):
#         print('Say hi from C')
#
#
# class B(C, A):
#     def say_hi(self):
#         print('Say hi from B')
#
#
# a = A('Johan')
# c = C('Peter')
# b = B('Sara')
# print(a.name)
# print(c.name)
# print(b.name)
# a.say_hi()



