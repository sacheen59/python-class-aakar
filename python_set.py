# students= {
#     "Physics":78,
#     "Chemistry":85,
#     "maths":98,
#     "Health":82,
#    "Computer":92
# }

# hightest marks subject marks

# set => unordered, unindexed, duplicate not allowed

# defining set 
# number = {1,4,5,6,10,20,9,5}
# fruits = {"mango","apple","orange","papaya"}
# print(type(number))
# print(number)
# print(fruits)
# print(number)
# print(number)

# access
# print(fruits[0])
# for i in fruits:
#     if i == "apple":
#         print(i)
#         break


# numbers = [2,3,43,3,4,5,2,3,5]
# print(set(numbers))

# fruits = {"mango","apple","orange","papaya","pumpkin"}

# fruits.add("pineapple")
# print(fruits)

# veg_list = ["tomato","potato","pumpkin"]

# fruits.update(veg_list)
# print(fruits)

# remove 

# remove(),pop(),discard()
# number = {"mango","papaya","apple"}
# number.pop()
# print(number)

# remove()
# number.remove("pineapple")
# print(number)

# discard()
# number.discard("pineapple")
# print(number)

# union, intersection ,difference, symmetric_difference ...

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

# for union we use union() or | symbol
# C = A.union(B)
# C = A | B
# print(C)

# for intersection we use intersection() or & 
# C = A.intersection(B)
# C = A & B
# print(C)


# whole_numbers = [0,1,2,3,4,5,6,7,8,9]
# even_numbers = [0,2,4,6,8]

# print(set(whole_numbers) | set(even_numbers))

# print(set(whole_numbers) & set(even_numbers))

numbers = {1,2,3,4,5,6,7}
second_numbers = {4,5,6,7}
# difference = numbers.difference(second_numbers)
# difference = numbers - second_numbers
# print(difference)

print(second_numbers.issubset(numbers))

