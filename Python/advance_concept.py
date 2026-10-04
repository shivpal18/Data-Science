
# DECORATOR

# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")

# obj = Animal()
# obj.show



# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your number are ")
#         func(a,b)
#         print("thnak you i hope you liked it")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"your total is {a+b}")

# addition(12,45)



# ARGS & KWARGS

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# addition(3,23,534,6,56,77,)



# def addition(**kwargs):
#     print(kwargs)

# addition(a=12,b=34,c=23)



# def information(**kwargs):
#     print("your information is: \n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "shivpal", age = "20", designation = "data scientist")



# LIST, DICTIONARY AND SET COMPHREHENSION

# l = [i for i in range(1,21) if i%2==0]
# print(l)

# l = {i : i**2 for i in range(1,10)}
# print(l)



# LAMBDA FUNCTION

# addition = lambda a,b : a+b
# print(addition(12,13))



# addition = lambda a: "even" if a % 2==0 else "odd"
# print(addition(18))



# MAP, FILTER

# a = [1,2,3,4,5]
# result = map(lambda x:x*2, a)
# print(list(result))



# a = [1,2,3,4,5]
# def double(x):
#     return x*2
# result = map(double, a)
# print(list(result))



# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# a=[1,2,3,4,5,6,7,8,9]
# result = filter(even, a)
# print(list(result))



# a=[1,2,3,4,5,6,7,8,9]
# result = filter(lambda x: True if x%2==0 else False, a)
# print(list(result))



# MODULES AND PACKAGES

# import maths
# print(maths.addition(12,12))



# from maths import addition
# print(addition(12,14))



# ITERATOR & GENERATORS

# def gen(n):
#     for i in range(n):
#         yield i

# print(gen(10000))
# for i in gen(100):
#     print(i)



# def gen(n):
#     for i in range(n):
#         yield i

# ob1 = gen(4)
# print(next(ob1))
# print(next(ob1))



# ZIP FUNCTION

# l = [10,20,30,40]
# l1 = [1,2,3,4]

# for a,b in zip(l,l1):
#     print(a,b)



# ANY & ALL FUNCTION

# numbers = [False, False, True, False]
# print(any(numbers))

# numbers = [False, False, False]
# print(any(numbers))

# numbers = [True, True, True]
# print(all(numbers))

# numbers = [True, True, False, True]
# print(all(numbers))



# REGULAR EXPRESSION

import re

# text = "My phone number is 7607812407"
# result = re.search(r"\d+", text)
# print(result.group())



# text = "I have 123 apples and 456 oranges"
# numbers = re.findall(r"\d+", text)
# print(numbers)



# text = "Contact me at abc@gmail.com"
# pattern = r"[\w.-]+@[\w.-]+\.\w+"
# result = re.findall(pattern, text)
# print(result)



# text = "My phone number is 7607812407"
# result = re.sub(r"\d", "*", text)
# print(result)



text = """
My name is Shivpal.
My age is 21.
My phone is 7607812407.
My marks are 85.
"""
numbers = re.findall(r"\d+", text)
print(numbers)