# function => block of code which executes whenever we call it 

# function declaration
# function defination
# in python function defination & declaration
# function call

# signature function
# def sum(x,y)

# def sum(x , y): #x,y parameter
#     # x = 10
#     # y = 20
#     print(x + y)

# sum(10,20) # 10, 20 arguement
# sum(3,4)
# sum(5,6)
# sum(7,8)
# sum(8,9)

# def diff(x,y):
#     print(x - y)

# diff(10,5)

# firstname
# lastname
# def information

# def information(fname,lname):
#     print(f"{fname} {lname}")

# firstname = input("Enter your firstname: ")
# lastname = input("Enter your lastname: ")

# information(firstname,lastname)

# requirement
# first_number, last_number
# addition
# subtraction
# division
# mulitplication

# choice
# +, - , /, *

# return 

# def sum(x,y):
#     sum = x + y
#     return sum
#     # return 30

# add = sum(10,20)
# print(add)


# def number(x,y,z):
#     print(x,y,z)

# print(number(10,20,30))

# postional argument and keyword or named argument 

# def info(fname,lname):
#     print(fname,lname)

# info("Barali","Sachin")
# info(lname="Barali",fname="Sachin")

# arbitary arguments(*args) and keyword arguments(**kwargs)

# def number(a,b,c,*args):
#     print(a,b,c,args)
#     # for i in args:
#     #     print(i)

# number(1,2,3)


# def information(**kwargs):
#     # print(kwargs["fname"])
#     for key, value in kwargs.items():
#         print(key,value)

# # information(fname="sachin",lname='Barali',age=20)
# information(fname="Zenith",lname="Dhakal",age=18,college = "Forbes",grade= "1st semester")




# sort and sorted
# numbers = [1,2,9,8,7,4,5]
# # numbers.sort()
# # print(numbers)
# next_number = sorted(numbers)
# print(next_number)


# lambda function
# single satement 
# built in function Map,Filter,Reduce,Any, All 

# syntax:
    # lambda parameer: return 

# def sum(x,y):
#     return x + y

# add = sum(10,20)
# print(add)

# add = lambda x,y: x + y
# print(add(10,20))

my_list = [[(1,2,3),20],[(4,5,6),10],[(6,7,8),2]]

my_list.sort(key=lambda item: item[1])
print(my_list)