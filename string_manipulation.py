# array is an ADT(Abstract Data type)
# CRUD
# create, retrieve, update, delete

# mutable  and immutable
# mutable => changeable (update,add,remove)
# list, dict,

# immutable => unchangeable (update, add, remove)
# string

# text = 'we are learning python django'
# # text = ['w','e',' ','a',...]
# # text[0] = 'r'
# for letter in text:
#     print(letter)

# quotes
# text = "It's a python class"
# print(text)
# next_text = "we are learning from \"sachin barali\""
# print(next_text)

# text = "we are learning python"

# access/retrive
# print(text[0])
# print(text[3])

# range of value
# [start:end:step]
# print(text[0:15])
# print(text[16:22])

# [start:] => start from the given index character and remaining all

# print(text[16:])

# print(text[:6])

# print(text[0:22:2])

# print(text[::2])

# negative indexing
# print(text[-1])
# print(text[-2])
# print(text[-6:]) 

# start value must be smaller than stop value
# print(text[0:6])

# first_name = "sachin" # index 0 - 5, len() => 1 - 6, range(len(first_name), range(0:6), 0 - 5

# print("0 => s")
# length
# index - length
# first_name[index]

# for i in range(len(first_name)):
#     print(i, first_name[i])

# concatenation
# firstname = "sachin"
# lastname = "barali"
# full_name = firstname + " " + lastname
# print(full_name)

# requirements:
# user can input a number
# if user number is equal to the number of your system
# print congratulations you gussed it
# else print your guessed is worng
# user can guess only 3 times

# for while

# else

# for i in range(3):
#     print(i)
# else:
#     print("The loop is terminated")

# system_number = 10

# for i in range(3):
#     user_guess = int(input("Guess your number 0 - 20: "))
#     if user_guess == system_number:
#         print("you have guessed the number")
#         break
#     else:
#         print("your guess is wrong please try again")
# else:
#     print("your attemp is failed")


# system_number = 2
# count = 0

# while count < 3:
#     user_input = int(input("Enter a number: "))
#     if user_input == system_number:
#         print("you guessed it right")
#         break
#     else:
#         print("you guessed it wrong please try again")
#     count+=1
# else:
#     print("your attempt is finished")


# upper() and lower()

# text = "we are learning python"
# print(text.upper())

# upper_text = "WE ARE DOING GREAT"
# print(upper_text.lower())

# username = "sachin"
# user_input = input("Enter your name: ")

# if username == user_input.strip():
#     print("you are logged in")
# else:
#     print("login failed")

# removing white space => strip()

# name = "   tripti   "
# print(len(name))
# strippted_text = name.strip()
# print(len(strippted_text))


# name = "#########sachin#######"
# # print(name.strip('#'))
# # rstrip()
# # lstrip()
# print(name.rstrip('#'))
# print(name.lstrip('#'))

# text = "    #####Shandya#####    "
# # print(text.strip())
# formatted_text = text.strip()
# result = formatted_text.strip("#")
# print(result)

name = "_______#####*****Tripti*****####______"

# first = name.strip("_")
# # print(first)
# second = first.strip("#")
# # print(second)
# result = second.strip('*')
# print(result)

# result = name.strip('_').strip('#').strip('*')
# print(result)

# replace("source character","destination character")

# text = "we are learning python"
# # print(text.replace("python","Django")
# print(text.replace('e','a'))

# split() => split the sentence into the array of string form the given character

# greeting = "Hello, Everyone"
# print(greeting.split(','))

# email = "triptitiwari625@gmail.com"
# print(email.split('.')[0])

# url = "https://www.youtube.com"
# print(url.split('/'))

# find() => position value
# text = "we are learning python and python is very easy to learn"
# print(text.find("python"))
# print(text.find('e'))
# print(text.count('python'))

# startsWith and endsWith

# email = "triptitiwari@gmail.com.np"

# print(email.startswith(".np"))
# print(email.endswith('.com.np'))

# user input gmail
# end edu.np
# your email is valid
# email invalid

# user_email = input("enter your email: ")
# if user_email.endswith("edu.np"):
#     print("Valid email")
# else:
#     print("Invalid email")

# formatted string

fullname = "sachin barali"
age = 22
# print("my name is " + fullname + " I am " + age + " years old")

# format()

# result = "my name is {}. I am {} years old".format(fullname,age)
# result = "my name is {1}. I am {0} years old".format(age, fullname)
# print(result)

# f-string 
# result = f"my name is {fullname}. I am {age} years old."
# print(result)


# email => uppercase
# password => fkljdlfkjdlfjdlkj
# email password match login successful 
# login failed

name = "############sachin###########"

middle_text = name.strip('#')
length_of_name = len(name)
strip_left = len(name.lstrip("#"))
strip_right = len(name.rstrip('#'))

count_left_hash = length_of_name - strip_left
# print(count_left_hash)
count_right_hash = length_of_name - strip_right
                # 12
result = '*' * count_left_hash + middle_text + '*' * count_right_hash
print(result)


