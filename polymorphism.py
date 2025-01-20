# +,

# string = concatenate
# number = addition

# method overloading
# method overriding

# simple example of polymorphism
# class Dog:
#     def walk(self):
#         print("Dog can walk")

# class Cat:
#     def walk(self):
#         print("Cat can walk")

# class Cow:
#     def walk(self):
#         print("Cow can walk")

# dog = Dog()
# cat = Cat()
# cow = Cow()
# dog.walk()
# cat.walk()
# cow.walk()

# for x in (dog,cat,cow):
#     x.walk()

# inheritance class polymorphism

# class Vehicle:
#     def move(self):
#         print("Vehicle can move")

# class Plane:
#     def move(self):
#         # super().move()
#         print("Plane can fly")

# class Yeti(Plane,Vehicle):
#     def move(self):
#         super().move()
#         print("This is yeti plane")

# plane = Plane()
# plane.move()
# yeti_plane = Yeti()
# yeti_plane.move()

# object oriented 
# file handling
# built in module => Date time, random, os
# decorator and generator
# module => import export 
# database sqlite 3 DBMS => create, retrive, update, delete query, where, orderby, index, field type(varchar, integer,text), primary key, foreign key
# parking system, library management, banking system

# remaining in oops 
# private attribute or methods and private name mangling
# abstract method 
# getter and setters


# class Vehicle:
#     def __init__(self):
#         self.__name = "Tripti Tiwari"

#     def __move(self):
#         print("Vehicle can move")

# car = Vehicle()
# # print(car.__name)
# print(car._Vehicle__name)
# car._Vehicle__move()

# getters and setters
# class Person:

#     def __init__(self):
#         self.__name = "Sandhya"

#     def get_name(self):
#         return self.__name

#     def set_name(self,value):
#         self.__name = value

# obj = Person()
# print(obj.get_name())
# obj.set_name("Tripti")
# print(obj.get_name())

# class Person:

#     def __init__(self):
#         self.__name = "Sandhya"

#     # @property and @attribute_name.setters

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self,value):
#         self.__name = value


# obj = Person()
# print(obj.name)
# obj.name = "Tripti"
# print(obj.name)

# abstract class

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
    
#     @abstractmethod
#     def brand(self):
#         pass

# class Plane(Vehicle):
#     def move(self):
#         print("Fly")

#     def brand(self):
#         print("Buddha Air")

# class Car(Vehicle):
#     def move(self):
#         print("Walk")
#     def brand(self):
#         print("BMW")
# obj = Plane()
# obj.brand()
# obj.move()
# car = Car()
# car.brand()
# car.move()

# dunder methods 
# __eq__ (==)
# __str__

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    

# person1 = Person("Sachin",12)
# person2 = Person("Pragya",15)

# print(person1)
# print(person2)

# if person1 == person2:
#     print("The two objects are same")

# import traceback
# class CustomException(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)

# age = int(input("Enter your age for vote: "))

# try:
#     if age < 18:
#         raise CustomException("Age mustnot be less than 18")
# except CustomException as e:
#     print(e)
#     traceback.print_exc()

