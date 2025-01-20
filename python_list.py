# list => collection of heterogenous data in contiguous memeory location

# array = [1,2.0,"sachin"]
# fruits = ["mango","apple","orange","pineapple","grapes","kiwi","strawberry"]
# print(type(fruits))

# fruits[1] = "banana"
# print(fruits)

# length of list
# print(len(fruits))

# access the list element
# print(fruits[0])
# print(fruits[-1])
# print(fruits[0:4])
# print(fruits[:4])
# print(fruits[4:])
# print(fruits[::2])

# changing range of item
# vegetables = ["potato","tomato","pumpkin","spanich","cauliflower"]
# vegetables[0:2] = ["pidlu","matatar"]
# print(vegetables)

# for veg in vegetables:
#     # print(veg)
#     if veg == "potato":
#         print("There is potato")

# if "potato" in vegetables:
#     print("yes")

# add items to the list append()
# vegetables.append("mutton")
# print(vegetables)

# # insert(index,value)
# vegetables.insert(2,"chicken")
# print(vegetables)

# concatenate
# veg = ["potato","tomato","pumpkin","spanich","cauliflower"]
# non_veg = ["mutton","pork","chicken","buff","beef"]
# result = veg + non_veg
# print(result)

# extend(new_list)

# veg.extend(non_veg)
# print(veg)

# veg += non_veg

# numbers = [1,2,3,4,5]

# [1,4,9,16,25]
# square_numbers = []
# for num in numbers:
#     square = num**2
#     square_numbers.append(square)

# print(square_numbers)

# access, add, join two list, remove

# facebook_post = ["dashain post","tihar post","birthday post","holi post"]
# facebook_post.append("loshar post")
# print(facebook_post)

# remove, pop 
# facebook_post.remove("tihar post")
# print(facebook_post)

# facebook_post.discard("loshar post")
# print(facebook_post)

# deleted_post = facebook_post.pop(0)
# print(deleted_post)

# clear
# facebook_post.clear()
# print(facebook_post)

# del
# del facebook_post
# print(facebook_post)

# user = ["sachin","sandhya","tripti","zenith"]
# 1) add user
# 2) remove user
# 3) delete whole user

# sort(), sorted(),reverse()
# number = [2,1,5,4,7,100,20,6]
# number.sort(reverse=True)
# print(number)
# print(number)
# number.reverse()
# print(number)

# sorted_number = sorted(number,reverse=True)
# print(sorted_number)

# shallow copy and deep copy
# number = [1,2,3,4,5,6]
# # second_number = number.copy()
# second_number = number[:]
# print(second_number)

# multi_array = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(multi_array)
# print(multi_array[0][0])
# print(multi_array[1][1])

# for i in multi_array:
#     for j in i:
#         print(j)

# marksheet = [
#     "sachin",
#     12,
#     [29,30,40,50,60]
# ]

# name: sachin
# class: 12
# english: 30

# print(f"Name = {marksheet[0]}")
# print(f"Grade = {marksheet[1]}")
# print(f"English = {marksheet[2][1]}")
# from copy import deepcopy
# new_copy = deepcopy(marksheet)
# print(new_copy)

# number = list()
# print(number)