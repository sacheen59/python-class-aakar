# map, filter, reduce

# map => function that iterate over the given sequence of data and apply the given function to the individual item and return map object
# map(function,iter)

# def square(x):
#     return x ** 2

# number = [1,2,3,4,5,6]
# # map(squre,[1,2,3,4,5,6])
# square_number = map(square,number)
# # print(list(square_number))
# print(square_number)
# # print(id(square_number))

# numbers = [1,2,3,4,5,6]
# cube_numbers = map(lambda x: x ** 3, numbers)
# print(list(cube_numbers))

# filter
# def even_number(x):
#     return x % 2 == 0

# numbers = [1,2,3,4,5,6,7,8]

# map_result = map(even_number,numbers)
# # filter_result = filter(even_number,numbers)
# filter_result = filter(lambda x: x%2 == 0,numbers)
# print(list(map_result))
# print(list(filter_result))

# odd_numbers = filter(lambda x: x % 2 != 0,numbers)
# print(list(odd_numbers))


# reduce => sequence of items , final reuslt single value

# from functools import reduce

# def total_price(x,y):
#     return x + y

# price = [40,30,120,50,60]

# total = reduce(total_price,price)
# print(total)
# print(sum(price))

# list, dict, tuple comprehesion,
# decorator and generator
# module 
# import export virtual env

# git and github
# database query
# python with database
# sql database xampp

