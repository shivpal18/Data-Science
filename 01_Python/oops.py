# class Factory:
#     a=12  #attribute

#     def hello(self):  #method
#         print("how are you")

# print(Factory().a)
# Factory().hello()



# class Factory:
#     a=12  #attribute

#     def hello(self):  #method
#         print("how are you")

# obj = Factory()
# print(obj.a)
# obj.hello()



# class Factory:
#     def __init__(self, material, zips, pockets):
#         print(self)
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"your object details are: {self.material}, {self.pockets}, {self.zips}")

# rebook = Factory("leather", 3, 2)
# campus = Factory("nylon", 3, 3)

# print(rebook.pockets)
# rebook.show()



# class Animal:
#     name = "lion"   #class attribute

#     def __init__(self,age):
#         self.age = age   #instance attribute

#     def show(self):  #instance method
#         print(f"how are you your age is {self.age}") 

#     @classmethod
#     def hello(cls):
#         print("how are you")

#     @staticmethod
#     def static():
#         print("how are you bro")

# obj = Animal(12)
# obj.static()




# INHERITANCE


# class Factorymumbai:   #parent class / superclass
#     a="I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello i am a method mentioned inside factory")

# class Factorypune(Factorymumbai):  #child class / subclass
#     pass

# obj = Factorymumbai()
# obj2 = Factorypune()
# print(obj2.hello())



# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"hello my name is {self.name} and age is {self.age}")

# animal1 = Animal("lion")
# person1 = Human("shivpal",21)
# person1.show()
# animal1.show()



# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human, Animal):
#     name3 = "charli123"

# obj = Robots()
# # print(obj.name2)



# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets



# POLYMORPHISM

# class Animal:
#     def show2(self):
#         print("hello i am shivpal")

# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show2()



# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("hello i am also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()



# ENCAPSULATION

# class Factory:
#     _a = "pune"

#     def _show(self):
#         print("hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super()._a)

# obj = Bhopal()
# obj.show2()



# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)

# obj = Factory()
# obj.show()



# ABSTRACTION

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#             print("i have created")
    
#     def area(self):
#         print("i have created this")

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius

#     def perimeter(self):
#         print("i have created")

#     def area(self):
#         print("i have created this")

# obj = Circle(7)
# obj2 = Square(2)




# DUNDER METHODS

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"

    def __add__(self, other):
        return f"your sum of ages are {self.age + other.age}"

obj = Animal("lion",12)
obj2 = Animal("dolphin",14)
print(obj + obj2)



