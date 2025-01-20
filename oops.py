# class => blueprint of an object which contains data and methods
# object => instance of an class
# encapsulation => binding of attributes(data) and behaviour (methods)
# abstration => hiding the internal details private,pulbic,protected
# polymorphism => more than one form
# inheritance => inherit the property of parent class


# class Animal:
#     # pass
#     arms = 4
#     # behaviour or methods
#     def walk(self,name):
#         print(f"{name} can walk with {Animal.arms}")


# # # creating an object
# dog = Animal()
# dog.walk("Dog")
# cat = Animal()
# cat.walk("Cat")
# rabbit = Animal()
# rabbit.walk("Rabbit")
# dog.walk()

# x = 10
# print(type(x))

# class Animal:
#     def __init__(self,arms):
#         self.arms = arms
#         print(f"The animal can walk with {self.arms} legs")
#     # def display(self):
#     #     print("this is custom method")

# dog = Animal(arms = 4)
# bird = Animal(arms = 2)
# obj.display()
# obj2 = Animal()
# obj2.display()


# class Area:
#     def areaofCircle

#     def areaOfrectangle


# rectangle
# circle

# class Area:
#     def __init__(self,length, breadth=None):
#         self.length = length
#         self.breadth = breadth

#     def area_of_circle(self,radius):
#         area = 3.14 * radius ** 2
#         print(f"Area of circle is {area}")
    
#     def area_of_rectangle(self,length,breadth):
#         area = length * breadth
#         print(f"Area of rectangle is {area}")


# circle = Area()
# circle.area_of_circle(radius=10)
# rectangle = Area()
# rectangle.area_of_rectangle(length=10,breadth=20)

class Area:
    PI = 3.14
    
    def __init__(self,radius):
        self.radius = radius
        self.area = Area.PI * self.radius ** 2
        print(self.area)
    

circle1 = Area(10)
circle2 = Area(20)
