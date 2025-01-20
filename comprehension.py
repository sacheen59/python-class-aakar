# shorter syntax to generate the sequence collectioin on the basis of existing sequence collection

# list comprehension
numbers = [1,2,3,4,5,6]
# even_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

# even_numbers = [i for i in numbers if i % 2 == 0]
# print(even_numbers)

numbers = [1,2,3,4,5,6,7]
# output
# [False,True,False,True,False,True,False]

# result = ["True" if i % 2 == 0 else "False" for i in numbers]
# print(result)


# dictionary comprehension
result = {x: x**2 for x in numbers if x % 2 == 0}
print(result)

# {1: 'Odd',2: 'Even'}

# result = (i for i in numbers if i % 2 == 0)
# print(tuple(result))


# numbers = [1,2,3,4,5,6]

# result = {i ** 2 for i in numbers}
# print(result)

# numbers = [-2,-3,-1,0,1,2,3]
# # output
# # ['negative','zero','positive']

# result = ['positive' if x > 0 else 'negative' if x < 0 else 'Zero' for x in numbers]
# print(result)

s = "the quick fox jump over the lazy dog"
# output
# list comprehension
# [5,3,...]

splitted_text = s.split()
filtered_splitted_text = list(filter(lambda x:x != 'the', splitted_text))
result = [len(word) for word in filtered_splitted_text]
print(result)

# find the total sum of unique positive even numbers from the given set
# numbers = [
#     [-1,-2,3,9,2,1,2],
#     [2,3,0,-1,-2,-4],
#     [10,9,8,-8,-10,-4],
#     [2,3,4,0,-1,-2,-3]
# ]
