# decorators => higher order function which modifies or extend the functionalities of function without changing its structure


# function as first class citizen 
# it can be store in variable 
# it can pass as a arguement
# it can be reutrn as the result

# higher order function

# def greet(func):
#     if True:
#         return func()
   
# def function():
#     return "hello world"
    
# print(greet(function))

# is_signin = True
# def signin(func):
#     if is_signin:
#         return func()

# def cart():
#     pass

# def order():
#     pass
# signin(cart)

# signin(order)

# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper


# @decorator
# def greet():
#     print("hello world")
    
# greet()

# def sum_decorator(func):
#     def wrapper(a,b):
#         if a > 0 and b > 0:
#             return func(a,b)
#         else:
#             return "your both number must be positive" 
#     return wrapper

# @sum_decorator
# def sum(x,y):
#     return x + y

# print(sum(-1,20))


# user_info = {
#     "username": "sachin",
#     "is_logged_in": True
# }

# def signin_decorator(func):
#     def wrapper(*args,**kwargs):
#         if args[0]["is_logged_in"]:
#             return func(*args,**kwargs)
#         else:
#             return "Please do login for accessing this page"
#     return wrapper

# @signin_decorator
# def welcome(user):
#     return f"welcome {user["username"]}"
   
# @signin_decorator
# def cart(user):
#     return f"This is the cart of {user["username"]}"

# @signin_decorator
# def order(user):
#     return f"this is the order of {user["username"]}"

# print(welcome(user_info))
# print(cart(user_info))
# print(order(user_info))

# def method_decorator(method):
#     def signin_decorator(func):
#         def wrapper(*args,**kwargs):
#             if kwargs["is_logged_in"] and method == 'post':
#                 return func(*args,**kwargs)
#             else:
#                 return "Please do login for accessing this page"
#         return wrapper
#     return signin_decorator


# @method_decorator('get')
# def greet(**kwargs):
#     return f"welcome {kwargs["username"]}"

# print(greet(username = "sachin",is_logged_in = True))

# method=> get /post 

# verify_age()

# age() 16 is satisfied for citizenship


# userinput = int(input("Enter your age: "))

# def verify_age(func):
#     def wrapper(a):
#         if a >= 16:
#             return func(a)
#         else:
#             return f"{a} is not setisfied for citizenship"
#     return wrapper

# @verify_age
# def age(age):
#     return f"{age} is verified for citizenship"

# print(age(userinput))


# def greet():
#     """this is a function for greeting"""
#     pass

# def age():
#     """This is function for age"""
#     pass

