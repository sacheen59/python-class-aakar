# tuple => immutable, order, unchangeable

fruits = ("apple","banana","mango","orange")
# print(type(fruits))

# fruits[0] = "papaya"
# print(fruits)

# print(fruits[1])
# print(fruits[-1])

# y = list(fruits)
# y.append("papaya")
# fruits = tuple(y)
# print(fruits)

veg = ("tomato","potato","ladyfinger","pumpkin")

# result = fruits + veg
# print(result)

# double_fruits = fruits * 2
# print(double_fruits)

# my_number = (1,)
# print(type(my_number))

# tuple_unpacking 
# fruits = ("mango","papaya","apple","orange")
# fruits = "mango","papaya","apple","banana"
# print(type(fruits))

# # *args
# a,*b = fruits
# print(a)
# print(b)
# print(d)

# number = [2,3,4,5,6,7]
# total sum 
# total_sum = sum(number)
# print(total_sum)

# total_sum = 0
# for num in number:
#     total_sum+=num

# print(total_sum)

numbers = [
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (10,11,23),
    (55,44,66)
]

[[(1,2,3),6],[(4,5,6),15]]

# total_sum = 0

# for i in numbers:
#     for j in i:
#         total_sum += j

# print(total_sum)

# total_sum = 0
# for i in numbers:
#     total_sum+= sum(i)

# print(total_sum)

n = numbers[0] + numbers[1] + numbers[2]
print(sum(n))

# number1 = [1,2,3]
# number2 = [4,5,6]

# total_sum = []


# for i in range(len(number1)):
#     sum = 0
#     sum = number1[i] + number2[i]
#     total_sum.append(sum)

# print(total_sum)
